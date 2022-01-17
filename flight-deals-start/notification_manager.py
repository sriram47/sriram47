import smtplib
from flight_data import FlightData


class NotificationManager:

    def send_email(self, email_message):
        my_email = "sripy2022@gmail.com"
        password = "Sri@2022"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=f"sriram.ramachandran@outlook.com",
                msg=f"Low flight Alert!\n\n{email_message}"
            )