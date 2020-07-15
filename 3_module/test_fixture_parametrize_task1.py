import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

# smart-hints__feedback hints__component hints__component_showed ember-view


@pytest.mark.parametrize('number_case', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905", ])
class TestStepikStep():

    def test_Stepik_Step_Function(self, browser, number_case):
        link = f"https://stepik.org/lesson/{number_case}/step/1"
        browser.get(link)
        input_response = browser.find_element_by_css_selector(
            "[placeholder='Напишите ваш ответ здесь...']")
        answer = math.log(int(time.time()))

        input_response.send_keys(str(answer))
        button_response = browser.find_element_by_css_selector(
            ".submit-submission")
        button_response.click()
        text_zone = browser.find_element_by_class_name("smart-hints__feedback")
        response_text = text_zone.text
        assert response_text == "Correct!"
