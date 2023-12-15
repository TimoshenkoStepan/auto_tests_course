import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


def registration(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.get(link)

    name = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    name.send_keys('Name')
    lastname = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    send_keys('Lastname')
    email = browser.find_element(By.CSS_SELECTOR, '.third_class .third')
    email.send_keys('email@mail.ru')

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

class TestUniqueSelectors(unittest.TestCase):
    def test_registration1(self):
        registration('http://suninjuly.github.io/registration1.html')

    def test_registration2(self):
        registration('http://suninjuly.github.io/registration2.html')


if __name__ == "__main__":
    unittest.main()