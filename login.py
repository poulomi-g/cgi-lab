#!/usr/bin/env python3
import cgi
import cgitb

from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http import cookies

cgitb.enable()

print(login_page())

form = cgi.FieldStorage()
username = form.getfirst("username")
password = form.getfirst("password")

cookie = cookies.SimpleCookie().get(os.environ.get('HTTP_COOKIE'))

cookie_username = secret.username
cookie_password = secret.password
if (cookie_username == username and cookie_password == password):
    print("Set-Cookie: loggedin=true")


if username == secret.username and password == secret.password:
    print(secret_page(username, password))

if not username and not password:
    print(login_page())

else: 
    print(after_login_incorrect())