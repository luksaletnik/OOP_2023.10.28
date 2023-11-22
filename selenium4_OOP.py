from selenium import webdriver
from selenium3_OOP import LoginPage
import time
from Selenium1 import make_screenshot

driver = webdriver.Chrome()
page = LoginPage(driver)
page.open()
page.enter_username('standard_user')
page.enter_password('secret_sauce')
page.click_login()
time.sleep(2)

try:
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', make_screenshot(driver)
except AssertionError:
    print('Błąd, adres url się nie zgadza')
    raise
else:
    print('OK')
finally:
    driver.quit()
