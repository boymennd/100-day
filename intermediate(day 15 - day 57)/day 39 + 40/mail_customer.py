import requests, os

user_sheety = os.environ.get("USER_sheety")
pass_sheety = os.environ.get("PASS_sheety")
sheety_endpoint = (
    "https://api.sheety.co/3433f1cc0c04e3c800e561ff11e8e9d4/customerMail/trangTính1"
)


class MailCus:
    def __init__(self):
        self.first_name = input("What is your first name?")
        self.last_name = input("What is your last name?")
        self.mail_cus = input("Enter your email?")
        self.mail_retype = input("Type your email again?")
        self.mail_list = []
        self.check_mail()
        self.add_to_mail_list()

    def check_mail(self):
        if self.mail_cus != self.mail_retype:
            print("You have entered the wrong email inviting you to re-enter!")
        else:
            parameters = {
                "trangTính1": {
                    "firstName": self.first_name,
                    "lastName": self.last_name,
                    "email": self.mail_cus,
                }
            }
            requests.post(
                url=sheety_endpoint, json=parameters, auth=(user_sheety, pass_sheety)
            )

    def add_to_mail_list(self):
        response = requests.get(url=sheety_endpoint, auth=(user_sheety, pass_sheety))
        data = response.json()["trangTính1"]
        self.mail_list = [cus["email"] for cus in data]
