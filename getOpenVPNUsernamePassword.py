from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

f = open('./list.csv')
lines = f.readlines()
end = len(lines) - 1
try:
    while lines[end] == '':
        end -= 1
except IndexError:
    print("No username and password found in list.csv")
    exit(-1)

username, password = lines[end].strip().split(', ')

login_url = 'https://account.protonvpn.com/login'
account_url = 'https://account.protonvpn.com/account'
driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=Options())

# driver = webdriver.Firefox(executable_path='./geckodriver', firefox_options=Options())
driver.get(login_url)

wait = WebDriverWait(driver, 60)

try:
    loginElement = wait.until(EC.presence_of_element_located((By.ID, 'login')))
    passwordElement = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    loginElement.send_keys(username)
    passwordElement.send_keys(password)
    buttonElement = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.app-root > main > div > div > div > div > form > div.flex.flex-spacebetween > button.pm-button.pm-button--primary')))
    buttonElement.click()
except:
    print('In first try/except')
    print("Timed Out. Now Exiting")
    exit(-1)

try:
    account = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.app-root > div.flex.flex-nowrap.no-scroll > div > div > div.sidebar.flex.flex-column.noprint > nav > ul > li:nth-child(2) > a')))
    account.click()
    time.sleep(1)
    print('Account found')

    username = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.app-root > div.flex.flex-nowrap.no-scroll > div > div > div.main.flex-item-fluid.main-area > div > main > div > section:nth-child(8) > div:nth-child(3) > div.pm-field-container > div > code')))
    username = username.text
    print('username found', username)

    showButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.app-root > div.flex.flex-nowrap.no-scroll > div > div > div.main.flex-item-fluid.main-area > div > main > div > section:nth-child(8) > div:nth-child(4) > div.ml1.flex-item-noshrink.onmobile-ml0.onmobile-mt0-5 > button.pm-button.pm-button--for-icon > svg')))
    showButton.click()
    print('show password button found')
    
    password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.app-root > div.flex.flex-nowrap.no-scroll > div > div > div.main.flex-item-fluid.main-area > div > main > div > section:nth-child(8) > div:nth-child(4) > div.pm-field-container > div > code'))).text
    print('password found', password)

    f = open('openVPNUsernamePassword.txt', 'a')
    f.write(username + ', ' + password + '\n')
    f.close()
    print('Username and Password written to openVPNUsernamePassword.txt')
except:
    print('In second try/except')
    print("Timed Out. Bad Luck Mate")
finally:
    print('Executed without exceptions. Now exiting')
    driver.quit()
