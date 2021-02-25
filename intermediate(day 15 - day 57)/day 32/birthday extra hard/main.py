import pandas, random, smtplib
import datetime as dt


my_gmail = "iobi1907@gmail.com"
password = "01214179548"


def send_mail(name, email):
    a = random.randint(1, 3)
    with open(f"letter_templates/letter_{a}.txt", "r") as f:
        data_file = f.read()
        mail_file = data_file.replace("[NAME]", name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=email,
            msg=f"Subject:Happy birthday!\n\n{mail_file}",
        )


now = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")
for i in range(len(data)):
    if data.day[i] == now.day and data.month[i] == now.month:
        send_mail(data.name[i], data.email[i])
