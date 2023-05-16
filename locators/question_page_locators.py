from selenium.webdriver.common.by import By

class QuestionPageLocators:
    questions = [By.XPATH, f"//div[@class='accordion__heading']"]
    question_buttons = [By.XPATH, f"//div[@class='accordion__button']"]
    question_answers = [By.XPATH, f"//div[@class='accordion__panel']"]
    answers = [By.XPATH, "//div[starts-with(@id,'accordion__panel-')]/p"]