from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ждём, пока прогрузится элемент")
    def wait_element(self, xpath):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((xpath)))
    
    @allure.step("Нажимаем на кнопку 'Принять куки'")
    def accept_cookie(self, btn_xpath):
        self.driver.find_element(*btn_xpath).click()

    @allure.step(f"Вводим значения в поле")
    def send_key(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)
    
    @allure.step(f"Кликаем по элементу")
    def click_to_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Прокручиваем вниз до вопроса")
    def scroll_to_questions(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")