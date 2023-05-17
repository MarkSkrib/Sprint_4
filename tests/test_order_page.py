from pages.order_page import PageOrder
import allure
import pytest
from data import user_1, user_2

@allure.feature("Проверяет оформление заказа через кнопку 'Заказать' в шапке главной страницы и внизу страницы")
class TestOrderPage:

    @allure.title("Оформления заказа с помощью кнопки 'Заказать' в шапке сайта")
    @allure.description("Проверка оформления заказа с помощью кнопки 'Заказать' в шапке сайта")
    @pytest.mark.parametrize('name, second_name, address, metro, phone, order_date, term, color, comment',
                             [pytest.param(user_1.name, user_1.second_name,
                                    user_1.address, user_1.metro,
                                    user_1.phone, user_1.order_date, user_1.term,
                                    user_1.color, user_1.comment),
                              pytest.param(user_2.name, user_2.second_name,
                                    user_2.address, user_2.metro,
                                    user_2.phone, user_2.order_date, user_2.term,
                                    user_2.color, user_2.comment)])
    def test_header_scooter_order(self, driver, name, second_name, address, metro, phone, order_date, term, color, comment):
        order_page = PageOrder(driver)
        order_page.page_initialization()
        order_page.click_header_order_button()
        order_page.set_customer_info(name, second_name, address, metro, phone)
        order_page.set_order_info(order_date, term, color, comment)
        assert order_page.get_success_text() == "Заказ оформлен", f"Ошибка. Должно быть написано: 'Заказ оформлен'"


    @allure.title("Оформления заказа с помощью кнопки 'Заказать' внизу сайта")
    @allure.description("Проверка оформления заказа с помощью кнопки 'Заказать' внизу сайта")
    @pytest.mark.parametrize('name, second_name, address, metro, phone, order_date, term, color, comment',
                             [pytest.param(user_1.name, user_1.second_name,
                                    user_1.address, user_1.metro,
                                    user_1.phone, user_1.order_date, user_1.term,
                                    user_1.color, user_1.comment),
                              pytest.param(user_2.name, user_2.second_name,
                                    user_2.address, user_2.metro,
                                    user_2.phone, user_2.order_date, user_2.term,
                                    user_2.color, user_2.comment)])
    def test_footer_scooter_order(self, driver, name, second_name, address, metro, phone, order_date, term, color, comment):
        order_page = PageOrder(driver)
        order_page.page_initialization()
        order_page.click_footer_order_button()
        order_page.set_customer_info(name, second_name, address, metro, phone)
        order_page.set_order_info(order_date, term, color, comment)

        assert order_page.get_success_text() == "Заказ оформлен", f"Ошибка. Должно быть написано: 'Заказ оформлен'"
