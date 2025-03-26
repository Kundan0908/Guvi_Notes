from pickle import FALSE

import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",action="store", default="chrome")

@pytest.fixture(scope="function")
def InvokeBrowser(request):
    # driver = webdriver.Chrome()
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    driver.implicitly_wait(4)
    driver.get("https://www.demoblaze.com/index.html#")
    yield driver
    driver.close()
