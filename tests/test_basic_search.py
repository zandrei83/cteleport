from datetime import date
from datetime import timedelta
from playwright.sync_api import Page
from pages.home_page import HomePage
from locales.home_page import search_data


class TestBasicSearch:
    def test_basic_search_not_logged(self, page: Page, language):

        home_page = HomePage(page, language)
        home_page.open()
        home_page.set_flight_type(search_data[language]["oneway"])
        home_page.clear_departure_airport()
        home_page.set_departure_airport(
            search_data[language]["departure_short_rtm"], search_data[language]["departure_long_rtm"]
        )
        home_page.set_arrival_airport(
            search_data[language]["arrival_short_rtm"], search_data[language]["arrival_long_rtm"]
        )

        # Set start date
        today = date.today()
        # Set end date. Can be any date in the future.
        date_in_future = today + timedelta(days=7)

        home_page.set_departure_time(today.strftime("%Y-%m-%d"), date_in_future.strftime("%Y-%m-%d"))
        home_page.uncheck_accommodation_with_booking()
        home_page.click_search_button()
        home_page.check_result_page_is_opened_no_return()
