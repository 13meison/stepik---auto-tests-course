from selenium import webdriver
import os
import time

try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    enterFirst = browser.find_element_by_css_selector("[name='firstname']")
    enterFirst.send_keys('Никита')

    enterLast = browser.find_element_by_css_selector("[name='lastname']")
    enterLast.send_keys('Mamaev')

    enterMail = browser.find_element_by_css_selector("[name='email']")
    enterMail.send_keys('13meison@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(current_dir, 'test.txt')
    fileUpload = browser.find_element_by_css_selector("[type='file']")
    fileUpload.send_keys(filepath)

    button = browser.find_element_by_tag_name("button")
    button.click()


finally:

    time.sleep(10)
    browser.quit()
