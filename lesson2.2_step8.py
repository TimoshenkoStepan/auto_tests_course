from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from os import path


print('input your http or https')
link = input()

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.NAME, 'firstname')
    name.send_keys('name')

    lastname = browser.find_element(By.NAME, 'lastname')
    lastname.send_keys('lastname')

    email = browser.find_element(By.NAME, 'email')
    email.send_keys('email@mail.ru')

    current_dir = path.abspath(path.dirname(__file__))
    file_path = path.join(current_dir, 'test.txt')

    for_file = browser.find_element(By.ID, 'file')
    for_file.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

except Exception as error:
    print(error)

finally:
    time.sleep(10)
    browser.quit()
