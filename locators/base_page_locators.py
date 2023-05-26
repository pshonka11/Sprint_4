from selenium.webdriver.common.by import By


class BasePageLocators:
    BUTTON_ORDER_HEADER = By.XPATH, "// *[ @class ='Button_Button__ra12g']"
    LOGO_YANDEX = By.CLASS_NAME, "Header_LogoYandex__3TSOI"
    LOGO_SCOOTER = By.CLASS_NAME, "Header_LogoScooter__3lsAR"