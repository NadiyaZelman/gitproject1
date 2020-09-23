from selenium import webdriver
from week7.webdriver_class.webdriver_functions import *

sign_in_link = "//a[@class='login']"
email_input = "//input[@id='email_create']"
create_an_account_button = "//form[@id='create-account_form']//span[1]"
password_input = "//input[@id='passwd']"
title_input = "//input[@id='id_gender2']"
first_name_button ="//input[@id='customer_firstname']"
last_name_button ="//input[@id='customer_lastname']"
date_of_birth_month = "//select[@id='days']"


launch_website("http://automationpractice.com/index.php")
click_element_by_xpath(sign_in_link)
enter_text_by_xpath(email_input, "nz@email.com")
click_element_by_xpath(create_an_account_button)
time.sleep(5)
click_element_by_xpath(title_input)
enter_text_by_xpath(first_name_button, "Nadia")
enter_text_by_xpath(last_name_button, "Z")
enter_text_by_xpath(password_input, "Nadia3!")
click_element_by_xpath(date_of_birth_month)


drop_and_down(date_of_birth_month, "//div[@id='uniform-days']//option[4]")
