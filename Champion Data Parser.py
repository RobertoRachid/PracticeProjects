import requests
from bs4 import BeautifulSoup
while True:
    selectedChamp = input("\nEnter champion name (or type \"exit\" to quit program):\n>").title().replace(" ","").replace("'","")
    if (selectedChamp == "Exit"):
        break
    URL = f"https://u.gg/lol/champions/{selectedChamp}/build"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    if (soup.find(class_="champion-name") == None or selectedChamp == ""):
        print("\nChampion name invalid.")
    else:
        champName = soup.find(class_="champion-name").get_text()
        champWin, champRank, champPick, champBan, champMatches = [tag.get_text() for tag in soup.select('.champion-ranking-stats .value')]
        print('\nWin rate:', champWin)
        print('Champion rank in role:', champRank)
        print('Pick rate:', champPick)
        print('Ban rate:', champBan)
        print('Matches found:', champMatches)
        champRawSummonerSpells = soup.find(class_="grid-block summoner-spells")
        champSummonerSpells = champRawSummonerSpells.find_all("img")
        print(f"\nSummoner spells for {champName}\n")
        print(f"Spell 1: {champSummonerSpells[0].get('alt')}")
        print(f"Spell 2: {champSummonerSpells[1].get('alt')}")
exit()