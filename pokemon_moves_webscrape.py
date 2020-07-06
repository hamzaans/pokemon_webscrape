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
# xPath = '//*[@id="mw-content-text"]/table[1]/tbody/tr/td/table/tbody'
INNER_HTML = 'innerHTML'
OUTER_HTML = 'outerHTML'
# //*[@id="mw-content-text"]/table[1]/tbody/tr/td/table/tbody/tr[1]/td[2]/a
# //*[@id="mw-content-text"]/table[1]/tbody/tr/td/table/tbody/tr[2]/td[2]/a
# //*[@id="mw-content-text"]/table[1]/tbody/tr/td/table/tbody/tr[818]/td[2]/a
driver = webdriver.Firefox()
elems = driver.get("https://bulbapedia.bulbagarden.net/wiki/List_of_moves")
i = 1
while i <= 842:
    try:
        move_xPath = '//*[@id="mw-content-text"]/table[1]/tbody/tr/td/table/tbody/tr[{i}]/td[2]/a'.format(i=i)
        move = driver.find_element_by_xpath(move_xPath).get_attribute(INNER_HTML)
        
        print(move)
    except:
        pass
    i = i + 1


driver.close()