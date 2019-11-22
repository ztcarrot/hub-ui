# encoding=utf-8

from util import Logging
from tests.TestBase import TestBase
from pages.homePage import HomePage as hubHome
import pytest

@pytest.mark.Major
@pytest.mark.usefixtures("beforeEach")
@pytest.mark.usefixtures("beforeAll")
@pytest.mark.usefixtures("setup")
class TestHomeSearch(TestBase):

    @pytest.mark.Critical
    @pytest.mark.incremental
    def test_search_for_featured(self):

        #TODO remote webdriver
        home = hubHome(self.driver)
        home.open()
        home.searchInSearchBar("people")

        current_url = home.browser.current_url
        Logging.Logger().logger.info(current_url)
        assert current_url.split("/")[3] == "search?q=people1", "test failed" + current_url
        home.browser.find_element_by_link_text("People Central")

        Logging.Logger().logger.info("search people and find people central")

        home.browser.save_screenshot('./report/' + "ss" + '.png')


    @pytest.mark.Minor
    @pytest.mark.Low
    @pytest.mark.incremental
    @pytest.mark.Xfail()
    def test_search_for_featured_1(self):

        home = hubHome(self.driver)
        home.open()
        home.searchInSearchBar("people")

        current_url = home.browser.current_url
        Logging.Logger().logger.info(current_url)
        assert current_url.split("/")[3] == "search?q=people", "test failed" + current_url
        home.browser.find_element_by_link_text("People Central")

        Logging.Logger().logger.info("search people and find people central")


    @pytest.mark.skip(reason="it is a example of skip a test")
    def test_skip_annoucement(self):

        home = hubHome(self.driver)
        home.open()
        home.searchInSearchBar("people")

        current_url = home.browser.current_url
        Logging.Logger().logger.info(current_url)
        assert current_url.split("/")[3] == "search?q=people", "test failed" + current_url
        home.browser.find_element_by_link_text("People Central")

        Logging.Logger().logger.info("search people and find people central")


if __name__ == '__main__':
    pytest.main(['tests/test_home_search.py'])