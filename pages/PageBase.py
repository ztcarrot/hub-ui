# encoding=utf-8
from selenium import webdriver
from util import Logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class Page():

    @Logging.log_call
    def __init__(self,browserType):
        browser = webdriver.Chrome(browserType)
        self.browser = browser

    @Logging.log_call
    def open(self):
        self.browser.get("https://hubdev1.corp.ebay.com")
        self.browser.maximize_window()
        # wait for feed section loaded
        self.waitForLoaded("hub-home-yourfeeds", By.CLASS_NAME)
        assert EC.title_is("Hub Home")

    def close(self):
        self.browser.close()

    def waitForLoaded(self, class_name,locator_type, second = 20):
        locator = (locator_type, class_name)
        WebDriverWait(self.browser, second).until(EC.visibility_of_element_located(locator))
