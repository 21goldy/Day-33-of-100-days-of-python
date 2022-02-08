import datetime as dt
import pandas as pd
import smtplib
import random

MY_EMAIL = "**************@gmail.com"
PASSWORD = "****************"
PLACEHOLDER = "[NAME]"

# ---------------- READING CSV ---------------- #

birthday_csv = pd.read_csv("birthdays.csv")
dictionary = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday_csv.iterrows()
}

# ---------------- CHECKING DATE & MONTH ---------------- #

today = dt.datetime
day = today.now()
month = int(day.strftime("%m"))
day = int(day.strftime("%d"))
today_tuple = (month, day)


if today_tuple in dictionary:
    birthday_person = dictionary[today_tuple]
    birthday_person_name = birthday_person["name"]

# ---------------- PICKING A RANDOM LETTER ---------------- #

    letter_list = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
    random_letter = random.choice(letter_list)
    with open(f"letter_templates/{random_letter}") as letter:
        a = letter.read()

# ---------------- SENDING THE MAIL ---------------- #

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{a.replace(PLACEHOLDER, birthday_person_name)}"
        )
