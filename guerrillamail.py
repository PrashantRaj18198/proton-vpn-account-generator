from selenium import webdriver
from colorama import Fore, Back, Style
import warnings
import time
import random
import string
import urllib.request
import requests
import csv
import sys
from proxyscrape import create_collector
from time import sleep
import os
clear = lambda: os.system('clear')
clear()

collector = create_collector('my-collector', 'https')

from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.select import Select

warnings.filterwarnings("ignore", category=DeprecationWarning) 

options = Options()
driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)

url = 'https://www.guerrillamail.com/'

driver.get(url)

time.sleep(4)

print(driver.find_element_by_id('inbox-id').text)
email = driver.find_element_by_id('inbox-id').text + '@';
domain_name = Select(driver.find_element_by_id('gm-host-select')).first_selected_option.text
# domain_name = driver.find_element_by_id('gm-host-select').text
email += domain_name
print(domain_name)
print(email)
f = open('./input_emails.txt', 'w')
f.write(email)
# sleep(60)
# driver.find_element_by_partial_link_text('verification').click()
# print(driver.find_element_by_class_name('email-excerpt').text)
# sleep(60)
print(driver.find_element_by_class_name('email-excerpt').text)