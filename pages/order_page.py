from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BaseLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
import allure

class PageOrder:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ждём, пока прогрузится страница Яндекс.Самоката")
    def wait_main_page_loaded(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((BaseLocators.MAIN_PAGE)))

    @allure.step("Ждём, пока прогрузится страница заказа самоката")
    def wait_order_page_loaded(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((OrderPageLocators.order_page)))

    @allure.step("Нажимаем на кнопку 'Принять куки'")
    def click_cookie_button(self):
        self.driver.find_element(*OrderPageLocators.cookie_button).click()

    @allure.step("Нажимаем на кнопку 'Заказать' в шапке главной страницы")
    def click_header_order_button(self):
        self.driver.find_element(*OrderPageLocators.header_order_button).click()

    @allure.step("Нажимаем на кнопку 'Заказать' внизу главной страницы")
    def click_footer_order_button(self):
        self.driver.find_element(*OrderPageLocators.footer_order_button).click()

    @allure.step("Вводим имя на странице заказа самоката")
    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.name_field).send_keys(name)
    
    @allure.step("Вводим фамилию на странице заказа самоката")
    def set_second_name(self, second_name):
        self.driver.find_element(*OrderPageLocators.second_name_field).send_keys(second_name)
    
    @allure.step("Вводим адрес на странице заказа самоката")
    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.address_field).send_keys(address)
    
    @allure.step("Вводим номер телефона на странице заказа самоката")
    def set_phone(self, phone):
        self.driver.find_element(*OrderPageLocators.phone_field).send_keys(phone)
    
    @allure.step("Выбираем метро на странице заказа самоката")
    def select_metro(self, value):
        metro_value = self.driver.find_element(*OrderPageLocators.select_metro_field)
        metro_value.send_keys(value)
        metro_value.send_keys(Keys.ARROW_DOWN)
        metro_value.send_keys(Keys.RETURN)

    @allure.step("Нажимаем на кнопку 'Далее'")
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.next_button).click()
    
    @allure.step("Вводим дату доставки самоката")
    def set_date_input(self, order_date):
        self.driver.find_element(*OrderPageLocators.date_field).send_keys(order_date)
        self.driver.find_element(*OrderPageLocators.date_field).send_keys(Keys.RETURN)

    @allure.step("Выбираем срок использования самоката")
    def set_day_term(self, term):
        self.driver.find_element(*OrderPageLocators.dropdown_input).click()
        self.driver.find_elements(*OrderPageLocators.dropdown_items)[term].click()

    @allure.step("Выбираем цвет самоката")
    def check_scooter_color(self, color):
        color_checkboxes = self.driver.find_elements(*OrderPageLocators.scooter_colors)
        for chekbox in color_checkboxes:
            if color == chekbox.get_attribute("for"):
                chekbox.click()
                break
    
    @allure.step("Вводим комментарий к заказу")
    def set_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.comment_field).send_keys(comment)

    @allure.step("Нажимаем на кнопку 'Заказать'")
    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.order_button).click()
    
    @allure.step("Нажимаем на кнопку подтверждения 'Да'")
    def click_confirm_button(self):
        self.driver.find_element(*OrderPageLocators.confirm_button).click()

    @allure.step("Получаем текст для сравнения к ожидаемому результату")
    def get_success_text(self):
        return self.driver.find_element(*OrderPageLocators.order_success_title).text.split("\n")[0]
    
    @allure.step("Нажимаем на логотип самоката")
    def click_scooter_logo(self):
        self.driver.find_element(*OrderPageLocators.scooter_logo).click()

    @allure.step("Нажимаем на логотип яндекса")
    def click_yandex_logo(self):
        self.driver.find_element(*OrderPageLocators.yandex_logo).click()

    @allure.step("Получаем текст главной страницы Яндекс.Самоката для сравнения к ожидаемому")
    def get_scooter_main_page_text(self):
        return self.driver.find_element(*BaseLocators.MAIN_PAGE).text.split("\n")[0]
    
    def set_customer_info(self, name, second_name, address, metro, phone):
        self.set_name(name)
        self.set_second_name(second_name)
        self.set_address(address)
        self.select_metro(metro)
        self.set_phone(phone)
        self.click_next_button()
    
    def set_order_info(self, order_date, term, scooter_color, comment):
        self.set_date_input(order_date)
        self.set_day_term(term)
        self.check_scooter_color(scooter_color)    
        self.set_comment(comment)
        self.click_order_button()
