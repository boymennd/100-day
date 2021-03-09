from bs4 import BeautifulSoup
# import lxml
with open("contacrt.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
exp = soup.find_all(name="a")
print(exp[0].get("href"))