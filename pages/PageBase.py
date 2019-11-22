# encoding=utf-8
from selenium import webdriver
from util import Logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import selenium.webdriver.remote.webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import conftest
class Page():

    @Logging.log_call_time
    def __init__(self, driver):
        assert driver is not None
        self.browser = driver

    @Logging.log_call_time
    def open(self):
        self.browser.get("https://hubdev1.corp.ebay.com")
        self.browser.maximize_window()
        # wait for feed section loaded
        self.waitForLoaded("hub-home-yourfeeds", By.CLASS_NAME)
        assert EC.title_is("Hub Home")

    def close(self):
        pass

    def waitForLoaded(self, class_name,locator_type, second = 20):
        locator = (locator_type, class_name)
        WebDriverWait(self.browser, second).until(EC.visibility_of_element_located(locator))

    # def click(self):
    #     self.browser.find_elements_by_xpath()
