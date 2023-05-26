import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(1280, 800)
    yield driver
    driver.quit()