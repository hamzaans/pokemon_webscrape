#Pokemon Cards Webscrape
import time
import traceback
import re
import os
import sys
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from datetime import datetime
from datetime import date

#get rid of vmax, v, ex, gx
def check_invalid(name):
    name = name.lower()
    
    arr = [' ex', ' vmax', ' v', ' ex', ' gx', '-ex', '-gx', '&amp', 'break', 'team', 'shining ', 'dark ', 'rocket', 'flying ', 'surfing ', 'Imakuni', ' cloak', '[g]', '[gl]', '[fb]', '[c]', ' legend', ]
    if any(c in name for c in arr):
        return True
    
    return False

visited = []
INNER_HTML = 'innerHTML'
OUTER_HTML = 'outerHTML'
xPath = '//*[@id="cardResults"]/li[1]/a/div/img'

URL = "https://www.pokemon.com/us/pokemon-tcg/pokemon-cards/{i}?cardName=&cardText=&evolvesFrom=&card-grass=on&card-fire=on&card-water=on&card-lightning=on&card-psychic=on&card-fighting=on&card-darkness=on&card-metal=on&card-colorless=on&card-fairy=on&card-dragon=on&simpleSubmit=&format=unlimited&hitPointsMin=0&hitPointsMax=340&retreatCostMin=0&retreatCostMax=5&totalAttackCostMin=0&totalAttackCostMax=5&particularArtist=&sort=number&sort=number"

driver = webdriver.Firefox()

listy = []
url = ''
for i in range(1, 737):
    if i == 1:
        url = URL.format(i="")

    else:
        url = URL.format(i=str(i))
    
    driver.get(url)
    time.sleep(2)
    cards = driver.find_elements_by_class_name('animating')
    for card in cards:
        if "h4" in card.get_attribute(INNER_HTML):
            continue
        link = card.get_attribute(INNER_HTML).split("\"")[1]
        name = card.get_attribute(INNER_HTML).split("\"")[3]

        if check_invalid(name) == True:
            continue

        if name in visited:
            continue
        
        visited.append(name)
        dict_collection = {name: link}
        listy.append(dict_collection)

        # convert dict to json
        # dict_collection = json.dumps(dict_collection)

        print(dict_collection)

driver.close()

listy = json.dumps(listy, indent=4)

f = open("cards.json", "w")
f.write(listy)
f.close()