# -*- coding: utf-8 -*-

#Kutuphaneler

import re, urllib
import smtplib
import os
import time
from lxml import html
import requests

#Kodlar

liste = ["Senin Satis Fiyatin", "Senin Alis Fiyatin"]
print liste[0] + "      " + liste[1]
print "-"*len(liste[0]) + "      " + "-"*len(liste[1])

x = 0

while x < 10:
    page = requests.get('http://www.bigpara.com/altin/ceyrek-altin-fiyati')
    tree = html.fromstring(page.content)
    altinSatis = tree.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[2]/span[2]/text()')
    altinAlis = tree.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[3]/span[2]/text()')

    def satisSonDurum():
        j = 0
        satisFiyati = altinSatis[j]
        return satisFiyati

    def alisSonDurum():
        i = 0
        alisFiyati = altinAlis[i]
        return alisFiyati

    print satisSonDurum() + "                   " + alisSonDurum()

    x = x + 1

    time.sleep(2)
