from pages.question_page import QuestionPage
import allure

class TestQuestionPage:

    @allure.title('Проверка вопроса: Сколько это стоит? И как оплатить?')
    @allure.description("Нажимаем на вопрос 'Сколько это стоит? И как оплатить?' и сравниваем ответ")
    def test_first_question(self, driver):
        question_page = QuestionPage(driver)
        question_page.wait_question_page_loaded()
        question_page.scroll_to_question(0)
        question_page.wait_question_is_visible()
        question_page.click_accordion(0)
        question_page.wait_answer_is_visible(0)
        assert question_page.get_answer(0) == "Сутки — 400 рублей. Оплата курьеру — наличными или картой.", f"Текст отличается. Должно быть: 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'"

    @allure.title('Проверка вопроса: Хочу сразу несколько самокатов! Так можно?')
    @allure.description("Нажимаем на вопрос 'Хочу сразу несколько самокатов! Так можно?' и сравниваем ответ")
    def test_second_question(self, driver):
        question_page = QuestionPage(driver)
        question_page.wait_question_page_loaded()
        question_page.scroll_to_question(1)
        question_page.wait_question_is_visible()
        question_page.click_accordion(1)
        question_page.wait_answer_is_visible(1)
        assert question_page.get_answer(1) == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.", f"Текст отличается. Должно быть:\n'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'"

    @allure.title('Проверка вопроса: Как рассчитывается время аренды?')
    @allure.description("Нажимаем на вопрос 'Как рассчитывается время аренды?' и сравниваем ответ")
    def test_third_question(self, driver):
        question_page = QuestionPage(driver)
        question_page.wait_question_page_loaded()
        question_page.scroll_to_question(2)
        question_page.wait_question_is_visible()
        question_page.click_accordion(2)
        question_page.wait_answer_is_visible(2)
        assert question_page.get_answer(2) == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.", f"Текст отличается. Должно быть:\n'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'"

    @allure.title('Проверка вопроса: Можно ли заказать самокат прямо на сегодня?')
    @allure.description("Нажимаем на вопрос 'Можно ли заказать самокат прямо на сегодня?' и сравниваем ответ")
    def test_fourth_question(self, driver):
        question_page = QuestionPage(driver)
        question_page.wait_question_page_loaded()
        question_page.scroll_to_question(3)
        question_page.wait_question_is_visible()
        question_page.click_accordion(3)
        question_page.wait_answer_is_visible(3)
        assert question_page.get_answer(3) == "Только начиная с завтрашнего дня. Но скоро станем расторопнее.", f"Текст отличается. Должно быть:\n'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'"

    @allure.title('Проверка вопроса: Можно ли продлить заказ или вернуть самокат раньше?')
    @allure.description("Нажимаем на вопрос 'Можно ли продлить заказ или вернуть самокат раньше?' и сравниваем ответ")
    def test_fifth_question(self, driver):
        question_page = QuestionPage(driver)
        question_page.wait_question_page_loaded()
        question_page.scroll_to_question(4)
        question_page.wait_question_is_visible()
        question_page.click_accordion(4)
        question_page.wait_answer_is_visible(4)
        assert question_page.get_answer(4) == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.", f"Текст отличается. Должно быть:\n'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'"

    @allure.title('Проверка вопроса: Вы привозите зарядку вместе с самокатом?')
    @allure.description("Нажимаем на вопрос 'Вы привозите зарядку вместе с самокатом?' и сравниваем ответ")
    def test_six_question(self, driver):
        question_page = QuestionPage(driver)
        question_page.wait_question_page_loaded()
        question_page.scroll_to_question(5)
        question_page.wait_question_is_visible()
        question_page.click_accordion(5)
        question_page.wait_answer_is_visible(5)
        assert question_page.get_answer(5) == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.", f"Текст отличается. Должно быть:\n'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'"

    @allure.title('Проверка вопроса: Можно ли отменить заказ?')
    @allure.description("Нажимаем на вопрос 'Можно ли отменить заказ?' и сравниваем ответ")
    def test_seven_question(self, driver):
        question_page = QuestionPage(driver)
        question_page.wait_question_page_loaded()
        question_page.scroll_to_question(6)
        question_page.wait_question_is_visible()
        question_page.click_accordion(6)
        question_page.wait_answer_is_visible(6)
        assert question_page.get_answer(6) == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.", f"Текст отличается. Должно быть:\n'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'"

    @allure.title('Проверка вопроса: Я живу за МКАДом, привезёте?')
    @allure.description("Нажимаем на вопрос 'Я живу за МКАДом, привезёте?' и сравниваем ответ")
    def test_eight_question(self, driver):
        question_page = QuestionPage(driver)
        question_page.wait_question_page_loaded()
        question_page.scroll_to_question(7)
        question_page.wait_question_is_visible()
        question_page.click_accordion(7)
        question_page.wait_answer_is_visible(7)
        assert question_page.get_answer(7) == "Да, обязательно. Всем самокатов! И Москве, и Московской области.", f"Текст отличается. Должно быть:\n'Да, обязательно. Всем самокатов! И Москве, и Московской области.'"

