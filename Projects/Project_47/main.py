# AMAZON PRICE TRACKER
import requests
from bs4 import BeautifulSoup
import smtplib

BUY_PRICE = 80
MY_EMAIL = ""
MY_PASSWORD = ""
RECEIVER = ""

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,ta;q=0.6"
}

response = requests.get(url=URL, headers=header)
web = response.content

soup = BeautifulSoup(web, "lxml")
price = soup.find(class_="a-price-whole").get_text()
price_wo_dot = price.split(".")[0]
price_as_float = float(price_wo_dot)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

price_as_float = 50
message = ""
if price_as_float < BUY_PRICE:
    message = f"{title} is now at ${price_as_float}"

with smtplib.SMTP(MY_EMAIL, 587) as connection:
    connection.starttls()
    result = connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=RECEIVER,
        msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
    )