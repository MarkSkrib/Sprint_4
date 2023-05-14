from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.order_page import PageOrder
from pages.yandex_page import PageYandex
import time
import allure
import pytest

class TestRedirect:

    @allure.title("Логотип Самоката")
    @allure.description("Проверка, что при клике на логотип Самоката, открывается главная страница Яндекс Самоката")
    def test_scooter_main_page_redirect(self, driver):
        order_page = PageOrder(driver)
        order_page.wait_main_page_loaded()
        order_page.click_header_order_button()
        order_page.click_scooter_logo()
        order_page.wait_main_page_loaded()
        assert order_page.get_scooter_main_page_text() == "Самокат", "Ошибка. Мы не попали на главную страницу самоката."

    @allure.title("Логотип Яндекса")
    @allure.description("Проверка, что при клике на логотип Яндекса, открывается главная страница Яндекс Самоката")
    def test_yandex_main_page_redirect(self, driver):
        order_page = PageOrder(driver)
        order_page.wait_main_page_loaded()
        order_page.click_yandex_logo()
        yandex_page = PageYandex(driver)
        yandex_page.switch_to_new_tab()
        yandex_page.wait_yandex_page_loaded()
        assert yandex_page.get_yandex_search_label() == "Поиск Яндекса", "Ошибка. Мы не попали на главную страницу яндекса."