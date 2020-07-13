from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
    element1 = browser.find_element_by_css_selector(
        "input.first[placeholder='Input your first name']")
    element1.send_keys("Мой ответ1")
    element2 = browser.find_element_by_css_selector(
        "input.second[placeholder='Input your last name']")
    element2.send_keys("Мой ответ2")
    element3 = browser.find_element_by_css_selector(
        "input.third[placeholder='Input your email']")
    element3.send_keys("Мой ответ3")
    # for element in elements:
    #     element.send_keys("Мой ответ")
    # time.sleep(5)
    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
