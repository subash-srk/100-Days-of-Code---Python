import smtplib

my_email = "mail@mail.com"
password = "password"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="mail@mail.com", msg="Subject:Hello\n\nBody is this")
connection.close()
