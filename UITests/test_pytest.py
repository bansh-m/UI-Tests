from search_page import SearchHelper
from consts import *


def test_rozklad(browser):
    page = SearchHelper(browser)
    page.go_to_site()
    page.enter_group(GROUP)
    response = page.read_response()
    assert response == EXPECTED_RESULT

def test_session(browser):
    page = SearchHelper(browser)
    page.go_to_site()
    page.go_to_session()
    page.enter_group(GROUP)
    response = page.read_session_response()
    assert response == EXPECTED_SESSION_RESULT
