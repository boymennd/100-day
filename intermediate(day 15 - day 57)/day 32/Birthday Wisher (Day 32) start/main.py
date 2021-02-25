import smtplib, random
import datetime as dt

my_gmail = "iobi1907@gmail.com"
password = "01214179548"
lists = []


def sent_mail():
    with open("quotes.txt", "r") as f:
        lists.extend(f.readlines())

    new_list = [item.strip() for item in lists]
    content = random.choice(new_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=my_gmail,
            msg=f"Subject:Good morning!\n\n{content}",
        )


date = dt.datetime.now()
if date.weekday() == 0:
    sent_mail()
