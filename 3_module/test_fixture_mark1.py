import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.skip
    # марка для пропуска данного теста
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.xfail
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")


# для запуска по маркировке использовать такую конструкцию  pytest -s -v -m smoke test_fixture_mark1.py
# для запуска кроме какой либо марки использовать инверсию pytest -s -v -m "not smoke" test_fixture_mark1.py
# Для запуска тестов с разными метками можно использовать логическое ИЛИ.   pytest -s -v -m "smoke or regression" test_fixture_mark1.py
# Для запуска тестов с разными метками можно использовать логическое И.   pytest -s -v -m "smoke and regression" test_fixture_mark1.py
