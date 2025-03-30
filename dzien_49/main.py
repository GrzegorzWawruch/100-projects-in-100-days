from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()
LINKEDIN_EMAIL = os.environ['LINKEDIN_EMAIL']
LINKEDIN_PASSWORD = os.environ['LINKEDIN_PASSWORD']

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")


sign_in_button_1 = driver.find_element(By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in_button_1.click()
time.sleep(1)
email_box = driver.find_element(By.ID, "base-sign-in-modal_session_key")
email_box.send_keys(LINKEDIN_EMAIL)
password_box = driver.find_element(By.ID, "base-sign-in-modal_session_password")
password_box.send_keys(LINKEDIN_PASSWORD)
sign_in_button_2 = driver.find_element(By.XPATH, "//*[@id='base-sign-in-modal']/div/section/div/div/form/div[2]/button")
sign_in_button_2.click()

