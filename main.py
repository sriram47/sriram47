import requests
from datetime import datetime
import smtplib

MY_LAT = 37.677243  # Your latitude
MY_LONG = -121.79203  # Your longitude


def is_iss_near_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (iss_latitude - MY_LAT == 5 or iss_latitude - MY_LAT == -5) and (
            iss_longitude - MY_LONG == 5 or iss_longitude - MY_LONG == -5):
        return True
    else:
        return False


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
hour_now = time_now.hour

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


if sunset <= hour_now <= sunrise and is_iss_near_me() == True:
    my_email = "sripy2022@gmail.com"
    password = "Sri@2022"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="sripy2022@outlook.com",
            msg="Subject:Look Up in the sky!\n\n Hey, Look up in the sky. ISS is crossing"
        )
