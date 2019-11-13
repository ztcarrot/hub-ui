# encoding=utf-8
from selenium import webdriver
import time
from util import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class homePage(object):

    def __init__(self,browserType):
        browser = webdriver.Chrome(browserType)
        self.browser = browser

    def open(self):
        logger.info('navigate to home page start ')
        self.browser.get("https://hubdev1.corp.ebay.com")
        self.browser.maximize_window()
        # wait for feed section loaded
        self.waitForLoaded("hub-home-yourfeeds", By.CLASS_NAME)


        assert EC.title_is("Hub Home")
        logger.info('navigate to home page end')

    def close(self):
        logger.info('close browser')
        self.browser.close()
        logger.info('browser is closed')

    def searchInSearchBar(self, keyword):
        logger.info('start search')
        searchBar = self.browser.find_element_by_id("hubsearch")
        assert EC.title_is("Hub Search")
        searchBar.send_keys(keyword)
        self.waitForLoaded("//*[@id='all']/search-results-all/div/div[1]/div/h3", By.XPATH)
        logger.info('end search')


    def waitForLoaded(self, class_name,locator_type, second = 10):
        logger.info("load page start")
        locator = (locator_type, class_name)
        WebDriverWait(self.browser, second).until(EC.visibility_of_element_located(locator))
        logger.info("load page successfully")
