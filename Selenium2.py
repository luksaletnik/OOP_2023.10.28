from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as excon
from Selenium1 import make_screenshot


def wait_for_id(id_element):
    timeout = 5
    timeout_message = f'Element with id {id_element} did not appear within {timeout} seconds'
    localizator = (By.ID, id_element)
    found = excon.visibility_of_element_located(localizator)  # sprawdzamy, czy element widoczny
    waiter = WebDriverWait(driver, timeout)  # jak dlugo czekac i gdzie
    return waiter.until(found, timeout_message)  # zwrotka


driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com')

# login_button = driver.find_element(By.ID, 'login-button')

try:
    login_button = wait_for_id('login-button')
except:
    print('Not found')
    raise
else:
    print('Found')
finally:
    print('End of test')
    make_screenshot(driver)
    driver.quit()
