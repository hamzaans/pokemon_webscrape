#Pokemon Showdown Webscrape
import time
import traceback
import re
import os
import sys
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from datetime import date

pokemon_jsons = []
def _scroll_to_bottom(driver):
    print('scrolling to bottom of page')

    utilichart = driver.find_element_by_class_name('utilichart')

    while '<button class="button big">More</button></p></li>' in utilichart.get_attribute('innerHTML'):
        utilichart.find_element_by_class_name('big').click()
        time.sleep(.5)
    
# Headless option
options = Options()
options.headless = False
pokemon_home_jsons = []

# Initialize driver
driver = webdriver.Firefox(options=options)
driver.get('https://play.pokemonshowdown.com/teambuilder')

# click new team and add pokemon buttons to get to list of pokemon
driver.find_element_by_xpath('/html/body/div[4]/div[2]/p[3]/button').click()
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ol/li[4]/button').click()

# use down keys to scroll down
_scroll_to_bottom(driver)

# For all pokemon in list, get names, abilites, hidden abilities, sprites
i = 3
while i <= 666:
    try:
        name_xPath = '//*[@id="room-teambuilder"]/div/div[4]/ul/li[{i}]/a/span[3]'.format(i=i)
        name = driver.find_element_by_xpath(name_xPath)
        name_inner = name.get_attribute('innerHTML')
        if "<small>-" in str(name_inner):
            name_inner = name_inner.replace("<small>-", " ").replace("</small>", "")
            print(name_inner)
        else: print(name_inner)

        ability_xPath = '//*[@id="room-teambuilder"]/div/div[4]/ul/li[{i}]/a/span[5]'.format(i=i)
        ability = driver.find_element_by_xpath(ability_xPath)
        ability_inner = ability.get_attribute('innerHTML')
        if "<br>" in str(ability_inner):
            ability_inner = ability_inner.split("<br>")
            print(ability_inner)
        else:
            print(ability_inner)
        
        if type(ability_inner) is not list:
            ability_inner = [ability_inner]

        h_ability_xPath = '//*[@id="room-teambuilder"]/div/div[4]/ul/li[{i}]/a/span[6]'.format(i=i)
        h_ability = driver.find_element_by_xpath(h_ability_xPath)
        h_ability_inner = h_ability.get_attribute('innerHTML')
        print(h_ability_inner)

        print("")
        pokemon_json = {"name": name_inner, "abilities": ability_inner, "hidden ability": h_ability_inner, "index": i}
        pokemon_jsons.append(pokemon_json)
        
    except:
        print("an error has occured")
        print(driver.find_element_by_xpath('//*[@id="room-teambuilder"]/div/div[4]/ul/li[{i}]'.format(i=i)).get_attribute('innerHTML'))
    i = i + 1

driver.close()
print(json.dumps(pokemon_jsons, indent=4))


