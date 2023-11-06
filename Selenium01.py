from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com')
time.sleep(1)
print('Strona:', driver.title)

button1_accept = driver.find_element('id', 'L2AGLb')
button1_accept.click()
#button1_accept = driver.find_element('id', 'L2AGLb').click() #tj. powyzej, tylko w jednej linii

search_field = driver.find_element('name', 'q')
search_field.send_keys('Jaki jest koszt bitcoin?')
time.sleep(1)

# search_button = driver.find_element('name', 'btnK')
# search_button.submit()
search_field.send_keys(Keys.ENTER)
time.sleep(1)

driver.get_screenshot_as_file('zrzut_ekranu.png')

#time.sleep(1)
driver.quit()
