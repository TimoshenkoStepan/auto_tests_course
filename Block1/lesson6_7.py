from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, 'input')
    for elem in elements:
        elem.send_keys('Suck')

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
finally:
    time.sleep(30)
    browser.quit()