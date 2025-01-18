import pytest
from playwright.async_api import Page


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Specify language: en")


@pytest.fixture()
def page(context, playwright):
    page: Page = context.new_page()
    page.set_viewport_size({'height': 1000, 'width': 1920})
    playwright.selectors.set_test_id_attribute("data-test")
    yield page


@pytest.fixture
def language(request):
    return request.config.getoption("language")
