import datetime as dt
import pandas
import random
import smtplib

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

my_email = "@gmail.com"
password = ""
email_subject = "Happy Birthday"


def send_email(to_addrs, body):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_addrs,
            msg=f"Subject: {email_subject}\n\n{body}"
        )


# Use pandas to read the birthdays.csv

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    # Pick random letter
    random_letter = random.randint(1, 3)
    with open(f"./letter_templates/letter_{random_letter}.txt") as letter_file:
        letter = letter_file.read()

    # Replace [NAME] with actual name
    letter = letter.replace("[NAME]", birthdays_dict[today]["name"])
    email_to = birthdays_dict[today]["email"]
    send_email(email_to, letter)
