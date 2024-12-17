import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture()
def browser():
    chrome_options = webdriver.ChromeOptions()
    service = Service(executable_path=ChromeDriverManager().install())

    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(
                            service=service,
                              options=chrome_options
                              )
    # wait = WebDriverWait(browser, 15, poll_frequency=1)

    yield browser
    browser.close()
