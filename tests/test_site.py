from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.product import ProductPage


def test_open_s6(browser):
    home_page = HomePage(browser)
    home_page.open()
    home_page.click()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')
