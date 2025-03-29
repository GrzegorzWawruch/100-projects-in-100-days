from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_3?_encoding=UTF8&content-id=amzn1.sym.2f889ce0-246f-467a-a086-d9a721167240&dib=eyJ2IjoiMSJ9.y4LLAMvRXyF-GJBFF44YpgWbgxoJo_XCbCGmJdSrQvbeTKdYVPdPw6K-mZz5Sd2ob4iL_yLtpEzc7hlRoGWQLLrltRGjFSnhiWPpJSbsczOt3Lq7xxJj022M_KC-wsu-18wnv_Jf8r03jMNlqHOPdiQOxscB6ZzdhLP-wOz-VzscGcEVbOw4LDOfgitYNBI3goEwlGT_DMjR1lE-bcvVxRGpYYeo0BKcGcvN5zDUgmE.vyoONPFnEes5SyTSrJaeRIDUSfqzsNCaZUkB_xfqOPI&dib_tag=se&keywords=cooker&pd_rd_r=8a69c6ab-4ffa-4042-82dc-d66e826365b6&pd_rd_w=QQ6RW&pd_rd_wg=p5cOP&qid=1743093795&refresh=1&sr=8-3')

price = driver.find_element(By.CLASS_NAME, "aok-offscreen")
print(price.text)

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))
#driver.close()

button = driver.find_element(By.ID, value="submit")
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.get_attribute("href"))

bug_link = driver.find_element(By.XPATH, value="//*[@id='documentation']")
print(bug_link.text)

driver.quit()