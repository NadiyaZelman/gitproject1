
import time

from selenium import webdriver
driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://letskodeit.teachable.com/p/practice")
time.sleep(3)

buttons = driver.find_elements_by_xpath("//button")
for button in buttons:
    print('text of button:', button.text)

#2 find by link text
open_tab = driver.find_element_by_link_text('Open Tab')
open_tab2 = driver.find_element_by_patrial_link_text('Open Tab')
