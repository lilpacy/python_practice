# coding: UTF-8
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time

f = open('madomagi_miku_sumiyoshi.csv','a')
writer = csv.writer(f,lineterminator='\n')

csv_list = []

time_ = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
csv_list.append(time_)

# アクセスするURL
url = 'https://daidata.goraggio.com/100433/unit_list?hist_num=1&model=SLOT%E9%AD%94%E6%B3%95%E5%B0%91%E5%A5%B3%E3%81%BE%E3%81%A9%E3%81%8B%E2%98%86%E3%83%9E%E3%82%AE%E3%82%AB&ballPrice=20.00&disp=1&graph=1'

try:
    # htmlオブジェクトが返ってくる
    print('httpリクエストの送信')
    html = urllib.request.urlopen(url)

    # htmlをBeautifulSoupで扱い、htmlタグのかたまりが返ってくる
    soup = BeautifulSoup(html, "html.parser")
    td = soup.find_all("td")

    i = 0
    for tag in td:
        if tag.a != None:
            csv_list.append(tag.a.string)
        elif tag.string != None:
            csv_list.append(tag.string)
        i += 1
        if i == 12:
            print(csv_list)
            writer.writerow(csv_list)
            i = 0
            csv_list = []
            time_ = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            csv_list.append(time_)
except:
    pass

f.close()
