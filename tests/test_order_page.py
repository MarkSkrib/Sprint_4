from pages.order_page import PageOrder
import allure
import pytest

class TestOrderPage:

    @allure.title("Оформления заказа с помощью кнопки 'Заказать' в шапке сайта")
    @allure.description("Проверка оформления заказа с помощью кнопки 'Заказать' в шапке сайта")
    @pytest.mark.parametrize(
        'name, second_name, address, metro, phone, order_date, term, color, comment',
        [
            ["Вася", "Шукшин", "Фрунзенская 4", "Сокольники", "+79671112233", "15.05.2023", 1, "black", "Позвоните как будете у порога"],
            ["Иван", "Иванов", "Набережная 48", "Лубянка", "+79699581515", "19.06.2023", 1, "grey", "Незабудьте мне позвонить"],
            
        ]
    )
    def test_header_scooter_order(self, driver, name, second_name, address, metro, phone, order_date, term, color, comment):
        order_page = PageOrder(driver)
        order_page.wait_main_page_loaded()
        order_page.click_cookie_button()
        order_page.click_header_order_button()
        order_page.wait_order_page_loaded()
        order_page.set_customer_info(name, second_name, address, metro, phone)
        order_page.set_order_info(order_date, term, color, comment)
        order_page.click_confirm_button()
        assert order_page.get_success_text() == "Заказ оформлен", f"Ошибка. Должно быть написано: 'Заказ оформлен'"


    @allure.title("Оформления заказа с помощью кнопки 'Заказать' внизу сайта")
    @allure.description("Проверка оформления заказа с помощью кнопки 'Заказать' внизу сайта")
    @pytest.mark.parametrize(
        'name, second_name, address, metro, phone, order_date, term, color, comment',
        [
            ["Вася", "Шукшин", "Фрунзенская 4", "Сокольники", "+79671112233", "15.05.2023", 1, "black", "Позвоните как будете у порога"],
            ["Иван", "Иванов", "Набережная 48", "Лубянка", "+79699581515", "19.06.2023", 1, "grey", "Незабудьте мне позвонить"],
            
        ]
    )
    def test_footer_scooter_order(self, driver, name, second_name, address, metro, phone, order_date, term, color, comment):
        order_page = PageOrder(driver)
        order_page.wait_main_page_loaded()
        order_page.click_cookie_button()
        order_page.click_footer_order_button()
        order_page.wait_order_page_loaded()
        order_page.set_customer_info(name, second_name, address, metro, phone)
        order_page.set_order_info(order_date, term, color, comment)
        order_page.click_confirm_button()

        assert order_page.get_success_text() == "Заказ оформлен", f"Ошибка. Должно быть написано: 'Заказ оформлен'"
