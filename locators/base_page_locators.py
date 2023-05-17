from selenium.webdriver.common.by import By

class BaseLocators:
    MAIN_PAGE = By.XPATH, "//div[starts-with(text(), 'Самокат')]"
    YANDEX_SEARCH_BLOCK = [By.XPATH, "//iframe[@class='dzen-search-arrow-common__frame']"]
    