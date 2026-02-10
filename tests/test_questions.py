import allure
import pytest
from pages.main_page import MainPage
from constants import Constants

class TestImportantQuestions:

    @allure.step('Тест текстов ответов на вопросы о важном на главной странице сервиса')
    @pytest.mark.parametrize("index, expected_text", Constants.ANSWERS_TEXT)
    def test_question_answer(self,driver, index, expected_text):
        page = MainPage(driver)
        page.click_question(index)
        assert expected_text in page.get_answer_text(index)
