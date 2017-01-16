# -*- coding: utf-8 -*-

#Kutuphaneler

import re, urllib
import smtplib
import os
import time

import datetime
from lxml import html
import requests

#Kodlar

an = datetime.datetime.now()

liste = ["Senin Satis Fiyatin", "Senin Alis Fiyatin", "Yuzde Degisim (%)"]

if os.path.exists(r"C:\Users\MONSTER\PycharmProjects\FirstProject\FirstPackage\Altin_Durum_Izleme_DB.txt"):

    print "\n\n" + """'Altin_Durum_Izleme_DB.txt' dosyasi bulundu, okuyorum...'"""
    print open(r"C:\Users\MONSTER\PycharmProjects\FirstProject\FirstPackage\Altin_Durum_Izleme_DB.txt").read()

else:

    print """'Altin_Durum_Izleme_DB.txt' dosyasi belirtilen path'de bulunamadı, simdi olusturuyorum...'"""

    os.getcwd()
    gununDegerleri = open(r"C:\Users\MONSTER\PycharmProjects\FirstProject\FirstPackage\Altin_Durum_Izleme_DB.txt", "w")
    gununDegerleri.write("\n         ###Ceyrek Altin Durum Izleme Programi###\n\n             ###Designed by Furkan Birol###\n\n")

gununDegerleri = open(r"C:\Users\MONSTER\PycharmProjects\FirstProject\FirstPackage\Altin_Durum_Izleme_DB.txt", "a")
gununDegerleri.write("\n\n" + "********************* " + datetime.datetime.strftime(an, '%d %B %Y') + " **********************" + "\n\n")
gununDegerleri.write(liste[0] + "   " + liste[1] + "   " + liste[2] + "\n" + "-"*len(liste[0]) + "   " + "-"*len(liste[1]) + "   " + "-"*len(liste[2]))
gununDegerleri.close()

#print "\n         ###Ceyrek Altin Durum Izleme Programi###\n\n             ###Designed by Furkan Birol###\n\n"
print "\n" + "********************* " + datetime.datetime.strftime(an, '%d %B %Y') + " **********************" + "\n"
print liste[0] + "   " + liste[1] + "   " + liste[2]
print "-"*len(liste[0]) + "   " + "-"*len(liste[1]) + "   " + "-"*len(liste[2])

x = 0

while x < 5:
    pageCeyrekAltin = requests.get('http://www.bigpara.com/altin/ceyrek-altin-fiyati')
    treeCeyrekAltin = html.fromstring(pageCeyrekAltin.content)
    ceyrekAltinSatis = treeCeyrekAltin.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[2]/span[2]/text()')
    ceyrekAltinAlis = treeCeyrekAltin.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[3]/span[2]/text()')
    ceyrekAltinYuzdeDegisim = treeCeyrekAltin.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[4]/span[3]/text()')

    def ceyrekAltinSatisSonDurum():
        j = 0
        ceyrekAltinSatisFiyati = ceyrekAltinSatis[j]
        return ceyrekAltinSatisFiyati

    def ceyrekAltinAlisSonDurum():
        i = 0
        ceyrekAltinAlisFiyati = ceyrekAltinAlis[i]
        return ceyrekAltinAlisFiyati

    def ceyrekAltinYuzdeSonDurum():
        k = 0
        ceyrekAltinYuzdelikDegisim = ceyrekAltinYuzdeDegisim[k]
        return ceyrekAltinYuzdelikDegisim

    gununDegerleri = open(r"C:\Users\MONSTER\PycharmProjects\FirstProject\FirstPackage\Altin_Durum_Izleme_DB.txt", "a")
    gununDegerleri.write("\n      " + ceyrekAltinSatisSonDurum() + "                " + ceyrekAltinAlisSonDurum() + "              " + ceyrekAltinYuzdeSonDurum())
    gununDegerleri.close()

    print "      " + ceyrekAltinSatisSonDurum() + "                " + ceyrekAltinAlisSonDurum() + "              " + ceyrekAltinYuzdeSonDurum()

    x = x + 1

    time.sleep(2)
