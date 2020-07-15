import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
# Фикстура сработает 1 раз для каждого класса (в данном случае браузер откроется, отработают все функции и он закроется)
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('language', ["ru", "en-gb"])
# Добавили параметризацию для функции
@pytest.mark.skip
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")


@pytest.mark.parametrize('language', ["ru", "en-gb"])
# Добавили параметризацию для всего класса
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        # этот тест запустится 2 раза

    def test_guest_should_see_navbar_element(self, browser, language):
        link = "http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        # этот тест запустится 2 раза
