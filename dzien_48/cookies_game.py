from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_element = driver.find_element(By.XPATH, value="//*[@id='cookie']")

upgrades_price_list = [element.text.split("\n")[0].split(" ")[-1].replace(",", "") for element in driver.find_elements(By.CSS_SELECTOR, "#store div[id^='buy']")]
upgrades_price_int_list = [int(element) for element in upgrades_price_list if element != '']
print(upgrades_price_int_list)

upgrade_name_list = [element.text.split("-")[0] for element in driver.find_elements(By.CSS_SELECTOR, "#store div[id^='buy']") ]

upgrade_dictionary = {key[:-1] : value for key, value in zip(upgrade_name_list, upgrades_price_int_list)}

upgrade_check_interval = 5
next_upgrade_check = time.time() + upgrade_check_interval

while True:
    money_element = driver.find_element(By.ID, value="money")
    money = int(money_element.text.replace(",", ""))
    cookie_element.click()
    current_time = time.time()
    if current_time >= next_upgrade_check:
        for key in reversed(upgrade_dictionary.keys()):
            if upgrade_dictionary[key] <= money:
                print("Kupuję:", key)
                try:
                    upgrade_to_buy = driver.find_element(By.ID, value=f"buy{key}")
                    upgrade_to_buy.click()
                    break
                except:
                    continue

        next_upgrade_check = current_time + upgrade_check_interval