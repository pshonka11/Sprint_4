from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIELD_NAME = By.XPATH, "//input[@placeholder='* Имя']"
    FIELD_SURNAME = By.XPATH, "//input[@placeholder='* Фамилия']"
    FIELD_ADDRESS = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    FIELD_PHONE = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    FIELD_SUBWAY_STATION = By.CLASS_NAME, "select-search__input"
    SCROLLABLE_FIELD_SUBWAY_STATION = By.XPATH, ".//ul[@class='select-search__options']"
    BUTTON_FORWARD = By.XPATH, ".//button [contains(text(), 'Далее')]"
    FORM_TWO = By.XPATH, "//div[contains(text(), 'Про аренду')]"
    FIELD_CALENDAR = By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"
    CALENDAR = By.XPATH, "//div[@class= 'react-datepicker']"
    FIELD_RENTAL_PERIOD = By.CLASS_NAME, 'Dropdown-root'
    MENU_RENTAL_PERIOD = By.CLASS_NAME, 'Dropdown-menu'
    RENTAL_PERIOD_DAY = By.XPATH, "//*[contains(text(),'сутки')]"
    RENTAL_PERIOD_TWO_DAYS = By.XPATH, "//*[contains(text(),'двое суток')]"
    RENTAL_PERIOD_THREE_DAYS = By.XPATH, "//*[contains(text(),'трое суток')]"
    RENTAL_PERIOD_FOUR_DAYS = By.XPATH, "//*[contains(text(),'четверо суток')]"
    RENTAL_PERIOD_FIVE_DAYS = By.XPATH, "//*[contains(text(),'пятеро суток')]"
    RENTAL_PERIOD_SIX_DAYS = By.XPATH, "//*[contains(text(),'шестеро суток')]"
    RENTAL_PERIOD_SEVEN_DAYS = By.XPATH, "//*[contains(text(),'семеро суток')]"
    CHECKBOX_BLACK = By.ID, 'black'
    CHECKBOX_GREY = By.ID, 'grey'
    FIELD_COMMENT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    BUTTON_ORDER = By.XPATH, "//*[contains(@class, 'Button_Button__ra12g Button_Middle')][2]"
    FORM_THREE = By.XPATH, "//*[contains(text(), 'Хотите оформить заказ?')]"
    BUTTON_CONFIRMATION_ORDER = By.XPATH, "//*[contains(text(),'Да')]"
    WINDOW_ORDER_IS_PLACED = By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"
    BUTTON_VIEW_STATUS = By.XPATH, "//button[contains(text(), 'Посмотреть статус')]"
    DATE_PICKER_DAY_SELECTED = By.XPATH, "//*[contains(@class, 'react-datepicker__month-container')]"