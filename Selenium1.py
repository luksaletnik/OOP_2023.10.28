from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def make_screenshot(driver):
    today = datetime.datetime.today()
    short_date = today.strftime('_stamp%H%M%S')
    screen_name = 'C:\\Users\\luksa\\PycharmProjects\\selenium_2023.10.28\\screen_shots\\' + 'screen' + short_date + '.png'
    driver.get_screenshot_as_file(screen_name)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')

    try:
        username_field = driver.find_element('id', 'user-name')
    except NoSuchElementException:
        print('nie znaleziono pola "user-name" po ID. Szukam po nazwie ')
        username_field = driver.find_element('name', 'user-name')
        make_screenshot(driver)

    username_field.clear()
    username_field.send_keys('standard_user')

    #driver.find_element('id', 'user-name').send_keys('standard_user')

    try:
        password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    except NoSuchElementException:
        print('Nie znaleziono pola z haslem')
        driver.quit()
        raise
    password_field.clear()
    password_field.send_keys('secret_sauce')
    login_button = driver.find_element('name', 'login-button')
    if not login_button.get_attribute('disable'):
        login_button.click()
    else:
        print('przycisk nieaktywny')
    time.sleep(2)
    make_screenshot(driver)
    driver.quit()