from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


print('input your http or https')
link = input()

math_form = lambda x: str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    text_x = browser.find_element(By.ID, 'input_value').text

    input_result = browser.find_element(By.ID, 'answer')
    input_result.send_keys(math_form(text_x))

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radiobox = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobox)
    radiobox.click()

    submit = browser.find_element(By.CLASS_NAME, 'btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

except Exception as error:
    print(error)

finally:
    time.sleep(10)
    browser.quit()
