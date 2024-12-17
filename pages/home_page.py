import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, browser):
        self.browser = browser
        # self.wait = browser.wait
    def open(self):
        self.browser.get("https://www.demoblaze.com/")

    def click(self):
        time.sleep(1)
        # self.wait.until(EC.visibility_of_element_located(By.XPATH("//a[text()='Samsung galaxy s6']")))
        element = self.browser.find_element(By.XPATH, "//a[text()='Samsung galaxy s6']")
        element.click()
