# 🚀 This Project is in it's early stages of Development.
# 📌 Working on new features and main menu.
# ⚠️ Any Questions or Suggestions please Mail to: hendriksdevmail@gmail.com
# 🖥 Version: 1.0.0

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
clear = lambda: os.system('clear')
clear()

collector = create_collector('my-collector', 'https')

print ('\033[31m' + """\
    ____             __              __  ___      _ __
   / __ \_________  / /_____  ____  /  |/  /___ _(_) /
  / /_/ / ___/ __ \/ __/ __ \/ __ \/ /|_/ / __ `/ / / 
 / ____/ /  / /_/ / /_/ /_/ / / / / /  / / /_/ / / /  
/_/   /_/   \____/\__/\____/_/ /_/_/  /_/\__,_/_/_/   
                                                      
    ___                               __ 
   /   | ______________  __  ______  / /_
  / /| |/ ___/ ___/ __ \/ / / / __ \/ __/
 / ___ / /__/ /__/ /_/ / /_/ / / / / /_  
/_/  |_\___/\___/\____/\__,_/_/ /_/\__/  
                                         
   ______                __            
  / ____/_______  ____ _/ /_____  _____
 / /   / ___/ _ \/ __ `/ __/ __ \/ ___/
/ /___/ /  /  __/ /_/ / /_/ /_/ / /    
\____/_/   \___/\__,_/\__/\____/_/     
""" + '\033[0m')

time.sleep(15)

