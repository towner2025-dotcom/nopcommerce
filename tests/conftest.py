# conftest.py
import pytest
import platform
import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from pytest_metadata.plugin import metadata_key
from pytest_html import extras
from logs.logs_page import Log_Maker
from config.config import TestData
from pages.LogIn_Page import LoginPage

# ---------------- Screenshot folder ----------------
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


# ---------------- Pytest CLI option ----------------
def pytest_addoption(parser):
    """Add command line options"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use for testing: chrome, firefox, or edge"
    )


# ---------------- Register Custom Markers ----------------
def pytest_configure(config):
    """Add project metadata for HTML reports and register custom markers"""
    Log_Maker.info("Configuring Pytest")

    # Register custom markers
    config.addinivalue_line("markers", "regression: marks tests as regression tests")
    config.addinivalue_line("markers", "smoke: marks tests as smoke tests")
    config.addinivalue_line("markers", "order: specifies test execution order")

    # Add metadata for HTML reports
    if hasattr(config, "stash") and metadata_key in config.stash:
        metadata = config.stash[metadata_key]
        metadata["Project Name"] = "Towner"
        metadata["Tester"] = "Abbas_Dudekula"
        metadata["Execution Time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        metadata["Operating System"] = platform.system()
        metadata["OS Version"] = platform.version()
        metadata["Machine"] = platform.machine()
        metadata["Python Version"] = platform.python_version()

    Log_Maker.info("Test execution metadata configured")


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    """Clean up default unnecessary metadata."""
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


# ---------------- Session-scoped Driver with One-Time Login ----------------
@pytest.fixture(scope="session")
def driver_session(request):
    """
    Session-scoped driver - created once and shared across all tests
    Login happens once at the start
    """
    browser = request.config.getoption("--browser", default="chrome").lower()

    separator = "=" * 100
    Log_Maker.info(f"\n{separator}")
    Log_Maker.info("🚀 INITIALIZING SESSION - ONE TIME LOGIN")
    Log_Maker.info(f"{separator}")

    driver = None

    try:
        # Initialize browser based on type
        Log_Maker.info(f"Initializing {browser} browser")

        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        elif browser == "edge":
            driver = webdriver.Edge()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.maximize_window()
        driver.implicitly_wait(10)
        Log_Maker.info(f"Browser {browser} initialized and maximized")

        # Navigate to base URL
        driver.get(TestData.BASE_URL)
        Log_Maker.info(f"Navigated to: {TestData.BASE_URL}")

        # ONE-TIME LOGIN
        Log_Maker.info(f"{separator}")
        Log_Maker.info("🔐 PERFORMING ONE-TIME LOGIN FOR SESSION")
        Log_Maker.info(f"{separator}")

        login_page = LoginPage(driver)
        Log_Maker.info(f"👤 Logging in with user: {TestData.User_Name}")
        login_page.do_login(TestData.User_Name, TestData.User_Password)

        Log_Maker.info("✅ LOGIN SUCCESSFUL - Session Started")
        Log_Maker.info(f"{separator}\n")

        yield driver

    finally:
        if driver:
            Log_Maker.info(f"\n{separator}")
            Log_Maker.info("🔚 CLOSING SESSION - Cleaning up")
            Log_Maker.info(f"{separator}")
            driver.quit()
            Log_Maker.info("Browser closed successfully")


# ---------------- Function-scoped Wrapper ----------------
@pytest.fixture(scope="function")
def init_driver(driver_session, request):
    """
    Function-scoped fixture that provides the session driver to each test
    No login needed - already logged in!
    """
    # Provide the already-logged-in driver to the test class
    request.cls.driver = driver_session

    yield

    # No cleanup here - session handles it


# ---------------- Screenshot on Failure ----------------
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot on test failure and attach to HTML report."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        if report.failed:
            driver = getattr(item.instance, "driver", None)
            if driver:
                test_name = item.name
                screenshot_timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_file = os.path.join(SCREENSHOT_DIR, f"{test_name}_{screenshot_timestamp}.png")

                try:
                    driver.save_screenshot(screenshot_file)
                    Log_Maker.error(f"❌ Test FAILED: {test_name}")
                    Log_Maker.error(f"📸 Screenshot saved: {screenshot_file}")

                    # Attach screenshot to HTML report
                    if hasattr(report, "extra"):
                        html = f'<div style="margin:10px 0;padding:10px;border:2px solid #ff4444;background-color:#fff5f5;">' \
                               f'<strong style="color:#cc0000;">❌ Failed Test: {test_name}</strong><br>' \
                               f'<p style="color:#666;margin:5px 0;">Timestamp: {screenshot_timestamp}</p>' \
                               f'<a href="{screenshot_file}" target="_blank">' \
                               f'<img src="{screenshot_file}" style="width:600px;height:auto;margin-top:10px;border:1px solid #ccc;box-shadow:0 2px 4px rgba(0,0,0,0.1);"/></a>' \
                               f'</div>'
                        report.extra.append(extras.html(html))
                except Exception as e:
                    Log_Maker.error(f"Failed to capture screenshot: {str(e)}")

        elif report.passed:
            Log_Maker.info(f"✅ Test PASSED: {item.name}")


# ---------------- Test Start Hook ----------------
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    """Log when a test starts"""
    test_name = item.name
    separator = "=" * 80
    Log_Maker.info(f"\n{separator}")
    Log_Maker.info(f"Starting Test: {test_name}")
    Log_Maker.info(f"{separator}")


# ---------------- Test End Hook ----------------
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_teardown(item, nextitem):
    """Log when a test ends"""
    test_name = item.name
    separator = "=" * 80
    Log_Maker.info(f"{separator}")
    Log_Maker.info(f"Finished Test: {test_name}")
    Log_Maker.info(f"{separator}\n")


# ---------------- Session Start/End ----------------
def pytest_sessionstart(session):
    """Log session start"""
    separator = "=" * 100
    Log_Maker.info(f"\n{separator}")
    Log_Maker.info("🚀 TEST EXECUTION STARTED")
    Log_Maker.info("Project: Towner Automation Framework")
    Log_Maker.info("Tester: Abbas_Dudekula")
    Log_Maker.info(f"Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    Log_Maker.info(f"{separator}\n")


def pytest_sessionfinish(session, exitstatus):
    """Log session end"""
    separator = "=" * 100
    status_message = "✅ SUCCESS" if exitstatus == 0 else f"❌ FAILED (Exit Code: {exitstatus})"

    Log_Maker.info(f"\n{separator}")
    Log_Maker.info("🏁 TEST EXECUTION COMPLETED")
    Log_Maker.info(f"Status: {status_message}")
    Log_Maker.info(f"Exit Status Code: {exitstatus}")
    Log_Maker.info(f"Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    Log_Maker.info(f"{separator}\n")