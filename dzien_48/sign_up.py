from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Name")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("LastName")

email_address = driver.find_element(By.NAME, "email")
email_address.send_keys("EMAIL@eXAMPLE.COM")

sign_up_button = driver.find_element(By.XPATH, "/html/body/form/button")
sign_up_button.click()
