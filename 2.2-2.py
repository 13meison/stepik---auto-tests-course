from selenium import webdriver
import time
import math


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    num_1 = browser.find_element_by_id("num1").text
    num_2 = browser.find_element_by_id("num2").text

    sum3 = int(num_1) + int(num_2)
    sum3 = str(sum3)

    li_select = browser.find_element_by_id("dropdown")
    li_select.click()
    print("[value='"+sum3+"']")
    option_select = browser.find_element_by_css_selector("[value='"+sum3+"']")
    option_select.click()
    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()


finally:

    time.sleep(10)
    browser.quit()
