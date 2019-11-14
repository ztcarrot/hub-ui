# encoding=utf-8

from util import Logging
from tests.TestBase import beforeAll
from tests.TestBase import beforeEach
from tests.TestBase import TestBase
from pages.homePage import homePage as hubHome
import pytest




@pytest.mark.usefixtures("beforeEach")
@pytest.mark.usefixtures("beforeAll")
class TestHomeSearch(TestBase):



    '''
    # @pytest.mark.Critical
    # @pytest.mark.Major
    # @pytest.mark.Minor
    # @pytest.mark.Low
    #@Logging.log_call
    '''
    def test_search_for_featured(self):

        home = hubHome("./drivers/chromedriver")
        home.open()
        home.searchInSearchBar("people")

        current_url = home.browser.current_url
        Logging.Logger().logger.info(current_url)
        assert current_url.split("/")[3] == "search?q=people", "test failed" + current_url
        home.browser.find_element_by_link_text("People Central")

        Logging.Logger().logger.info("search people and find people central")
        home.close()

    def test_search_for_featured_1(self):

        home = hubHome("./drivers/chromedriver")
        home.open()
        home.searchInSearchBar("people")

        current_url = home.browser.current_url
        Logging.Logger().logger.info(current_url)
        assert current_url.split("/")[3] == "search?q=people", "test failed" + current_url
        home.browser.find_element_by_link_text("People Central")

        Logging.Logger().logger.info("search people and find people central")
        home.close()



