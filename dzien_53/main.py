from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By



LINK_TO_FORMS = "https://docs.google.com/forms/d/e/1FAIpQLSdok1MFFSLvseFrTkKM11xNEmyjc42D5NKA2K9dkML5tPELAw/viewform?usp=dialog"
ZILLOW_LINK = "https://appbrewery.github.io/Zillow-Clone/"
RESPONSES_SHEET_LINK = "https://docs.google.com/spreadsheets/d/1ha5-AvoXmQD6rTFhexB6SCYcB3l_9uC3maRmlIQEp-0/edit?resourcekey=&gid=330837182#gid=330837182"

response = requests.get(url=ZILLOW_LINK)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=LINK_TO_FORMS)

soup = BeautifulSoup(response.text, "html.parser")
list_of_objects = soup.find_all("li", class_='ListItem-c11n-8-84-3-StyledListCardWrapper' )

print(list_of_objects)

list_of_links = [ element.find(name="a").get('href') for element in list_of_objects ]
list_of_prices = [ element.find(name='span', class_="PropertyCardWrapper__StyledPriceLine").text.split('+')[0].split('/')[0] for element in list_of_objects ]
list_of_addresses = [ element.find(name="address").text.strip() for element in list_of_objects ]

# print(list_of_links)
# print(list_of_prices)
# print(list_of_addresses)


for elm in range(len(list_of_links)):
    list_of_q = driver.find_elements(By.CLASS_NAME, value="whsOnd.zHQkBf")
    list_of_q[0].send_keys(list_of_links[elm])
    list_of_q[1].send_keys(list_of_prices[elm])
    list_of_q[2].send_keys(list_of_addresses[elm])

    submit_button = driver.find_element(By.CLASS_NAME, "NPEfkd.RveJvd.snByac")
    submit_button.click()

    send_answer_again = driver.find_element(By.CSS_SELECTOR, value="div[class='c2gzEf'] a")
    send_answer_again.click()



driver.get(RESPONSES_SHEET_LINK)


