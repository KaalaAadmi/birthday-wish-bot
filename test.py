import smtplib
from email.message import EmailMessage
from datetime import date
import csv
import time


def send_wish(name, receiver):
    message = EmailMessage()
    message.set_content('Happy Birthday '+name+'\n\nLove, \n<Your Name> ♥')
    message['Subject'] = 'Happy Birthday'
    message['From'] = "<Your Email>"
    message['To'] = receiver

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # your email and password
    server.login('<>Your Email', "<Your Password>")
    server.send_message(message)
    print('mail sent')


def get_date():
    today = date.today()
    today = str(today)
    date_today = today[5:]
    return date_today


def readData():
    with open('birthdays.csv') as file:
        reader = csv.DictReader(file, delimiter=" ")
        for row in reader:
            bday = row['birthday']
            today = get_date()
            if(str(bday) == today):
                send_wish(row['name'], row['email'])
            else:
                time.sleep(86400)


readData()
