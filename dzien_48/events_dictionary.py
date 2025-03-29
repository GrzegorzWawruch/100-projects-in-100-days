
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

date_elements = driver.find_elements(By.CSS_SELECTOR, "div.medium-widget.event-widget.last li time")
dates = [element.get_attribute("datetime").split("T")[0] for element in date_elements]
event_titles_elements = driver.find_elements(By.CSS_SELECTOR, "div.medium-widget.event-widget.last li a")
event_titles = [element.text for element in event_titles_elements]

print(dates)
print(event_titles)

events_dict = {}
for number in range(len(dates)):
    events_dict[number] = {
        "date" : dates[number],
        "title" : event_titles[number]
    }

print(events_dict)

driver.quit()