# Monday Motivation Project
import datetime as dt
import random
import smtplib

MY_MAIL = ""
PASSWORD = ""

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("quotes.txt") as quote_file:
        quote_list = quote_file.readlines()
        quote = random.choice(quote_list)
    # print(quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_MAIL, PASSWORD)
        connection.sendmail(from_addr=MY_MAIL,
                            to_addrs="",
                            msg=f"Subject:Monday Motivation\n\n{quote}")
