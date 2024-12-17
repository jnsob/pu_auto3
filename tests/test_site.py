from selenium.webdriver.common.by import By


def test_open_s6(driver):
    driver.get("https://www.demoblaze.com/")

    element = driver.find_element(By.XPATH, "//a[text()='Samsung galaxy s6']")
    element.click()
    element_2 = driver.find_element(By.XPATH, "//h2[@class='name']")
    assert element_2.text == "Samsung galaxy s6"
