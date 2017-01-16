# -*- coding: utf-8 -*-

import re, urllib
import smtplib
import os

import time

liste = ["Senin Satış Fiyatın", "Senin Alış Fiyatın"]

# size gerekli olan adres
website = urllib.urlopen("http://www.bigpara.com/altin/ceyrek-altin-fiyati")
htmltext = website.read()

# site icinde altin fiyatinin bulundugu alan
altinSatis = '<span class="value dw">(.+?)</span>'
patternSatis = re.compile(altinSatis)
priceSatis = re.findall(patternSatis, htmltext)

altinAlis = '<span class="value up">(.+?)</span>'
patternAlis = re.compile(altinAlis)
priceAlis = re.findall(patternAlis, htmltext)

def definition():
    global satisFiyati, alisFiyati, satirBasi
    satisFiyati, alisFiyati = 0
    satirBasi = "\n"


def satirBasiFunc():
    satirBasi = "\n"
    return satirBasi


def satisSonDurum():
    j = 0
    for s in priceSatis:
        satisFiyati = liste[j] + " : " + s
    return satisFiyati


def alisSonDurum():
    j = 1
    for a in priceAlis:
        alisFiyati = liste[j] + "   : " + a
    return alisFiyati


os.getcwd()
gununDegerleri = open("Bes_Dakikalik_Degerler.txt", "w")

#gununDegerleri.write("Senin Satış Fiyatın" "     " "Senin Alış Fiyatın")

#gununDegerleri.write(satirBasiFunc() + str(satisSonDurum()) + satirBasiFunc() + str(alisSonDurum()))

gununDegerleri = open("/C:/Users/MONSTER/PycharmProjects/FirstProject/FirstPackage/Bes_Dakikalik_Degerler.txt", "r")
print (gununDegerleri.read())

time.sleep(1)

gununDegerleri = open("Bes_Dakikalik_Degerler.txt", "a")
gununDegerleri.write(satirBasiFunc() + str(satisSonDurum()) + "           " + str(alisSonDurum()))

gununDegerleri = open("Bes_Dakikalik_Degerler.txt", "r")
print (gununDegerleri.read())


gununDegerleri.close()

i = 0
while i < 100:
    website = urllib.urlopen("http://www.bigpara.com/altin/ceyrek-altin-fiyati")
    htmltext = website.read()

    # site icinde altin fiyatinin bulundugu alan
    altinSatis = '<span class="value dw">(.+?)</span>'
    patternSatis = re.compile(altinSatis)
    priceSatis = re.findall(patternSatis, htmltext)

    altinAlis = '<span class="value up">(.+?)</span>'
    patternAlis = re.compile(altinAlis)
    priceAlis = re.findall(patternAlis, htmltext)


    def definition():
        global satisFiyati, alisFiyati, satirBasi
        satisFiyati, alisFiyati = 0
        satirBasi = "\n"


    def satirBasiFunc():
        satirBasi = "\n"
        return satirBasi


    def satisSonDurum():
        j = 0
        for s in priceSatis:
            satisFiyati = liste[j] + " : " + s
        return satisFiyati


    def alisSonDurum():
        j = 1
        for a in priceAlis:
            alisFiyati = liste[j] + "   : " + a
        return alisFiyati

    print (satirBasiFunc() + satisSonDurum() + "           " + alisSonDurum())
    i = i + 1
    time.sleep(1)
