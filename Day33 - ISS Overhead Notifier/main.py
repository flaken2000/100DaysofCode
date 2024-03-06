import requests
from datetime import datetime
import smtplib

# Fill in below with https://www.latlong.net/
MY_LAT = 0
MY_LONG = 0

my_email = "@gmail.com"
password = ""
email_subject = "ISS is close!"


def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: {email_subject}\n\nLook up in the sky!"
        )


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "America/Toronto",
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

hour_now = datetime.now().hour

# If the ISS is close to my current position
if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5:
    # and it is currently dark
    if hour_now >= sunset or hour_now <= sunrise:
        # Then send me an email to tell me to look up.
        send_email()
