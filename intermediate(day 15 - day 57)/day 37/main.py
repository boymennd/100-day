import requests, datetime,os


def date_now():
    now = datetime.datetime.now()
    return now.strftime("%Y%m%d")


token_pixela = os.environ.get("token_pixela")
user_name = "boymennd"
graphs_id = "graphsofiobi1"
pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": token_pixela,
    "username": user_name,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint,json=user_parameters)
# print(response.text)
graphs_endpoint = f"{pixela_endpoint}/{user_name}/graphs"
graphs_parameters = {
    "id": graphs_id,
    "name": "Time coding Python",
    "unit": "Hour",
    "type": "float",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": token_pixela,
}
# response = requests.post(url=graphs_endpoint, json=graphs_parameters, headers=headers)
# print(response.text)


choose = input("What do you want?(post,put or delete)")
if choose == "post":
    post_endpoints = f"{graphs_endpoint}/{graphs_id}"
    post_parameters = {
        "date": date_now(),
        "quantity": input("How many hours do you code today?"),
    }
    response = requests.post(url=post_endpoints, json=post_parameters, headers=headers)
    print(response.text)
elif choose == "put":
    date_change = input("date you want to change?(yyyyMMdd)")
    put_endpoints = f"{graphs_endpoint}/{graphs_id}/{date_change}"
    put_parameters = {"quantity": input("hour you want to change?")}
    response = requests.put(url=put_endpoints, json=put_parameters, headers=headers)
    print(response.text)
else:
    date_delete = input("date you want delete?(yyyyMMdd)")
    delete_endpoints = f"{graphs_endpoint}/{graphs_id}/{date_delete}"
    response = requests.delete(url=delete_endpoints, headers=headers)
    print(response.text)
