from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

print('input your http or https')
link = input()

math_form = lambda x: str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    if price:
        browser.find_element(By.ID, 'book').click()

    text_x = browser.find_element(By.ID, 'input_value').text

    input_result = browser.find_element(By.ID, 'answer')
    input_result.send_keys(math_form(text_x))

    submit = browser.find_element(By.ID, 'solve')
    submit.click()

except Exception as error:
    print(error)

finally:
    time.sleep(10)
    browser.quit()
