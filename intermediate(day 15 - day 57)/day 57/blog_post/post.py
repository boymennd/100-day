import requests

blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"


class Post:
    def __init__(self):
        self.response = requests.get(url=blog_url).json()
        self.title = [data["title"] for data in self.response]
        self.subtitle = [data["subtitle"] for data in self.response]
        self.body = [data["body"] for data in self.response]
