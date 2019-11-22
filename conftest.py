import pytest
import time
import datetime
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from util import configUtil
import selenium
browser_list = configUtil.Configger().config["pytest"]["browser_list"].split(",")
print("Test for browsers: %s" % browser_list)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    # PyTest has an incremental marker that will mark all dependent tests as expected to fail,
    # so they don’t get executed.
    # add @pytest.mark.incremental before Class
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item

    # save image in the report
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        extra.append(pytest_html.extras.url('https://www.hubdev1.corp.ebay.com/'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            # capture_screenshot
            item.cls.driver.get_screenshot_as_file(("report/"+file_name))
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                   'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed (%s)" %previousfailed.name)


@pytest.fixture(params=browser_list, scope="class", autouse=True)
def setup(request):
    driver_type = None
    if request.param == "chrome":
        driver_type = DesiredCapabilities.CHROME
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver_type = DesiredCapabilities.FIREFOX
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver_type = DesiredCapabilities.EDGE
        driver = webdriver.Edge()
    elif request.param == "safari":
        driver_type = DesiredCapabilities.SAFARI
        driver = webdriver.Safari()
    else:
        print("not supported browser")

    if configUtil.Configger().config["selenium_server"]["enable_remote"] is "True":
        remote_url = configUtil.Configger().config["selenium_server"]["remote_url"]
        driver = selenium.webdriver.remote.webdriver.WebDriver(command_executor=remote_url, desired_capabilities=driver_type)

    request.cls.driver = driver
    yield
    # before all test case finished
    request.cls.driver.close()


@pytest.fixture(scope="module", autouse=True)
def mod_header(request):
    print('\n-----------------')
    print('module      : %s' % request.module.__name__)
    print('start time  : %s' % time.asctime())
    print('-----------------')
    yield
    print('\n-----------------')
    print('module      : %s' % request.module.__name__)
    print('end time    : %s' % time.asctime())
    print('-----------------')


@pytest.fixture(scope="function", autouse=True)
def func_header(request):
    print('\n       -----------------')
    print('       function    : %s' % request.function.__name__)
    print('       start time  : %s' % time.asctime())
    print('       -----------------')
    yield
    print('\n       -----------------')
    print('       module      : %s' % request.function.__name__)
    print('       end time    : %s' % time.asctime())
    print('       -----------------')

