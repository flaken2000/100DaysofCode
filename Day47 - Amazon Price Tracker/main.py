from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os

amazon_item = "https://www.amazon.ca/dp/B0C33XXS56/?coliid=I1N145Q3G78NP6&colid=3DH44XCYUN8WF&ref_=list_c_wl_lv_ov_lig_dp_it&th=1"
target_price = 350


def send_email(from_addrs, to_addrs, subject, body):
    password = os.environ.get("MY_EMAIL_PASS", "Env variable MY_EMAIL_PASS doesn't exists")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=from_addrs, password=password)
        connection.sendmail(
            from_addr=from_addrs,
            to_addrs=to_addrs,
            msg=f"Subject: {subject}\n\n{body}"
        )


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "Accept-Language": "en-US,en;q=0.9,fr;q=0.8,en-CA;q=0.7,fr-CA;q=0.6"
}

response = requests.get(amazon_item, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
price_whole = soup.find(name="span", class_="a-price-whole").getText()
price_decimal = soup.find(name="span", class_="a-price-fraction").getText()
price = float(price_whole + price_decimal)
print(price)

if price <= target_price:
    product_title = soup.find(name="span", id="productTitle").getText().strip()
    from_addrs = os.environ.get("MY_EMAIL", "Env variable MY_EMAIL doesn't exists")
    to_addrs = from_addrs
    email_subject = "Amazon Price Tracker 3000 Alert!"
    email_body = f"{product_title} is now {price}$\n{amazon_item}"
    send_email(from_addrs, to_addrs, email_subject, email_body)
