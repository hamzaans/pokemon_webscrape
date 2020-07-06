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
elems = driver.get("https://www.serebii.net/swordshield/items.shtml")

i = 2
while i < 403:
    name_xPath = '//*[@id="content"]/main/table[12]/tbody/tr[{i}]/td[2]/a'.format(i=i)
    name = driver.find_element_by_xpath(name_xPath).get_attribute(INNER_HTML)
    
    print(name)
    i = i + 1


driver.close

