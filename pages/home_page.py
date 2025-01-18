import re
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.home_page import HomePageLocators


class HomePage(BasePage):
    def __init__(self, *args, **kwargs):
        super(HomePage, self).__init__(*args, **kwargs)
        self.url = self.domain + self.lang + "/"

    def set_flight_type(self, flight_type):
        self.page.get_by_test_id(HomePageLocators.FLIGHT_TYPE_RETURN).click()
        self.page.get_by_text(flight_type, exact=True).click()

    def set_flight_class_type(self, class_type):
        pass

    def set_number_of_passengers(self, adults=0, children=0, infants=0):
        pass

    def set_number_of_bags(self, cabin_bags=0, baggage=0):
        pass

    def clear_departure_airport(self):
        close_link = self.check_element_exists_by_selector(HomePageLocators.DEPARTURE_AIRPORT_CLOSE)
        if close_link is not False:
            close_link.click()

    def set_departure_airport(self, departure_short, departure_long):
        self.page.locator(HomePageLocators.DEPARTURE_AIRPORT_INPUT).fill(departure_short)
        self.page.get_by_text(departure_long, exact=True).click()

    def set_arrival_airport(self, arrival_short, arrival_long):
        self.page.locator(HomePageLocators.ARRIVAL_AIRPORT_INPUT).fill(arrival_short)
        self.page.get_by_text(arrival_long, exact=True).click()

    def set_departure_time(self, start_date, end_date):
        self.page.get_by_test_id(HomePageLocators.DEPARTURE_TIME_INPUT).click()

        start_day = self.page.locator(HomePageLocators.DEPARTURE_DAY_CALENDAR.replace("*date*", start_date))
        start_day.click()

        end_date_locator = HomePageLocators.DEPARTURE_DAY_CALENDAR.replace("*date*", end_date)

        while True:
            source = start_day.get_by_test_id(HomePageLocators.CALENDAR_DAY_DRAG_RIGHT)
            if self.check_element_exists_by_selector(end_date_locator) is not False:
                target = self.page.locator(end_date_locator)
                source.drag_to(target)
                break
            else:
                target = self.page.get_by_test_id(HomePageLocators.CALENDAR_DAY).last
                current_end_day = target.get_attribute("data-value")
                source.drag_to(target)
                self.page.get_by_test_id(HomePageLocators.CALENDAR_NEXT_MONTH_BUTTON).click()

                start_day = self.page.locator(
                    HomePageLocators.DEPARTURE_DAY_CALENDAR.replace("*date*", current_end_day)
                )
        self.page.get_by_test_id(HomePageLocators.SET_DATES_BUTTON).click()

    def uncheck_accommodation_with_booking(self):
        if self.page.is_checked(HomePageLocators.CHECK_WITH_BOOKING) is True:
            self.page.get_by_alt_text("booking.com logo").click()

    def check_accommodation_with_booking(self):
        if self.page.is_checked(HomePageLocators.CHECK_WITH_BOOKING) is False:
            self.page.get_by_alt_text("booking.com logo").click()

    def click_search_button(self):
        self.page.get_by_test_id(HomePageLocators.SEARCH_BUTTON).click()

    def check_result_page_is_opened_no_return(self):
        regex = re.compile(r"/search/results/[\w-]+/[\w-]+/[0-9_-]+/no-return$")
        expect(self.page).to_have_url(regex)
