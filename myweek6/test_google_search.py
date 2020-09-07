##Google search SCENARIO:
# 1. Open the browser, launch the website


import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  #
# or specify the path: driver = webdriver.Chrome('/path/to/chromedriver')
driver.get("https://google.com")
print("opened the browser and google website")
time.sleep(3)

search_text_box = driver.find_element_by_name("q")
print("identified google search box")
time.sleep(3)

search_text_box.clear()
search_text_box.send_keys("python selenium")
print("cleared the search box then typed 'python selenium' words in it")
time.sleep(3)


search_text_box.send_keys(Keys.RETURN)
print("hit the enter button")
time.sleep(3)

result_msg = driver.find_element_by_xpath("//div[@id='result-stats']").text
print(result_msg)

print("now closing the browser...")

