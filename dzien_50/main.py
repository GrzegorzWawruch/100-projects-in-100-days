from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/pl")

#allow_cookies
allow_cookies_button = driver.find_element(By.XPATH, value = "//*[@id='q-22769943']/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div")
allow_cookies_button.click()

#sign-in button
time.sleep(2)
sign_in_button = driver.find_element(By.XPATH, value="//*[@id='q-22769943']/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div")
sign_in_button.click()

#phone number button
phone_nuber_button = driver.find_element(By.XPATH, value="//*[@id='q-1751151019']/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button/div[2]/div[2]/div[2]/div/div")
phone_nuber_button.click()

#user_phone_number
user_phone_number = input("Enter your phone number: ")

#phone_number_text_boc
phone_number_text_box = driver.find_element(By.ID, value="phone_number")
phone_number_text_box.send_keys(user_phone_number)

#next_button_1
next_button =driver.find_element(By.XPATH, value="//*[@id='q-1751151019']/div/div/div[1]/div/div[3]/button/div[2]/div[2]")
next_button.click()

#enter_code_from_sms
code_from_sms = input("Enter code from SMS: ")
code_list = list(code_from_sms)
code_elements = driver.find_elements(By.CLASS_NAME, "D(f).Jc(se)--ml.Jc(c).Py(20px)")
for code_element, code in zip(code_elements, code_list):
    code_element.send_keys(code)

#next_button_2
next_button_2 = driver.find_element(By.XPATH, value="//*[@id='q-1751151019']/div/div/div[1]/div/div[4]/button/div[2]/div[2]/div")
next_button_2.click()

#swipe
while True:
    try:
        #when we get match
        back_to_swipe = driver.find_element(By.XPATH, value="I didn't get matxh so i can't paste here path to object")
        back_to_swipe.click()
    except:
        try:
            #when we swpie
            swipe_right = driver.find_element(By.XPATH, value="//*[@id='main-content']/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[4]/button/span/span[1]/svg/g/path")
            swipe_right.click()
        except:
            break

