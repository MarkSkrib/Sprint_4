from pages.order_page import PageOrder
from pages.yandex_page import PageYandex
from locators.base_page_locators import BaseLocators
from locators.order_page_locators import OrderPageLocators
import allure

@allure.feature("Проверяет корректный переход по сайтам при клике на логотипы Яндекса и Самоката.")
class TestRedirect:

    @allure.title("Логотип Самоката")
    @allure.description("Проверка, что при клике на логотип Самоката, открывается главная страница Яндекс Самоката")
    def test_scooter_main_page_redirect(self, driver):
        order_page = PageOrder(driver)
        order_page.wait_element(BaseLocators.MAIN_PAGE)
        order_page.click_header_order_button()
        order_page.wait_element(OrderPageLocators.order_page)
        order_page.click_scooter_logo()
        order_page.wait_element(BaseLocators.MAIN_PAGE)
        assert order_page.get_scooter_main_page_text() == "Самокат", "Ошибка. Мы не попали на главную страницу самоката."

    @allure.title("Логотип Яндекса")
    @allure.description("Проверка, что при клике на логотип Яндекса, открывается главная страница Яндекс Самоката")
    def test_yandex_main_page_redirect(self, driver):
        order_page = PageOrder(driver)
        order_page.wait_element(BaseLocators.MAIN_PAGE)
        order_page.click_yandex_logo()
        yandex_page = PageYandex(driver)
        yandex_page.switch_to_new_tab()
        yandex_page.wait_yandex_page_loaded()
        assert yandex_page.get_yandex_search_label() == "Поиск Яндекса", "Ошибка. Мы не попали на главную страницу яндекса."