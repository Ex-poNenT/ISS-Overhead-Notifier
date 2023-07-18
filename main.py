import requests
from datetime import datetime
import smtplib
import time

my_lat = 18.520430
my_long = 73.856743

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # print(response.status_code)
    response.raise_for_status()

    data = response.json()["iss_position"]

    iss_longitude = float(data["longitude"])
    iss_latitude = float(data["latitude"])

    if iss_latitude in range(my_lat - 5, my_lat + 6) and iss_longitude in range(my_long - 5, my_long + 6):
        return True


def is_night():
    parameters = {
        "lat": my_lat,
        "long": my_long,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    
    if time_now >= sunset and time_now <= sunrise:
        return True
    
#Tasks :
# if the ISS is close to my current position
# and it is currently dark
# then send me an email to tell me to look up
# run the code every 60 seconds .


while True:
    time.sleep(60)
    if is_night() and is_iss_overhead() :
        my_email = "exponent23456@gmail.com"
        my_pass = "qqjynldgakasoyil"
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password= my_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="Xyz12345@gmail.com",
            msg="Subect:LOOK UP NOW\n\nThe ISS is above you in the sky ")

