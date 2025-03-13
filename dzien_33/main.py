import datetime
import requests
import smtplib

response = requests.get( url = "http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = (longitude, latitude)
print(iss_position)

my_lat = 52.229675
my_lng = 21.012230
my_email = "<EMAIL>"
my_password = "<PASSWORD>"
your_email = "<EMAIL>"

parameters = {
    "lat" : my_lat,
    "lng" : my_lng,
    "formatted" : 0
}

response = requests.get(url = "https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
print(sunset)
time_now = datetime.datetime.now()

sunrise_time = sunrise.split("T")
time_split = sunrise_time[1].split(":")
sunrise_hour = int(time_split[0])

sunset_hour = int(sunset.split("T")[1].split(":")[0])

print(sunrise_hour)
print(sunset_hour)
print(time_now.hour)

if my_lng - 5 < iss_position[0] < my_lng + 5:
    if my_lat - 5 < iss_position[1] < my_lat + 5:
        if time_now.hour < sunrise_hour or time_now.hour > sunset_hour:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(my_email, my_password)
                smtp.sendmail(
                    from_addr = my_email,
                    to_addrs = your_email,
                    msg = f'Subject: Look up\n\nThe iss above you in the sky'
                )