import sqlite3
import os

print "\n" + (sqlite3.version) + "\n"

database_name = "veriler.db"
baglanti = sqlite3.connect('veriler.db')

if not os.path.isfile(database_name):

    print "Database olusturulmamis, simdi olusturuyorum..."

    baglanti = sqlite3.connect('veriler.db')

    # baglanti kurulan veriyi sec.
    veritabani_sec = baglanti.cursor()

    try:
        # secili veritabanina sql sorgu yolluyoruz.
        veritabani_sec.execute('''
        CREATE TABLE ceyrekAltin(
        kayit_no INTEGER PRIMARY KEY,
        satis_fiyati INTEGER NOT NULL ,
        alis_fiyati INTEGER NOT NULL ,
        yuzde_degisim INTEGER NOT NULL)
        ''')
    except sqlite3.OperationalError, msg:
        print "Bir Database hatasi olustu."

#if (baglanti):
#    print("***Database baglantisi basarili bir sekilde gerceklesti.") + "\n"
#else:
#    print("!!!Database baglantisi basarisiz oldu!")

#baglanti kurulan veriyi sec.
veritabani_sec = baglanti.cursor()

veritabani_sec.execute('''
INSERT INTO ceyrekAltin
(satis_fiyati,alis_fiyati,yuzde_degisim)
VALUES ('235,81','241,70','4,08 %')
''')

baglanti.commit()

oku = veritabani_sec.execute('SELECT * FROM ceyrekAltin')
print(oku.fetchall())

baglanti.commit()
baglanti.close()