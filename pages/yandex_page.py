from locators.base_page_locators import BaseLocators
from pages.base_page import BasePage
import allure

class PageYandex(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Переключаемся на новый таб")
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Ждём, пока главная страница Дзен(Яндекс) прогрузится")
    def wait_yandex_page_loaded(self):
        self.wait_element(BaseLocators.YANDEX_SEARCH_BLOCK)
        
    @allure.step("Получаем название поля поиска")
    def get_yandex_search_label(self):
        return self.driver.find_element(*BaseLocators.YANDEX_SEARCH_BLOCK).get_attribute("aria-label")
        