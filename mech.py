#!/usr/bin/python

import os,mechanize
from bs4 import BeautifulSoup 
br = mechanize.Browser()
br.open("http://www.snortid.com")

print br.title()

br.select_form(name="frmquery")
br["QueryId"] = "1:234"
response = br.submit()

print response.info()
print response.read()


