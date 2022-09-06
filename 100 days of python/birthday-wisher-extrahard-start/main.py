##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import pandas as pd
import random as rd

email = 'my_email'
password = 'my_password'

today = (dt.datetime.now())
today_tuple = (today.month, today.day)

df = pd.read_csv('birthdays.csv')

bd_dic = {(df_row['month'], df_row['day']): df_row for (index, df_row) in df.iterrows()}

print(bd_dic)

if today_tuple in bd_dic:
    birthday_person = bd_dic[today_tuple]
    letter_choice = rd.randint(1,3)
    file_path = f'letter_templates/letter_{letter_choice}.text'
    with open (file_path) as letter:
        text = letter.read()
        text = text.replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(from_addr = email, 
        to_addrs = birthday_person['email'] 
        msg= f'Subject: Happy birthday \n \n {text}')