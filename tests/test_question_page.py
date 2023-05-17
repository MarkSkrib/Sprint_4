from pages.question_page import QuestionPage
from data import QuestionPageData
import pytest
import allure

@allure.feature("Проверяет вопросы на главной странице на соответствие ответов.")
class TestQuestionPage:

    @allure.title("Проверка ответов в разделе 'Вопросы о важном'")
    @pytest.mark.parametrize('question_idx', [i for i in range(8)])
    def test_first_question(self, driver, question_idx):
        question_page = QuestionPage(driver)
        question_page.setup_question(question_idx)
        expected_result = QuestionPageData.question_and_answers_dict[question_page.get_question(question_idx)]
        actual_result = question_page.get_answer(question_idx)
        assert actual_result == expected_result, f"Текст отличается. Должно быть: {expected_result}"
        