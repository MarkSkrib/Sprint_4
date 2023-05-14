from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class PageYandex:

    yandex_search_page = [By.XPATH, "//iframe[@class='dzen-search-arrow-common__frame']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Переключаемся на новый таб")
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Ждём, пока главная страница Дзен(Яндекс) прогрузится")
    def wait_yandex_page_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((self.yandex_search_page)))

    @allure.step("Получаем название поля поиска")
    def get_yandex_search_label(self):
        return self.driver.find_element(*self.yandex_search_page).get_attribute("aria-label")