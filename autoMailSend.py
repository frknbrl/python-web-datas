# -*- coding:utf-8 -*-
import smtplib


#server = smtplib.SMTP("smtp.google.com",587)

#Kullanıcıdan alıcağımız veriler için fonksiyon tanımladık
#def giris(kelime):
#    return raw_input(kelime).strip()

#Sunucu ile bağlantıyı kuran fonksiyonu tanımladık.
def baglan():
    sunucu = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    sunucu.login("furkanbiroll@gmail.com","48586745366_f")
    return sunucu

def mailgonder():
    sunucu = baglan()

    #gonderici = giris("Maili gönderenin mail adresi:")
    #alici = giris("Maili alanın mail adresi:")

    #konu = giris("Mailin konusu:")
    #icerik = giris("Mailin içeriği:")

    gonderici = "furkanbiroll@gmail.com"
    alici = "furkanbirol1905@gmail.com"
    konu = "Python'dan Haber Var!!!!"
    icerik = "Python bos durmuyor kanka"


    mail = """
            Gönderen:   %s
            Konu:       %s
            Mesaj:      %s
    """ % (gonderici,konu,icerik)

    try:
        #maili gönderiyoruz. Aldığı parametreler gonderenin mail adresi, alıcının mail adresi, ve mail içeriği
        sunucu.sendmail(gonderici,alici,mail)
        print "Mail başarılı bir şekilde gönderildi."
    except EOFError:
        print "Mail gönderilirken hata oluştu."

    sunucu.quit()

#mail gönder fonksiyonunu çağırdık
mailgonder()