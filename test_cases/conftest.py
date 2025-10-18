import pytest
import platform
import datetime
import getpass
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

def pytest_addoption(parser):
    """Add browser option to the command line"""
    parser.addoption("--browser", action="store", default="chrome",
                     help="Type of browser: chrome or edge or firefox")


@pytest.fixture()
def setup(request):
    """Fixture to initialize the browser based on command-line input"""
    browser = request.config.getoption("--browser")

    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()

# ---------- Add Project Metadata to Pytest HTML Report ----------
def pytest_configure(config):
    """Automatically add metadata to pytest-html or pytest-metadata plugin"""
    if hasattr(config, "stash") and metadata_key in config.stash:
        metadata = config.stash[metadata_key]
    else:
        return

    metadata["Project Name"] = "NopCommerce Admin Automation"
    metadata["Tester"] =  "Abbas_Dudekula"   #getpass.getuser()    Automatically gets your system username
    metadata["Execution Time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    metadata["Operating System"] = platform.system()
    metadata["OS Version"] = platform.version()
    metadata["Machine"] = platform.machine()
    metadata["Python Version"] = platform.python_version()


# ---------- Optional: Clean up unnecessary default metadata ----------
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    """Remove unwanted default keys"""
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)