# encoding=utf-8
from selenium import webdriver
import time
from util import Logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.PageBase import Page
from util.configUtil import Configger

class HomePage(Page):

    # @Logging.log_call
    # def __init__(self,browserType):
    #     browser = webdriver.Chrome(browserType)
    #     self.browser = browser

    @Logging.log_call_time
    def open(self):
        self.browser.get(Configger().config["Pages"]["hub_url"])
        self.browser.maximize_window()
        # wait for feed section loaded
        self.waitForLoaded("hub-home-yourfeeds", By.CLASS_NAME)
        assert EC.title_is("Hub Home")

    # def close(self):
    #     self.browser.close()

    @Logging.log_call_time
    def searchInSearchBar(self, keyword):
        searchBar = self.browser.find_element_by_id("hubsearch")
        assert EC.title_is("Hub Search")
        searchBar.send_keys(keyword)
        self.waitForLoaded("//*[@id='all']/search-results-all/div/div[1]/div/h3", By.XPATH)

    # def waitForLoaded(self, class_name,locator_type, second = 10):
    #     locator = (locator_type, class_name)
    #     WebDriverWait(self.browser, second).until(EC.visibility_of_element_located(locator))
