from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


print('input your http or https')
link = input()

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)

    dropdown = Select(browser.find_element(By.ID, 'dropdown'))
    dropdown.select_by_value(str(num1 + num2))

    submit = browser.find_element(By.CLASS_NAME, 'btn')
    submit.click()

except Exception as error:
    print(error)

finally:
    time.sleep(10)
    browser.quit()
