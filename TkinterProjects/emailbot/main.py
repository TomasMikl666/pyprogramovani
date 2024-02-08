import requests
import smtplib

#API
response = requests.get(url="https://api.kanye.rest/")
data = response.json()
quote = data["quote"]

#Sending Email address
my_email1 = "yourgmail@gmail.com"
password = "yourpassword for apps"

message = f"Subject: Nazdar Bazar\n\nAhoj, ty zabijaku\nKanye West: {quote}"

#Receiving Email Address
my_email2 = ["email@gmail.com", "pythontesttomas2@seznam.cz"]

#Main code
with smtplib.SMTP(host="smtp.gmail.com.", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email1, password=password)
    connection.sendmail(from_addr=my_email1,
                        to_addrs=my_email2,
                        msg=message.encode("utf-8"))