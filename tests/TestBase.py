# encoding=utf-8
from util import Logging
from pages.homePage import homePage as hubHome
import pytest


@pytest.fixture(scope="function")
def beforeEach():
    Logging.Logger().logger.info('\n==== before each()')

    yield "beforeEach"
    # after each
    Logging.Logger().logger.info('\n==== after each()')

@pytest.fixture(scope="session")
def beforeAll():
    Logging.Logger().logger.info('\n== before All()')

    yield "beforeAll"
    # after all
    Logging.Logger().logger.info('\n== after all()')



class TestBase:
    pass
