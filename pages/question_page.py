from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BaseLocators
from locators.question_page_locators import QuestionPageLocators
import allure


class QuestionPage:    

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ждём, пока прогрузится страница Яндекс.Самоката")
    def wait_question_page_loaded(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((BaseLocators.MAIN_PAGE)))

    @allure.step("Ждём, пока вопросы будут видны")
    def wait_question_is_visible(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((QuestionPageLocators.questions)))

    @allure.step("Ждём, пока ответы будут видны")
    def wait_answer_is_visible(self, num):
        answer_elem = [By.XPATH, f"//div[@id='accordion__panel-{num}']/p"]
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((answer_elem)))

    @allure.step("Нажимаем на вопрос")
    def click_accordion(self, num):
        self.driver.find_elements(*QuestionPageLocators.question_buttons)[num].click()

    @allure.step("Получаем ответ")
    def get_answer(self, num):
        return self.driver.find_elements(*QuestionPageLocators.question_answers)[num].text

    @allure.step("Прокручиваем вниз до вопроса")
    def scroll_to_question(self, num):
        question = self.driver.find_elements(*QuestionPageLocators.question_buttons)[num]
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", question)
    
