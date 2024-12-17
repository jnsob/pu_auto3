import time

from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, browser):
        self.browser = browser

    def check_title_is(self, title):
        time.sleep(2)
        element_2 = self.browser.find_element(By.XPATH, "//h2[@class='name']")
        assert element_2.text == title
