from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

provider_declared_download_speed = float(input("What is your download speed declared by your internet provider? Type on MB/s: "))
provider_declared_upload_speed = float(input("What is your upload speed declared by your internet provider? Type on MB/s: "))

load_dotenv()
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.speedtest.net/pl")

# decline cookies on speedtest website
time.sleep(2)
try:
    decline_cookies_button = driver.find_element(By.ID, value="onetrust-reject-all-handler")
    decline_cookies_button.click()
except:
    pass
# start internet test
start_test_button = driver.find_element(By.CLASS_NAME, "start-text")
start_test_button.click()
#download results
while True:
    try:
        #download file
        download_element = driver.find_element(By.CLASS_NAME, "result-data-large.number.result-data-value.download-speed")
        download_speed = float(download_element.text)
        upload_element = driver.find_element(By.CLASS_NAME, "result-data-large.number.result-data-value.upload-speed")
        upload_speed = float(upload_element.text)
        provider_element = driver.find_element(By.CLASS_NAME, "js-data-sponsor")
        internet_provider = provider_element.text
        break
    except:
        try:
            back_to_results_button = driver.find_element(By.CLASS_NAME, "close-btn")
            back_to_results_button.click()
        except:
            pass

print(download_speed)
print(upload_speed)

#porównanie dodać

if download_speed < provider_declared_download_speed or upload_speed < provider_declared_upload_speed:
    # Twitter part
    driver.get("https://x.com/")
    time.sleep(3)

    # decline cookies on twitter
    decline_twitter_cookies = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/button[2]/div/span/span')
    decline_twitter_cookies.click()

    #sign in on twitter
    sign_in_button_twitter = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[3]/a/div')
    sign_in_button_twitter.click()

    #email box
    email_box = driver.find_element(By.NAME, 'text')
    email_box.send_keys(TWITTER_EMAIL)

    #next_button
    next_login_button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
    next_login_button.click()

    #password box
    password_box = driver.find_element(By.NAME, 'password')
    password_box.send_keys(TWITTER_PASSWORD)

    #final login
    final_login_button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div')
    final_login_button.click()

    #write post
    #enter post text
    post_text_field = driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
    post_text_field.send_keys(f"Hey {internet_provider}, why is my internet speed {download_speed}down/{upload_speed}up when I pay for {provider_declared_download_speed}down/{provider_declared_upload_speed}up?")

    #psot_button
    # post_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
    # post_button.click()
