from locators.base_page import BasePageLocators


class HomePageLocators(BasePageLocators):
    # Test id's

    FLIGHT_TYPE_RETURN = "SearchFormModesPicker-active-return"
    CLASS_TYPE_ECONOMY = "CabinClassField-active-economy"
    DEPARTURE_TIME_INPUT = "SearchDateInput"
    CALENDAR_NEXT_MONTH_BUTTON = "CalendarMoveNextButton"
    CALENDAR_DAY = "CalendarDay"
    CALENDAR_DAY_SELECTED = "DaySelected-selected"
    CALENDAR_DAY_DRAG_RIGHT = "DayDragArrowRight"
    SET_DATES_BUTTON = "SearchFormDoneButton"
    SEARCH_BUTTON = "LandingSearchButton"

    # Selectors

    DEPARTURE_AIRPORT_CLOSE = "//div[@data-test='PlacePickerInputPlace-close']"
    DEPARTURE_AIRPORT_INPUT = "//div[@data-test='PlacePickerInput-origin']/input"
    ARRIVAL_AIRPORT_INPUT = "//div[@data-test='PlacePickerInput-destination']/input"
    DEPARTURE_DAY_CALENDAR = "//div[@data-value='*date*']"
    CHECK_WITH_BOOKING = "//input[@class='-z-default absolute opacity-0']"


