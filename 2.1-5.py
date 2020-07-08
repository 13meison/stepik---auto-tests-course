from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    cod = browser.find_element_by_id("treasure")
    x = cod.get_attribute("valuex")
    print(x)
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    check = browser.find_element_by_id("robotCheckbox")
    check.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()


finally:

    time.sleep(10)
    browser.quit()
