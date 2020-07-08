from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import os
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    browser = webdriver.Chrome()
    # browser.implicitly_wait(5)
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    btn_book = browser.find_element_by_id("book")
    btn_book.click()

    # alert = browser.switch_to.alert
    # alert.accept()

    x = browser.find_element_by_id("input_value").text
    print(x)
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()

# def calc(x):
# return str(math.log(abs(12*math.sin(int(x)))))

# x = browser.find_element_by_id("input_value").text
# print(x)
# y = calc(x)
# input1 = browser.find_element_by_id("answer")
# input1.send_keys(y)

# alert = browser.switch_to.alert
# alert.accept()

# browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/file_input.html"
# browser.get(link)

# enterFirst = browser.find_element_by_css_selector("[name='firstname']")
# enterFirst.send_keys('Никита')

# current_dir = os.path.abspath(os.path.dirname(__file__))
# filepath = os.path.join(current_dir, 'test.txt')
# fileUpload = browser.find_element_by_css_selector("[type='file']")
# fileUpload.send_keys(filepath)

# button = browser.find_element_by_tag_name("button")
# button.click()

# new_window = browser.window_handles[1]
# browser.switch_to.window(new_window)


finally:

    time.sleep(5)
    browser.quit()
