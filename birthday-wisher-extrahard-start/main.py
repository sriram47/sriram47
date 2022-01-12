##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates
# and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import random
import smtplib
import pandas
import datetime as dt

now = dt.datetime.now()
day_today = now.day
month_today = now.month

birthday_data = pandas.read_csv("birthdays.csv")
# name_birth_list = [birthday_data.name for name in birthday_data.name if birthday_data.day == day_today]
# birthday_row = birthday_data[birthday_data["day"] == day_today, birthday_data["month"] == month_today]
birthday_row = birthday_data.loc[(birthday_data["day"] == day_today) & (birthday_data["month"] == month_today)]
# birthday_month = birthday_data[birthday_data["month"] == day_today]
count = 0

while count < birthday_row.name.count():
    try:
        birthday_name = birthday_row["name"].values[count]
        birthday_email = birthday_row["email"].values[count]
    except IndexError:
        birthday_name = ""
        birthday_email = ""
    else:
        if (len(birthday_name) > 0) and (len(birthday_email > 0)):
            with open("letter_templates/letter_1.txt", mode='r') as letter1:
                letter_1_data = letter1.read()
                letter_1_data = letter_1_data.replace('[NAME]', birthday_name)
            with open("letter_templates/letter_2.txt", mode='r') as letter2:
                letter_2_data = letter2.read()
                letter_2_data = letter_2_data.replace('[NAME]', birthday_name)
            with open("letter_templates/letter_3.txt", mode='r') as letter3:
                letter_3_data = letter3.read()
                letter_3_data = letter_3_data.replace('[NAME]', birthday_name)

            letters = [letter_1_data, letter_2_data, letter_3_data]
            letter_to_send = random.choice(letters)
            my_email = "sripy2022@gmail.com"
            password = "Sri@2022"

            # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            #     connection.starttls()
            #     connection.login(user=my_email, password=password)
            #     connection.sendmail(
            #         from_addr=my_email,
            #         to_addrs=f"{birthday_email}",
            #         msg=f"Subject:Happy Birthday!\n\n{letter_to_send}"
            #     )
            print(birthday_name, birthday_email)
        else:
            pass

    count += 1

print("It's not anyone's birthday today")
# print(birthday_row.name.count())


# print(birthday_data[birthday_data["day"] == day_today])




