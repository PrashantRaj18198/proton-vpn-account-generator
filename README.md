# ProtonVPN Account Creator


## Getting Started

This script can create ProtonVPN using Python and Selenium

### Prerequisites

You need python 3 installed on your System.

```
pip install -r requirements.txt 
```
You need chromedriver
#### Download chromedriver from
https://chromedriver.chromium.org/downloads

After that you can proceed to edit the Script.

### Edit Script

Open emails.py with any TextEditor.

Find and replace 'wowmania' with a random word of your choice

## Running 🏃🏽‍♂️

### Create new account

```
python3 emails.py #slower
python3 cleaned_emails.py #faster
```

### Fetch openVPN credentials
```
python3 getOpenVPNUsernamePassword.py
```

### Change details to protonvpn-cli
* [protonvpn-cli](https://github.com/ProtonVPN/protonvpn-cli-ng)
Note: A protonvpn profile must be in place since the script uses `sudo protonvpn configure`. Use `sudo protonvpn init` to create one.
```
python3 script.py
```

## Built With

* [Selenium-Python](https://selenium-python.readthedocs.io/) - Tool for browser automation

## Authors

* **Hendrik Bgr** - *Initial work* - [HendrikBgr](https://github.com/hendrikbgr)
* **Prashant Raj** - *Verification Added* - [PrashantRaj](https://github.com/PrashantRaj18198)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration

## To Do List 📝

* Add random username and password. ✅
* Print account details to in console ✅
* Add more information to console when running ✅
* Create requirements.txt file for easy installation ✅
* Verification email ✅


