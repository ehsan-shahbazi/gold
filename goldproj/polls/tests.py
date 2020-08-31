from django.test import TestCase
import bs4, sys
from urllib import request
import requests
"""
r = requests.get('http://sekehbartar.com/', timeout=(3.05, 27))
print(r.text)
soup = bs4.BeautifulSoup(r.text, 'html.parser')
print(soup)
# bs4.BeautifulSoup.s
print(soup.findAll('td'))

for node in soup.findAll('article'):
    print(node.findAll('h2')[0].getText())
    print(str(node.findAll('a')[0])[9:37])
    # bs4.BeautifulSoup.getText"""
# Create your tests here.

from bs4 import BeautifulSoup
from selenium import webdriver
import os
import smtplib
import ssl
"""
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "meshahbazi72@gmail.com"  # Enter your address
receiver_email = "meshahbazi72@gmail.com"  # Enter receiver address
password = "QIwueyrt18273645"
message = "Hello i want to see you ehsan"

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

"""

"""print(os.path)
url = "https://www.sekehsarmayeh.com/"
page = request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
a = soup.find(id='ctl12_ctl16_ctl00_PriceList1_gvList')
b = a.find(text="سکه ربع ( زير 86 )").findNext()
print(a)
# print()
c = b.findNext()
d = c.findNext()
# print(b.findNext())
print()
# print(d.getText())
k = d.getText()
k = k.replace(',', '')
k = int(k)
print(k)
a = [1, 2, 3]
a.reverse()
print(a)"""
"""
import time
import pandas as pd
driver = webdriver.Chrome(executable_path="../goldproj/chromedriver/chromedriver")
print(driver)
my_pd = pd.read_csv('urls.csv', sep="---")
print(my_pd.head(1))
print('hi')
for item in my_pd:
    print(item)
    driver.get(item)
    time.sleep(10)
    elem = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/md-content/div/div/div[2]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]/i")

    elem.click()
"""
a = '13402415'
a = a[:-6] + ',' + a[-6:-3] + ',' + a[-3:]
a = a.replace('1', '۱')
a = a.replace('2', '۲')
a = a.replace('3', '۳')
a = a.replace('4', '۴')
a = a.replace('5', '۵')
a = a.replace('6', '۶')
a = a.replace('7', '۷')
a = a.replace('8', '۸')
a = a.replace('9', '۹')
a = a.replace('0', '۰')
print(a)