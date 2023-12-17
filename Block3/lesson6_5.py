import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
from os import environ


links = [
"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"
]

@pytest.mark.parametrize('pytest', links)
def test_login_and_answer(browser, pytest):
    browser.get(pytest)

    browser.find_element(By.CLASS_NAME, "navbar__auth_login ").click()
    browser.find_element(By.ID, "id_login_email").send_keys(environ.get('EMAIL'))
    browser.find_element(By.ID, "id_login_password").send_keys(environ.get('PASSWORD'))
    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()

    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "navbar__auth_login "))
    )

    answer = math.log(int(time.time()))
    browser.find_element(By.CLASS_NAME, 'ember-text-area').send_keys(answer)
    button = browser.find_element(By.CLASS_NAME, "submit-submission")
    button.click()

    result = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert result == "Correct!", f'result is {result} not "Correct!"'


