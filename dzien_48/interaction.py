from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

editors_element = driver.find_element(By.XPATH, value="//*[@id='articlecount']/ul/li[2]/a[1]")
print(editors_element.text)

all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
#all_portals.click()

search_lup = driver.find_element(By.XPATH, value="//*[@id='p-search']/a")
search_lup.click()

time.sleep(1)

search = driver.find_element(By.NAME, "search")

search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()