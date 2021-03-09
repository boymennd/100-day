from bs4 import BeautifulSoup
import requests
# with open("index.html") as file:
#     content = file.read()
# soup = BeautifulSoup(content, "html.parser")
# print(soup.find_all("h2"))
with open("film.text", "a+") as file:
    file.write("TOP BEST ANIME IN THE WORLD!!!\n")
response = requests.get("https://myanimelist.net/topanime.php")
data = BeautifulSoup(response.text, "html.parser")
data_film = data.find_all(name="h3", class_="hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3")
a = 0
for i in data_film:
    a += 1
    with open("film.text", "a+") as file:
        file.write(f"{a}. {i.text}\n")





# data_score = data.find_all(name="span",class_="score")
# data_link = data.find_all(name="a",class_="storylink")
# score_list = [int(data.string.split()[0]) for data in data_score]
# max_score_num = score_list.index(max(score_list))
# print(data_link[max_score_num].get("href"))
