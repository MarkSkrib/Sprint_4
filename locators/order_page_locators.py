from selenium.webdriver.common.by import By

class OrderPageLocators:
    scooter_logo = [By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"]
    yandex_logo = [By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']"]
    order_page = [By.XPATH, "//div[@class='Order_Header__BZXOb']"]
    header_order_button = [By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[@class='Button_Button__ra12g']"]
    footer_order_button = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    name_field = [By.XPATH, "//div[text()='Введите корректное имя']/preceding-sibling::input"]
    second_name_field = [By.XPATH, "//div[text()='Введите корректную фамилию']/preceding-sibling::input"]
    address_field = [By.XPATH, "//div[text()='Введите корректный адрес']/preceding-sibling::input"]
    select_metro_field = [By.XPATH, "//input[@class='select-search__input']"]
    phone_field = [By.XPATH, "//div[text()='Введите корректный номер']/preceding-sibling::input"]

    cookie_button = [By.XPATH, "//button[@class='App_CookieButton__3cvqF']"]
    next_button = [By.XPATH, "//div[@class='Order_NextButton__1_rCA']/button"]

    date_field = [By.XPATH, "//div[@class='react-datepicker__input-container']/input"]
    dropdown_input = [By.XPATH, "//div[@class='Dropdown-control']"]
    dropdown_items = [By.XPATH, "//div[@class='Dropdown-option']"]

    scooter_colors = [By.XPATH, "//label[@class='Checkbox_Label__3wxSf']"]
    comment_field = [By.XPATH, "//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']"]

    order_button = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    confirm_modal = [By.XPATH, "//div[starts-with(text(), 'Хотите')]"]
    confirm_button = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']"]
    order_success_title = [By.XPATH, "//div[starts-with(text(), 'Заказ')]"]
    order_success_modal = [By.XPATH, "//div[contains(text(), 'Номер заказа')]"]