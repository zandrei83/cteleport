from playwright.sync_api import Page
from locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, page: Page, lang="en"):
        self.domain = "https://www.kiwi.com/"
        self.lang = lang
        self.url = None
        self.page = page

    def open(self):
        if self.url is not None:
            self.page.goto(self.url)
            self.accept_cookies()
        else:
            raise Exception("The URL isn't specified!")

    def accept_cookies(self):
        if self.check_element_exists_by_selector(BasePageLocators.COOKIES_POPUP) is not False:
            self.page.get_by_test_id(BasePageLocators.COOKIE_ACCEPT_BUTTON).click()

    def check_element_exists_by_selector(self, selector):
        element = self.page.query_selector(selector)
        return False if element is None else element
