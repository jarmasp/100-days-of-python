from multiprocessing import connection
import requests
from datetime import datetime
import smtplib
import time 

my_email = 'my email'
my_passwd = 'my password'

MY_LAT = 10.480594 #latitude
MY_LONG = -66.903603 #longitude

def iss_above_me():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if  MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True 


def night_time():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now >= sunset and time_now <= sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)

    if night_time() and iss_above_me():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(my_email, my_passwd)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject:Look up\n\nThe iss it's in the sky"
    )




