from selenium.webdriver.common.by import By

class OrderPageLocators:
    scooter_logo = [By.XPATH, ".//*[@alt='Scooter']"] # Логотип самоката
    yandex_logo = [By.XPATH, ".//*[@alt='Yandex']"] # Логотип яндекса
    order_page = [By.XPATH, "//div[starts-with(@class, 'Order_Header')]"] # Страница заказа
    header_order_button = [By.XPATH, "//div[starts-with(@class,'Header_Nav')]/button[1]"] # Кнопка "Заказать" на шапке сайта
    footer_order_button = [By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']"] # Кнопка Заказать внизу главной страницы
    name_field = [By.XPATH, ".//input[@placeholder='* Имя']"] # Поле Имя
    second_name_field = [By.XPATH, ".//input[@placeholder='* Фамилия']"] # Поле Фамилия
    address_field = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"] # Поле Адрес
    select_metro_field = [By.XPATH, ".//input[@placeholder='* Станция метро']"] # Поле выбора станции метро
    phone_field = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"] # Поле ввода телефона

    cookie_button = [By.XPATH, ".//button[starts-with(@class,'App_CookieButton') and text()='да все привыкли']"] # Кнопка куки
    next_button = [By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Далее']"] # Кнопка далее

    date_field = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"] # Поле ввода даты
    dropdown_input = [By.XPATH, "//div[text()='* Срок аренды']"] # Поле выбора срока аренды
    dropdown_items = [By.XPATH, "//div[@role='option']"] # Сроки аренды

    scooter_colors = [By.XPATH, "//label[starts-with(@class,'Checkbox_Label')]"] # Цвета самоката
    comment_field = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"] # Поле Комментарий

    order_button = [By.XPATH, "//div[starts-with(@class,'Order_Buttons')]/button[text()='Заказать']"] # Кнопка Заказать 
    confirm_modal = [By.XPATH, "//div[starts-with(text(), 'Хотите')]"] # Окно подтверждения заказа
    confirm_button = [By.XPATH, "//button[text()='Да']"] # Кнопка подтверждения
    order_success_title = [By.XPATH, "//div[starts-with(text(), 'Заказ')]"] # Окно успешно созданного заказа
    order_success_modal = [By.XPATH, "//div[contains(text(), 'Номер заказа')]"] # Текст НОмер заказа