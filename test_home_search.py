# encoding=utf-8
from selenium import webdriver
from util import logger
from pages.homePage import homePage as hubHome
import pytest
def test_search_for_featured():
    home = hubHome("./drivers/chromedriver")
    home.open()
    home.searchInSearchBar("people")
    #
    current_url = home.browser.current_url
    logger.info(current_url)
    assert current_url.split("/")[3] == "search?q=people", "test failed" + current_url
    home.browser.find_element_by_link_text("People Central")

    logger.info("search people and find people central")
    home.close()




