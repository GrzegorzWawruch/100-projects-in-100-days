from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

AMAZOR_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]
RECIVER_EMAIL = os.environ["RECIVER_EMAIL"]

load_dotenv()
ACCEPT_LANGUAGE = os.environ["ACCEPT_LANGUAGE"]
USER_AGENT = os.environ["USER_AGENT"]

HEADER = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": ACCEPT_LANGUAGE,
    "Host": "httpbin.org",
    "Priority": "u=0, i",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": USER_AGENT,
    "X-Amzn-Trace-Id": "Root=1-67e5138d-35b77d8e21ee6a6a0fba960a"
}

response = requests.get(url=AMAZOR_URL, headers=HEADER)
sp = BeautifulSoup(response.text, "html.parser")

price = sp.find("span", class_ = "aok-offscreen").text
price = float(price.replace("$", ""))

product = sp.find(id="productTitle").text
product = product.split(" ")
product = [name for name in product if name != "" ]

item_list = []
for element in product:
    if "\n" in element:
        element = element.replace("\n", "")
        if "\r" in element:
            element = element.replace("\r", "")
            item_list.append(element)
    else:
        item_list.append(element)

delimiter = " "
product_name = delimiter.join(item_list)

content = f"Subject:Amazon Price Alert!\n\n{product_name}\n{AMAZOR_URL}"

target = float(100) #float(input(f"Set your price target: "))

if target > price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs= RECIVER_EMAIL,
            msg=content.encode("utf-8")
        )
