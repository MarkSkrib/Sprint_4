import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=Service("\driver\geckodriver.exe"))
    driver.get("https://qa-scooter.praktikum-services.ru/")
    
    yield driver

    driver.quit()