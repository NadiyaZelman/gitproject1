from week7.steps.webdriver_functions import *
from selenium.webdriver.support.select import Select


sign_in_link = "//a[@class='login']"
email_input = "//input[@id='email_create']"
create_an_account_button = "//form[@id='create-account_form']//span[1]"
password_input = "//input[@id='passwd']"
title_input = "//input[@id='id_gender2']"
first_name_button ="//input[@id='customer_firstname']"
last_name_button ="//input[@id='customer_lastname']"
date_of_birth_day = "//select[@id='days']"
date_of_birth_month = "//select[@id='months']"
date_of_birth_year = "//select[@id='years']"
address_input = "//input[@id='address1']"
city_input = "//input[@id='city']"
zip_code_input = "//input[@id='postcode']"
phone_input = "//input[@id='phone_mobile']"
register_input = "//span[contains(text(),'Register')]"
sign_out_link = "//a[@class='logout']"

#Scenario 1
# 1. Open automationpractice.com website
# 2. Enter email to create a new account
# 3. Click on "Create an account"

launch_website("http://automationpractice.com/index.php")

click_element_by_xpath(sign_in_link)
enter_text_by_xpath(email_input, "1724@email.com")
click_element_by_xpath(create_an_account_button)
time.sleep(5)

# Scenario 2
# 1. Find all elements (xpathe, id, name)
# 2. Input/select all required fields (your personal information)
# 3. Click "register" button.

click_element_by_xpath(title_input)
time.sleep(2)
enter_text_by_xpath(first_name_button, "Nadia")
time.sleep(2)
enter_text_by_xpath(last_name_button, "Z")
time.sleep(2)
enter_text_by_xpath(password_input, "Nadia3!")
time.sleep(2)

dd_days = Select(driver.find_element_by_id("days"))
dd_days.select_by_value('3')
time.sleep(2)

dd_months = Select(driver.find_element_by_id("months"))
dd_months.select_by_value('10')
time.sleep(2)

dd_years = Select(driver.find_element_by_id("years"))
dd_years.select_by_value('1983')
time.sleep(2)

enter_text_by_xpath(address_input, "189 Bay 23 St")
enter_text_by_xpath(city_input, "Brooklyn")
time.sleep(2)

select = Select(driver.find_element_by_id("id_state"))
select.select_by_visible_text('New York')

enter_text_by_xpath(zip_code_input, "11214")
time.sleep(2)

enter_text_by_xpath(phone_input, "1234567890")
click_element_by_xpath(register_input)
time.sleep(5)

# Scenario 3
# 1. Verify that account is created by message
# 2. Log out
# 3. Close the browser

heading_xpath = "//span[contains(text(),'Nadia Z')]"
element = driver.find_element_by_xpath(heading_xpath)
assert "Nadia Z" in element.text
print("Your account is successfully created.")

click_element_by_xpath(sign_out_link)
print("Logging out now...")

close_browser()


