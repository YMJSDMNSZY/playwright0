import re

import allure
import pytest
from pytest_playwright.pytest_playwright import CreateContextCallback
from playwright.sync_api import Page, expect, BrowserContext, Browser, Playwright
from utils.globalMap import GlobalMap

import hashlib
import shutil
import os
import sys
import warnings
from pathlib import Path
from typing import (
    Any,
    Callable,
    Dict,
    Generator,
    List,
    Literal,
    Optional,
    Protocol,
    Sequence,
    Union,
    Pattern,
    cast,
)

import pytest
from playwright.sync_api import (
    Browser,
    BrowserContext,
    BrowserType,
    Error,
    Page,
    Playwright,
    sync_playwright,
    ProxySettings,
    StorageState,
    HttpCredentials,
    Geolocation,
    ViewportSize,
)
from slugify import slugify
import tempfile

from typing import (
    Any,
    Callable,
    Dict,
    Generator,
    List,
    Literal,
    Optional,
    Protocol,
    Sequence,
    Union,
    Pattern,
    cast,
)




#
# @pytest.fixture()
# def hello_world():
#     print("hello")
#     yield
#     print("world")
#
#
# @pytest.fixture
# def page(context: BrowserContext) -> Page:
#     print("this is my page")
#     return context.new_page()


@pytest.fixture(scope="session",autouse=True)
def test_init(base_url):
    global_map = GlobalMap()
    global_map.set("baseurl",base_url)
    env=re.search("(https://)(.*)(.ezone.work)",base_url).group(2)
    global_map.set("env",env)



@pytest.fixture(scope="session")
def browser_context_args(browser_context_args,pytestconfig: Any):
    width,height= pytestconfig.getoption("--viewport")
    return {
        **browser_context_args,
        "viewport": {
            "width": width,
            "height": height,
        },
        "record_video_size": {
            "width": width,
            "height": height,
        }
    }


def pytest_addoption(parser: Any) -> None:
    group = parser.getgroup("playwright", "Playwright")
    group.addoption(
        "--viewport",
        action="store",  #把里面的东西拿过来
        default=[1400,900],
        help="viewport size set",
        type=int,
        nargs=2,
    )
    group.addoption(
        "--ui_timeout",
        default=30_000,
        help="locator timeout and expect timeout",
    )
    # group.addoption(
    #     "--headed",
    #     action="store_true",
    #     default=False,
    #     help="Run tests in headed mode.",
    # )

@pytest.fixture(scope="session")
def ui_timeout(pytestconfig):
    timeout=float(pytestconfig.getoption("--ui_timeout"))
    expect.set_options(timeout=timeout)
    return timeout


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.failed:
        try:
            for context in item.funcargs['browser'].contexts:
                for page in context.pages:
                    if page.is_closed():
                        continue
                    bytes_png = page.screenshot(timeout=5000, full_page=True)
                    allure.attach(bytes_png, f"失败截图---{page.title()}")
        except:
            ...


def _build_artifact_test_folder(
    pytestconfig: Any, request: pytest.FixtureRequest, folder_or_file_name: str
) -> str:
    output_dir = pytestconfig.getoption("--output")
    return os.path.join(
        output_dir,
        truncate_file_name(slugify(request.node.nodeid)),
        truncate_file_name(folder_or_file_name),
    )


def truncate_file_name(file_name: str) -> str:
    if len(file_name) < 256:
        return file_name
    return f"{file_name[:100]}-{hashlib.sha256(file_name.encode()).hexdigest()[:7]}-{file_name[-100:]}"



@pytest.fixture
def new_context(
    browser: Browser,
    browser_context_args: Dict,
    _artifacts_recorder: "ArtifactsRecorder",
    request: pytest.FixtureRequest,
    ui_timeout,
) -> Generator[CreateContextCallback, None, None]:
    browser_context_args = browser_context_args.copy()
    context_args_marker = next(request.node.iter_markers("browser_context_args"), None)
    additional_context_args = context_args_marker.kwargs if context_args_marker else {}
    browser_context_args.update(additional_context_args)
    contexts: List[BrowserContext] = []

    def _new_context(**kwargs: Any) -> BrowserContext:
        my_context = browser.new_context(**browser_context_args, **kwargs)
        my_context.set_default_timeout(ui_timeout)
        my_context.set_default_navigation_timeout(ui_timeout*2)
        original_close = my_context.close

        def _close_wrapper(*args: Any, **my_kwargs: Any) -> None:
            contexts.remove(my_context)
            _artifacts_recorder.on_will_close_browser_context(my_context)
            original_close(*args, **kwargs)

        my_context.close = _close_wrapper
        contexts.append(my_context)
        _artifacts_recorder.on_did_create_browser_context(my_context)
        return my_context

    yield cast(CreateContextCallback, _new_context)
    for context in contexts.copy():
        context.close()

