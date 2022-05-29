# lab-username-enumeration-via-account-lock

Python script for username enumeration and credential stuffing against Portswigger Web Security Academy lab.

```
pip install requests bs4
```

Update `url` using a fresh lab from https://portswigger.net/web-security/authentication/password-based/lab-broken-bruteforce-protection-ip-block

Save usernames and passwords to text files in working directory. Copy and paste from:
 - https://portswigger.net/web-security/authentication/auth-lab-usernames
 - https://portswigger.net/web-security/authentication/auth-lab-passwords

Simply run the script with

```
python3 fuzz.py
``` 

The `enumerate_username()` function is used to make 5 requests using the same username and password in an attempt to trigger a lockout. Note that the error message of the response will change when a valid username is found.

Once the username is captured, comment out the `enumerate_username()` function and uncomment `brute_force_user_account()`. Set the username param and run the script again. When no error message is detected you'll see "No warning detected, valid credential found?". 

Wait 60 seconds before using the credential to login and solve the lab.
