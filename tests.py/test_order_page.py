import allure
import pytest
from pages.main_page_pages import MainPageScooter
from pages.question_page_pages import QuestionPageScooter
from pages.order_page_pages import OrderPageScooter
from utils import get_random_phone_number, get_current_date, get_next_date


@pytest.mark.usefixtures("driver")
class TestOrderButtonQuestionPage:
    @allure.title(
        'Проверка оформления заказа через кнопку "Заказать" на главной странице: с текущей датой')
    @allure.description(
        'На странице найти и нажать кнопку "Заказать", заполнить весь флоу позитивного сценария и проверить, что "Заказ оформлен"')


    def test_order_button_question_page_current_date_positive(self, driver):
        click_button_order = QuestionPageScooter(driver)
        click_button_order.question_page()
        click_button_order.scroll_button_order()
        click_button_order.click_button_order()
        new_order = OrderPageScooter(driver)
        new_order.filling_form_one(
            name='Алёна',
            surname='Везденёва',
            address='Лучников пр., 12',
            station='Черкизовская',
            number=get_random_phone_number())
        new_order.wait_for_form_two()
        new_order.filling_form_about_rent_one_flow(
            date=get_current_date(),
            comment='Калитка закрыта, звоните на телефон')
        new_order.wait_for_form_three()
        new_order.click_confirmation_order()
        new_order_title = new_order.get_new_order_title()
        new_order.wait_for_window_order_is_placed()
        assert new_order_title == 'Заказ оформлен'

    @allure.title(
        'Проверка оформления заказа через кнопку "Заказать" на главной странице: со следующей датой')
    @allure.description(
        'На странице найти и нажать кнопку "Заказать", заполнить весь флоу позитивного сценария и проверить, что "Заказ оформлен"')
    def test_order_button_question_page_next_date_positive(self, driver):
        click_button_order = QuestionPageScooter(driver)
        click_button_order.question_page()
        click_button_order.scroll_button_order()
        click_button_order.click_button_order()
        new_order = OrderPageScooter(driver)
        new_order.filling_form_one(
            name='Алёна',
            surname='Везденёва',
            address='Лучников пр., 12',
            station='Черкизовская',
            number=get_random_phone_number())
        new_order.wait_for_form_two()
        new_order.filling_form_about_rent_two_flow(
            date=get_next_date(),
            comment='Калитка закрыта, звоните на телефон')
        new_order.wait_for_form_three()
        new_order.click_confirmation_order()
        new_order_title = new_order.get_new_order_title()
        new_order.wait_for_window_order_is_placed()
        assert new_order_title == 'Заказ оформлен'


@pytest.mark.usefixtures("driver")
class TestOrderButtonMainPage:
    @allure.title(
        'Проверка оформления заказа через кнопку "Заказать" в header: со текущей датой')
    @allure.description(
        'В header найти и нажать кнопку "Заказать", заполнить весь флоу позитивного сценария и проверить, что "Заказ оформлен"')
    def test_order_button_main_page_current_date_user_flow_positive(self, driver):
        open_question_page = QuestionPageScooter(driver)
        open_question_page.question_page()
        click_button_order = MainPageScooter(driver)
        click_button_order.click_button_order_header()
        new_order = OrderPageScooter(driver)
        new_order.filling_form_one(
            name='Алёна',
            surname='Везденёва',
            address='Лучников пр., 12',
            station='Черкизовская',
            number=get_random_phone_number())
        new_order.wait_for_form_two()
        new_order.filling_form_about_rent_one_flow(
            date=get_current_date(),
            comment='Калитка закрыта, звоните на телефон')
        new_order.wait_for_form_three()
        new_order.click_confirmation_order()
        new_order_title = new_order.get_new_order_title()
        new_order.wait_for_window_order_is_placed()
        assert new_order_title == 'Заказ оформлен'


    @allure.title(
        'Проверка оформления заказа через кнопку "Заказать" в header: со следующей датой')
    @allure.description(
        'В заголовке найти и нажать кнопку "Заказать", заполнить весь флоу позитивного сценария и проверить, что "Заказ оформлен"')
    def test_order_button_main_page_next_date_user_flow_positive(self, driver):
        open_question_page = QuestionPageScooter(driver)
        open_question_page.question_page()
        click_button_order = MainPageScooter(driver)
        click_button_order.click_button_order_header()
        new_order = OrderPageScooter(driver)
        new_order.filling_form_one(
            name='Алёна',
            surname='Везденёва',
            address='Лучников пр., 12',
            station='Черкизовская',
            number=get_random_phone_number())
        new_order.wait_for_form_two()
        new_order.filling_form_about_rent_two_flow(
            date=get_next_date(),
            comment='Калитка закрыта, звоните на телефон')
        new_order.wait_for_form_three()
        new_order.click_confirmation_order()
        new_order_title = new_order.get_new_order_title()
        new_order.wait_for_window_order_is_placed()
        assert new_order_title == 'Заказ оформлен'