class ArtifactsRecorder:
    def __init__(
        self,
        pytestconfig: Any,
        request: pytest.FixtureRequest,
        playwright: Playwright,
        pw_artifacts_folder: tempfile.TemporaryDirectory,
    ) -> None:
        self._request = request
        self._pytestconfig = pytestconfig
        self._playwright = playwright
        self._pw_artifacts_folder = pw_artifacts_folder

        self._all_pages: List[Page] = []
        self._screenshots: List[str] = []
        self._traces: List[str] = []
        self._tracing_option = pytestconfig.getoption("--tracing")
        self._capture_trace = self._tracing_option in ["on", "retain-on-failure"]

    def did_finish_test(self, failed: bool) -> None:
        screenshot_option = self._pytestconfig.getoption("--screenshot")
        capture_screenshot = screenshot_option == "on" or (
            failed and screenshot_option == "only-on-failure"
        )
        if capture_screenshot:
            for index, screenshot in enumerate(self._screenshots):
                human_readable_status = "failed" if failed else "finished"
                screenshot_path = _build_artifact_test_folder(
                    self._pytestconfig,
                    self._request,
                    f"test-{human_readable_status}-{index+1}.png",
                )
                os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
                shutil.move(screenshot, screenshot_path)
        else:
            for screenshot in self._screenshots:
                os.remove(screenshot)

        if self._tracing_option == "on" or (
            failed and self._tracing_option == "retain-on-failure"
        ):
            for index, trace in enumerate(self._traces):
                trace_file_name = (
                    "trace.zip" if len(self._traces) == 1 else f"trace-{index+1}.zip"
                )
                trace_path = _build_artifact_test_folder(
                    self._pytestconfig, self._request, trace_file_name
                )
                os.makedirs(os.path.dirname(trace_path), exist_ok=True)
                shutil.move(trace, trace_path)
        else:
            for trace in self._traces:
                os.remove(trace)

        video_option = self._pytestconfig.getoption("--video")
        preserve_video = video_option == "on" or (
            failed and video_option == "retain-on-failure"
        )
        if preserve_video:
            for index, page in enumerate(self._all_pages):
                video = page.video
                if not video:
                    continue
                try:
                    video_file_name = (
                        "video.webm"
                        if len(self._all_pages) == 1
                        else f"video-{index+1}.webm"
                    )
                    video.save_as(
                        path=_build_artifact_test_folder(
                            self._pytestconfig, self._request, video_file_name
                        )
                    )
                except Error:
                    # Silent catch empty videos.
                    pass
        else:
            for page in self._all_pages:
                # Can be changed to "if page.video" without try/except once https://github.com/microsoft/playwright-python/pull/2410 is released and widely adopted.
                if video_option in ["on", "retain-on-failure"]:
                    try:
                        page.video.delete()
                    except Error:
                        pass

    def on_did_create_browser_context(self, context: BrowserContext) -> None:
        context.on("page", lambda page: self._all_pages.append(page))
        if self._request and self._capture_trace:
            context.tracing.start(
                title=slugify(self._request.node.nodeid),
                screenshots=True,
                snapshots=True,
                sources=True,
            )

    def on_will_close_browser_context(self, context: BrowserContext) -> None:
        if self._capture_trace:
            trace_path = Path(self._pw_artifacts_folder.name) / create_guid()
            context.tracing.stop(path=trace_path)
            self._traces.append(str(trace_path))
        else:
            context.tracing.stop()

        if self._pytestconfig.getoption("--screenshot") in ["on", "only-on-failure"]:
            for page in context.pages:
                try:
                    screenshot_path = (
                        Path(self._pw_artifacts_folder.name) / create_guid()
                    )
                    page.screenshot(
                        timeout=5000,
                        path=screenshot_path,
                        full_page=self._pytestconfig.getoption(
                            "--full-page-screenshot"
                        ),
                    )
                    self._screenshots.append(str(screenshot_path))
                except Error:
                    pass


def create_guid() -> str:
    return hashlib.sha256(os.urandom(16)).hexdigest()
