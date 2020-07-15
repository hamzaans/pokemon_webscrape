#Pokemon Home Webscrape
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

driver = webdriver.Firefox()
pokemon_list = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Squirtle', 'Wartortle', 'Blastoise', 'Mewtwo', 'Mew', 'Celebi', 'Jirachi', 'Cobalion', 'Terrakion', 'Virizion', 'Reshiram', 'Zekrom', 'Kyurem', 'Keldeo', 'Rowlet', 'Dartrix', 'Decidueye', 'Litten', 'Torracat', 'Incineroar', 'Popplio', 'Brionne', 'Primarina', 'Cosmog', 'Cosmoem', 'Solgaleo', 'Lunala', 'Necrozma', 'Marshadow', 'Zeraora', 'Meltan', 'Melmetal']

driver.get('https://serebii.net')
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("Bulbasaur")
elem.send_keys(Keys.RETURN)
time.sleep(3)

driver.find_element_by_xpath('//*[@id="___gcse_0"]/div/div/div/div[5]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div/a').click()

time.sleep(3)

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

#Want names, image, and abilities
name = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div/table[5]/tbody/tr[2]/td[1]').get_attribute('innerHTML')
print(name)

driver.close()