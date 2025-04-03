from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']

what_search = input("What do you want to search : ")
how_many_to_follow = int(input("How many new accounts do you want to follow (max 50) : "))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://web.whatsapp.com")

# wait for page load
time.sleep(2)

# decline optional cookies
decline_optional_cookies_button = driver.find_element(By.CLASS_NAME, "_a9--._ap36._a9_1")
decline_optional_cookies_button.click()

# enter email
email_box = driver.find_element(By.ID, value="«r6»")
email_box.send_keys(EMAIL)

#enter password
password_box = driver.find_element(By.ID, value="«r9»")
password_box.send_keys(PASSWORD)

# don't save login information
dont_save_button = driver.find_element(By.XPATH, '//*[@id="mount_0_0_kz"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div')
dont_save_button.click()

#search

search_icon = driver.find_element(By.CLASS_NAME, "x1lliihq.x193iq5w.x6ikm8r.x10wlt62.xlyipyv.xuxw1ft")
search_icon.click()
input_search_box = driver.find_element(By.XPATH, '//*[@id="mount_0_0_zH"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
input_search_box.send_keys(what_search)

#enter to top 1 profile
profile_button = driver.find_element(By.XPATH, '//*[@id="mount_0_0_zH"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/a[1]/div[1]/div/div/div[2]/div/div/div/span')
profile_button.click()

#enter to followers list
follower_list_element = driver.find_element(By.XPATH, '//*[@id="mount_0_0_zH"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span')
follower_list_element.click()
to_follow_list = driver.find_elements(By.CLASS_NAME, '._acan._acap._acas._aj1-._ap30')

for account in to_follow_list:
    how_many_to_follow -= 1
    account.click()
    if how_many_to_follow == 0:
        break
