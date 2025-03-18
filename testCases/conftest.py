import pytest
from selenium import webdriver

from pytest_metadata.plugin import metadata_key


@pytest.fixture

def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    else:
        driver = webdriver.Ie()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# Hook for adding Environment info to HTML Reports
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Practice Test Automation'
    config.stash[metadata_key]['Tester'] = 'Stephanie'

#Modify/delete Environment info to HTML Reports
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop('JAVA_HOME', None)
#     metadata.pop('Plugings', None)
