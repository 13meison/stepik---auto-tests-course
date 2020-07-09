from selenium import webdriver
import os
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    # alert = browser.switch_to.alert
    # alert.accept()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text
    print(x)
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_tag_name("button")
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


finally:

    time.sleep(10)
    browser.quit()
