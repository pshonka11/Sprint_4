import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.question_page_locators import QuestionPageLocators


class QuestionPageScooter:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу https://qa-scooter.praktikum-services.ru')
    def question_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru')

    def wait_for_question_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be('https://qa-scooter.praktikum-services.ru'))

    def click_cookie_button(self):
        self.driver.find_element(*QuestionPageLocators.BUTTON_COOKIE).click()

    @allure.step('Перейти к разделу "Вопросы о важном"')
    def scroll_to_questions_section(self):
        section = self.driver.find_element(*QuestionPageLocators.QUESTIONS_SECTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", section)

    def wait_for_scroll_to_questions_section(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(QuestionPageLocators.QUESTIONS_SECTION))

    def get_questions(self):
        return self.driver.find_elements(*QuestionPageLocators.QUESTIONS)

    @allure.step('Нажать на вопрос')
    def click_question_button(self, num):
        questions = self.get_questions()
        questions[num - 1].click()

    @allure.step('Получить текст ответа')
    def get_current_answer_text(self):
        return self.driver.find_element(*QuestionPageLocators.CURRENT_ANSWER).text

    def wait_for_to_get_current_answer(self):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(QuestionPageLocators.CURRENT_ANSWER))

    @allure.step('Перейти к кнопке "Заказать"')
    def scroll_button_order(self):
        button = self.driver.find_element(*QuestionPageLocators.BUTTON_ORDER)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(QuestionPageLocators.BUTTON_ORDER))

    @allure.step('Нажать на кнопку "Заказать"')
    def click_button_order(self):
        self.driver.find_element(*QuestionPageLocators.BUTTON_ORDER).click()
