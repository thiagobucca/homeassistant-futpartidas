import requests
from bs4 import BeautifulSoup
import json
import sys
import unicodedata

if len(sys.argv) < 2:
    print("Please provide a team name.")
    sys.exit()

team = sys.argv[1]
team = team.lower().replace(' ', '-')
team = unicodedata.normalize('NFKD', team).encode('ASCII', 'ignore').decode('ASCII')

url = f"https://www.placardefutebol.com.br/time/{team}/proximos-jogos"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

main_div = soup.find(id="main")

matches = []
for element in main_div.find_all(class_="match__md_card"):
    match = {}
    match["campeonato"] = element.find(class_="match__md_card--league").get_text(strip=True)
    match["mandante"] = element.find(class_="match__md_card--ht-name").get_text(strip=True)
    match["visitante"] = element.find(class_="match__md_card--at-name").get_text(strip=True)
    match["mandante_img"] = element.find(class_="match__md_card--ht-logo").img["src"]
    match["visitante_img"] = element.find(class_="match__md_card--at-logo").img["src"]
    match["datetime"] = element.find(class_="match__md_card--datetime").get_text(separator=" ", strip=True).replace("\n", "")
    matches.append(match)

output = {}
if len(matches) > 0:
    output["campeonato_match_1"] = matches[0]["campeonato"]
    output["mandante_match_1"] = matches[0]["mandante"]
    output["visitante_match_1"] = matches[0]["visitante"]
    output["datetime_match_1"] = matches[0]["datetime"]
    output["mandante_img_match_1"] = matches[0]["mandante_img"]
    output["visitante_img_match_1"] = matches[0]["visitante_img"]
if len(matches) > 1:
    output["campeonato_match_2"] = matches[1]["campeonato"]
    output["mandante_match_2"] = matches[1]["mandante"]
    output["visitante_match_2"] = matches[1]["visitante"]
    output["datetime_match_2"] = matches[1]["datetime"]
    output["mandante_img_match_2"] = matches[1]["mandante_img"]
    output["visitante_img_match_2"] = matches[1]["visitante_img"]
if len(matches) > 2:
    output["campeonato_match_3"] = matches[2]["campeonato"]
    output["mandante_match_3"] = matches[2]["mandante"]
    output["visitante_match_3"] = matches[2]["visitante"]
    output["datetime_match_3"] = matches[2]["datetime"]
    output["mandante_img_match_3"] = matches[2]["mandante_img"]
    output["visitante_img_match_3"] = matches[2]["visitante_img"]
if len(matches) > 3:
    output["campeonato_match_4"] = matches[3]["campeonato"]
    output["mandante_match_4"] = matches[3]["mandante"]
    output["visitante_match_4"] = matches[3]["visitante"]
    output["datetime_match_4"] = matches[3]["datetime"]
    output["mandante_img_match_4"] = matches[3]["mandante_img"]
    output["visitante_img_match_4"] = matches[3]["visitante_img"]
if len(matches) > 4:
    output["campeonato_match_5"] = matches[4]["campeonato"]
    output["mandante_match_5"] = matches[4]["mandante"]
    output["visitante_match_5"] = matches[4]["visitante"]
    output["datetime_match_5"] = matches[4]["datetime"]
    output["mandante_img_match_5"] = matches[4]["mandante_img"]
    output["visitante_img_match_5"] = matches[4]["visitante_img"]

print(json.dumps(output,ensure_ascii=False))
