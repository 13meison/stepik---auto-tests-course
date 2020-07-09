from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = int(browser.find_element_by_id("input_value").text)
    print(x)

    y = calc(x)

    enter = browser.find_element_by_id("answer")
    enter.send_keys(y)

    browser.execute_script("window.scrollBy(0, 100);")

    checkButton = browser.find_element_by_id("robotCheckbox")
    checkButton.click()

    radioButton = browser.find_element_by_id("robotsRule")
    radioButton.click()

    button = browser.find_element_by_tag_name("button")
    button.click()
    assert True


finally:

    time.sleep(10)
    browser.quit()
