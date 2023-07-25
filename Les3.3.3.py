import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

response = "Congratulations! You have successfully registered!"


def check_page(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    els = browser.find_elements(By.CSS_SELECTOR, ".first_block *")
    for el in els:
        print(el.accessible_name)
    browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Alex")

    browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Ragulin")

    browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("S-Pb")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    return browser.find_element(By.TAG_NAME, "h1").text


class TestCase(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(response, check_page("http://suninjuly.github.io/registration1.html"))

    def test_reg2(self):
        self.assertEqual(response, check_page("http://suninjuly.github.io/registration2.html"))


if __name__ == '__main__':
    unittest.main()
