import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import csv
import sys
import numpy as np


def get_past():
    for item in ['geram18', 'sekee', 'platinum']:
        the_url = 'https://www.tgju.org/chart/' + item + '/2'
        print('_item_' * 10, '\n', item)
        kind = 'td'
        the_id = "DataTables_Table_0"
        response = requests.get(url=str(the_url))
        page = response.content
        soup = BeautifulSoup(page, 'html.parser')
        my_object = [x.getText() for x in soup.find_all(kind)]
        location = "./chromedriver/chromedriver"
        driver = webdriver.Chrome(executable_path='./chromedriver/chromedriver')
        driver.get(the_url)

        # click radio button
        results = []
        i = 0
        the_last = 800
        for _ in range(800):
            i += 1
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            my_object = [x.getText().replace(',', '') for x in soup.find_all(kind)]

            results.append(my_object)
            sys.stdout.write('\r' + str(i * 100 / the_last) + '% completed.')
            sys.stdout.flush()
            a = driver.find_elements_by_xpath("/html/body")
            for _ in range(3):
                a[0].send_keys(Keys.PAGE_UP)
            a[0].send_keys(Keys.PAGE_DOWN)
            a[0].send_keys(Keys.PAGE_DOWN)
            button = driver.find_elements_by_xpath('//*[@id="DataTables_Table_0_next"]')[0]
            if i == 1:
                last = driver.find_elements_by_xpath('//*[@id="DataTables_Table_0_paginate"]/span/a[6]')[0]
                time.sleep(0.5)
                the_last = int(last.text)
                print(the_last)
            if i >= the_last:
                break
            time.sleep(0.5)
            button.click()
            time.sleep(1)

        file_name = item + '.csv'

        with open('/polls/' + file_name, 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(results)


def save_past(file_name):
    with open(file_name) as file:
        data = file.readline()
        # print(data)
        data = data.split(',')
        for i in range(int(len(data) / 7)):
            print(int(data[7 * i]), data[7 * i + 5])
        input()


# save_past('../polls/sekee.csv')
"""
a = [1, 22, 3, 4, 5, 2, 4]
d = np.histogram(a, bins=100, density=True)
print(d[0])
"""