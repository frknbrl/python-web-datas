#-*- coding: utf-8 -*-

import re , urllib
import smtplib
import os

liste=["Senin Satış Fiyatın","Senin Alış Fiyatın"]

# size gerekli olan adres
website=urllib.urlopen("http://www.bigpara.com/altin/ceyrek-altin-fiyati")
htmltext=website.read()

# site icinde altin fiyatinin bulundugu alan
altinSatis='<span class="value dw">(.+?)</span>'
patternSatis=re.compile(altinSatis)
priceSatis=re.findall(patternSatis,htmltext)

altinAlis='<span class="value up">(.+?)</span>'
patternAlis=re.compile(altinAlis)
priceAlis=re.findall(patternAlis,htmltext)

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

def dosyalama():

    os.getcwd()
    gununDegerleri = open("Bes_Dakikalik_Degerler.txt", "w")

    gununDegerleri.write(satirBasiFunc() + str(satisSonDurum()) + satirBasiFunc() + str(alisSonDurum()))

    gununDegerleri.close()


#    j = 0
#    for s in priceSatis:
#       print liste[j] + " : " + s
#        j = j + 1
#        for a in priceAlis:
#           print liste[j] + "  : " + a

#Sunucu ile bağlantıyı kuran fonksiyonu tanımladık.
def baglan():
    sunucu = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    sunucu.login("furkanbiroll@gmail.com","48586745366_f")
    return sunucu

def mailgonder():
    sunucu = baglan()

    gonderici = "furkanbiroll@gmail.com"
    alici = "furkanbirol1905@gmail.com"
    konu = "Altında Son Duum"
    icerik = satirBasiFunc() + str(satisSonDurum()) + satirBasiFunc() + str(alisSonDurum())

    mail = """
            Gönderen:   %s
            Konu:       %s
            Mesaj:      %s
    """ % (gonderici,konu,icerik)

    try:
        #maili gönderiyoruz. Aldığı parametreler gonderenin mail adresi, alıcının mail adresi, ve mail içeriği
        sunucu.sendmail(gonderici,alici,mail)
        print "Mail basarili bir sekilde gonderildi."
    except EOFError:
        print "Mail gonderilirken hata olustu."

    sunucu.quit()

#mail gönder fonksiyonunu çağırdık
mailgonder()