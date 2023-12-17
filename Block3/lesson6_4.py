from selenium.webdriver.common.by import By
from os import environ

link = 'https://stepik.org/lesson/236895/step/1'

def test_login_on_stepik(browser):
    browser.get(link)

    browser.find_element(By.ID, "ember33").click()

    browser.find_element(By.ID, "id_login_email").send_keys(environ.get('EMAIL'))
    browser.find_element(By.ID, "id_login_password").send_keys(environ.get('PASSWORD'))

    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()
