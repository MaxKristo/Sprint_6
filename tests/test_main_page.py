import allure
import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from conftest import driver

class TestMainPage:

    @allure.title('Проверка вопросов и ответов')
    @allure.description('Кликаем на вопрос, получаем ответ, сравниваем с ожидаемым ответом')
    @pytest.mark.parametrize( 'question_num' , [ 0, 1, 2, 3, 4, 5, 6, 7 ] )
    def test_answer_for_question(self, driver, question_num):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.click_to_question(question_num)
        answer_text = main_page.get_answer_text(question_num)
        assert answer_text == MainPageLocators.ANSWERS[question_num]
