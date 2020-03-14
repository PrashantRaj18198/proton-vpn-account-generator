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
import os


from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.select import Select

print('ProtonVPN account creation started')

warnings.filterwarnings("ignore", category=DeprecationWarning) 

options = Options()

email_driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)

email_url = 'https://www.guerrillamail.com/'

print("Loading temp-mail server:", email_url)

email_driver.get(email_url)

t = 0
timeout = 60

def checkTimeout():
    global t, timeout
    if t > timeout:
        t = 0
        print("Connection timed out. Exiting now!")
        exit(-1)
    t += 1

while True:
    try:
        email = email_driver.find_element_by_id('inbox-id').text + '@'
        domain_name = Select(email_driver.find_element_by_id('gm-host-select')).first_selected_option.text
        email += domain_name
        print(email)
        break
    except:
        checkTimeout()
        time.sleep(1)


verifymail = email

# Change Path to Chrome Driver Path (or move your ChromeDriver into the project folder)
driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)


url = 'http://account.protonvpn.com/signup'

def randomStringDigits(stringLength=13):
    # Generate a random string of letters and digits
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def getUserName():
    f = open('lastused.txt')
    val = int(f.readline())
    f.close()
    f = open('lastused.txt', 'w')
    val += 1
    f.write(str(val))
    return 'AbolitionMan'+str(val - 1)

rngusername = getUserName()
rngpassword = randomStringDigits(13)

print("Loading protonvpn server:", url)

driver.get(url)

while True:
    try:
        driver.find_element_by_css_selector("body > div.app-root > main > main > div > div:nth-child(5) > div:nth-child(1) > div.flex-item-fluid-auto.pt1.pb1.flex.flex-column > button").click()
        break
    except:
        checkTimeout()
        time.sleep(1)

while True:
    try:
        driver.find_element_by_id("username").send_keys(rngusername)
        driver.find_element_by_id("password").send_keys(rngpassword)
        driver.find_element_by_id("passwordConfirmation").send_keys(rngpassword)
        driver.find_element_by_id("email").send_keys(verifymail)
        driver.find_element_by_css_selector("body > div.app-root > main > main > div > div.pt2.mb2 > div > div:nth-child(1) > form > div:nth-child(3) > div > button").click()
        break
    except:
        checkTimeout()
        time.sleep(1)
while True:
    try:
        driver.find_element_by_css_selector("body > div.app-root > main > main > div > div.pt2.mb2 > div > div.w100 > div:nth-child(2) > div > div > div:nth-child(2) > form > div:nth-child(2) > button").click()
        break
    except:
        checkTimeout()
        time.sleep(1)

print("Wait for verification")

while True:
    try:
        val = email_driver.find_element_by_class_name('email-excerpt').text
        if not val[-6:].isnumeric():
            raise Exception
        print(val[-6:], "verification")
        driver.find_element_by_id('code').send_keys(val[-6:])
        time.sleep(1)
        driver.find_element_by_css_selector('body > div.app-root > main > main > div > div.pt2.mb2 > div > div.w100 > div:nth-child(2) > form > div > div > div:nth-child(4) > button').click()
        break
    except:
        checkTimeout()
        time.sleep(1)

print("Account Created \uE405\nYour Details")

f = open('list.csv', 'a')
info = rngusername +', '+ rngpassword + '\n'
f.write(info)
print("Username", rngusername, "Password", rngpassword)
print("Info also added to list.csv")