restart = 2
while (restart > 1):
    # Pick an email for Verification. Replace 'YourEmail@Mail.com' with an email adress. (You can use 10min mail for this)
    # verifymail = input('\033[31m' + "Enter Email Adress for Verification: " + '\033[0m')
    verifymail = ''
    # f = open('./input_emails.txt')
    # verifymail = f.readline().trim()
    # verifymail = 'itlammhewuicxfmhco@ttirv.org'

    # Pick an email for Notification. Replace 'YourEmail@Mail.com' with an email adress. (You can use 10min mail for this)
    # notifymail = input('\033[31m' + "Enter Email Adress for Recovery: " + '\033[0m')                           
    notifymail = ''                         
    # notifymail = 'itlammhewuicxfmhco@ttirv.org'
    proxy_status = "false"
    while (proxy_status == "false" and False):

        # Retrieve only 'us' proxies
        proxygrab = collector.get_proxy({'code': ('in')})
        proxy = ("{}:{}".format(proxygrab.host, proxygrab.port))
        print ('\033[31m' + "Proxy:", proxy + '\033[0m')

        try:
            proxy_host = proxygrab.host
            proxy_port = proxygrab.port
            proxy_auth = ":"
            proxies = {'http':'http://{}@{}:{}/'.format(proxy_auth, proxy_host, proxy_port)}
            requests.get("http://example.org", proxies=proxies, timeout=1.5)

        except OSError:
            print ('\033[31m' + "Proxy Connection error!" + '\033[0m')
            time.sleep(1)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K") 
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K") 
            proxy_status = "false"
        else:
            print ('\033[31m' + "Proxy is working..." + '\033[0m')
            time.sleep(1)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K") 
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K") 
            proxy_status = "true"


    else:
        from selenium.webdriver.chrome.options import Options 
        from selenium.webdriver.support.select import Select

        warnings.filterwarnings("ignore", category=DeprecationWarning) 

        options = Options()

        email_driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)

        email_url = 'https://www.guerrillamail.com/'

        email_driver.get(email_url)

        time.sleep(4)

        # # print(driver.find_element_by_id('inbox-id').text)
        email = email_driver.find_element_by_id('inbox-id').text + '@';
        domain_name = Select(email_driver.find_element_by_id('gm-host-select')).first_selected_option.text
        # # domain_name = email_driver.find_element_by_id('gm-host-select').text
        email += domain_name
        # print(domain_name)
        print(email)
        # f = open('./input_emails.txt', 'w')
        # f.write(email)
        
        verifymail = email
        # email_driver.find_element_by_partial_link_text('verification').click()
        # options.add_argument('--proxy-server={}'.format(proxy))

        # Change Path to Chrome Driver Path (or move your ChromeDriver into the project folder)
        driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)

        # url = 'http://protonmail.com/signup'
        url = 'http://account.protonvpn.com/signup'
        #url =


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
            return 'wowmainia'+str(val - 1)

        rngusername = getUserName()
        rngpassword = randomStringDigits(15)

        driver.get(url)

        # time.sleep(10)

        # driver.find_element_by_class_name('pm-button w100 mtauto pm-button--primaryborder').click()
        # driver.find_element_by_link_text("Get Free").click()
        # driver.find_element_by_xpath("/html/body/div[1]/main/main/div/div[4]/div[1]/div[3]/button").click()
        while True:
            try:
                driver.find_element_by_css_selector("body > div.app-root > main > main > div > div:nth-child(5) > div:nth-child(1) > div.flex-item-fluid-auto.pt1.pb1.flex.flex-column > button").click()
                break
            except:
                time.sleep(1)
                continue

        # driver.find_element_by_id('freePlan').click()
        # driver.find_element_by_css_selector("#username").send_keys(rngusername)

        # time.sleep(4)

        # driver.switch_to_frame(0)

        # time.sleep(3)

        # driver.find_element_by_id('username').send_keys(rngusername)

        # time.sleep(1)

        # driver.find_element_by_css_selector("#username").send_keys(rngusername)
        while True:
            try:
                driver.find_element_by_id("username").send_keys(rngusername)
                driver.find_element_by_id("password").send_keys(rngpassword)
                driver.find_element_by_id("passwordConfirmation").send_keys(rngpassword)
                driver.find_element_by_id("email").send_keys(verifymail)
                driver.find_element_by_css_selector("body > div.app-root > main > main > div > div.pt2.mb2 > div > div:nth-child(1) > form > div:nth-child(3) > div > button").click()
                break
            except:
                time.sleep(1)
        # driver.switch_to.default_content()

        # time.sleep(1)

        # driver.find_element_by_id('password').send_keys(rngpassword)

        # time.sleep(1)

        # driver.find_element_by_id('passwordc').send_keys(rngpassword)

        # time.sleep(1)

        # driver.switch_to_frame(1)

        # time.sleep(1)

        # driver.find_element_by_id('notificationEmail').send_keys(notifymail)
        while True:
            try:
                driver.find_element_by_css_selector("body > div.app-root > main > main > div > div.pt2.mb2 > div > div.w100 > div:nth-child(2) > div > div > div:nth-child(2) > form > div:nth-child(2) > button").click()
                break
            except:
                time.sleep(1)
        # time.sleep(60)
        # time.sleep(1)
        # email_driver.find_element_by_partial_link_text('verification').click()
        # email_driver.find_element_by_link_text('notify@protonmail.ch ').click()
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
                time.sleep(1)
        # driver.find_element_by_name('submitBtn').click()

        # time.sleep(6)

        # driver.find_element_by_id('id-signup-radio-email').click()

        # time.sleep(1)

        # driver.find_element_by_id('emailVerification').send_keys(verifymail)

        # time.sleep(1)

        # driver.find_element_by_class_name('codeVerificator-btn-send').click()

        # time.sleep(3)

        print ('\033[31m' + "Your New Email Adress is: ", rngusername,"@protonmail.com", sep='' + '\033[0m')
        print ('\033[31m' + "Your New Email Password is: "  + '\033[0m' , rngpassword)

        complete = "false"

        while (complete == "false"):
            complete_q = input("Did you complete the Verification process? y/n: ")

            if complete_q == "y":
                driver.close()
                csvData = [[verifymail, rngpassword]]
                with open('list.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerows(csvData)
                csvFile.close()
                print ('Great! We added you account details to the table.')
                complete = "true"
            
            else:
                print ('Please try verifing and try again')
                time.sleep(1)
                complete = "false"
        else:
            restart_s = input("Do you want to restart the Script and create more Accounts? y/n: ")
            if restart_s == "y":
                restart ++ 1
                clear()
                print ('\033[31m' + """\
    ____             __              __  ___      _ __
   / __ \_________  / /_____  ____  /  |/  /___ _(_) /
  / /_/ / ___/ __ \/ __/ __ \/ __ \/ /|_/ / __ `/ / / 
 / ____/ /  / /_/ / /_/ /_/ / / / / /  / / /_/ / / /  
/_/   /_/   \____/\__/\____/_/ /_/_/  /_/\__,_/_/_/   
                                                      
    ___                               __ 
   /   | ______________  __  ______  / /_
  / /| |/ ___/ ___/ __ \/ / / / __ \/ __/
 / ___ / /__/ /__/ /_/ / /_/ / / / / /_  
/_/  |_\___/\___/\____/\__,_/_/ /_/\__/  
                                         
   ______                __            
  / ____/_______  ____ _/ /_____  _____
 / /   / ___/ _ \/ __ `/ __/ __ \/ ___/
/ /___/ /  /  __/ /_/ / /_/ /_/ / /    
\____/_/   \___/\__,_/\__/\____/_/     
""" + '\033[0m')

            else:
                print ("Ok! The script is exiting now.")
                time.sleep(1)
                exit()
else:
    print("something")
