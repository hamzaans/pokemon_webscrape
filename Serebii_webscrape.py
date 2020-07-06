#Serebii Webscrape
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

INNER_HTML = 'innerHTML'
OUTER_HTML = 'outerHTML'

driver = webdriver.Firefox()
elems = driver.get("https://www.serebii.net/swordshield/galarpokedex.shtml")
# table = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/table[2]")
# rows = table.find_elements_by_tag_name("tr")

# # name = driver.find_elements_by_tag_name('#text')
# for row in rows:
#     //*[@id="content"]/main/table[2]/tbody/tr[3]/td[3]/a
#     name = row.find_element_by_css_selector('td:nth-child(3) > a')
#     print("name")
#     print(name)
#     print("-----------------------------------------")
# print(name.get_attribute("innerHTML"))

pokemon_jsons = []
# NORMAL POKEMON
i = 3
while i < 403:
    name_xPath = '//*[@id="content"]/main/table[2]/tbody/tr[{i}]/td[3]/a'.format(i=i)
    image_xPath = '//*[@id="content"]/main/table[2]/tbody/tr[{i}]/td[2]/table/tbody/tr/td/a/img'.format(i=i)
    ability_xPath = '//*[@id="content"]/main/table[2]/tbody/tr[{i}]/td[4]'.format(i=i)

    name = driver.find_element_by_xpath(name_xPath).get_attribute(INNER_HTML).split("<br>")[0].strip()
    image = 'https://www.serebii.net/' + (driver.find_element_by_xpath(image_xPath).get_attribute(OUTER_HTML).split('src="')[1].split('" class')[0])
    abilities = driver.find_element_by_xpath(ability_xPath).find_elements_by_tag_name('a')

    abilities_list = []
    for ability in abilities:
        abilities_list.append(ability.get_attribute(INNER_HTML))

    pokemon_json = {"name": name, "image": image, "abilities": abilities_list}
    # print(pokemon_json)
    pokemon_jsons.append(pokemon_json)
    i = i + 1

# EXPANSION POKEMON
i = 12
while i < 81:
    name_xPath = '//*[@id="content"]/main/table[3]/tbody/tr[{i}]/td[3]'.format(i=i)
    image_xPath = '//*[@id="content"]/main/table[3]/tbody/tr[{i}]/td[2]/table/tbody/tr/td/img'.format(i=i)
    ability_xPath = '//*[@id="content"]/main/table[3]/tbody/tr[{i}]/td[4]'.format(i=i)

    name = driver.find_element_by_xpath(name_xPath).get_attribute(INNER_HTML).split("<br>")[0].strip()
    image = 'https://www.serebii.net/' + (driver.find_element_by_xpath(image_xPath).get_attribute(OUTER_HTML).split('src="')[1].split('" class')[0])
    abilities = driver.find_element_by_xpath(ability_xPath).find_elements_by_tag_name('a')
    
    # if the pokemon does exist - continue
    if abilities[0].get_attribute(INNER_HTML):
        abilities_list = []
        for ability in abilities:
            abilities_list.append(ability.get_attribute(INNER_HTML))
        pokemon_json = {"name": name, "image": image, "abilities": abilities_list}
        # print(pokemon_json)
        pokemon_jsons.append(pokemon_json)

    
    i = i+1

driver.close()

# print pokemon jsons
# print(pokemon_jsons)

print(json.dumps(pokemon_jsons, indent=4))