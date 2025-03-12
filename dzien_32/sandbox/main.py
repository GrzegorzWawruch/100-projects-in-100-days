# import smtplib
#
# my_email = "wawruch.grzegorz.kontakt@gmail.com"
# password = "123"
#
# your_email = "<EMAIL>"

# with  smtplib.SMTP('smtp.gmail.com', 587) as connection:
#     connection.starttls()
#     connection.login(user = my_email , password = password)
#     connection.sendmail(from_addr=my_email, to_addrs="your_email", msg="Subject:Hello \n\n This is the body of my email")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(now)
# print(year)
#
# date_of_birth = dt.datetime(year,1,1)

import datetime as dt
import smtplib
import random

my_email = "wawruch.grzegorz.kontakt@gmail.com"
password = "123"

your_email = "<EMAIL>"

day_of_week = dt.date.today().weekday()
if day_of_week == 1:    # 0 = Monday

    with open("quotes.txt") as data:
        all_quotes = data.readlines()
        quote = random.choice(all_quotes)


    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=your_email, msg=f"Subject: Hello World! \n\n {quote}")