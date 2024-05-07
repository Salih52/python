import sqlite3

def create_database():
    conn = sqlite3.connect('metinler.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS metinler (id INTEGER PRIMARY KEY, metin TEXT)''')
    conn.commit()
    conn.close()

def insert_metin(metin):
    conn = sqlite3.connect('metinler.db')
    c = conn.cursor()
    c.execute('''INSERT INTO metinler (metin) VALUES (?)''', (metin,))
    conn.commit()
    conn.close()


metin1 = input("İlk metni girin: ")
metin2 = input("İkinci metni girin: ")


create_database()
insert_metin(metin1)
insert_metin(metin2)

benzerKelimeler = set()

def jaccard_hesapla(metin1, metin2):
    
    set1 = set(metin1.split())
    set2 = set(metin2.split())
    
     
    
    for kelime in set1:
       if kelime in set2:
           benzerKelimeler.add(kelime)
    
    
    birlesim = len(set1) + len(set2) - (len(benzerKelimeler) * 2)
    kesisim = len(benzerKelimeler)
    oran = kesisim / birlesim 
    
    
    return oran


benzerlik_orani = jaccard_hesapla(metin1, metin2)


def yazdırma(benzerlik_orani):
    with open('benzerlikDurumu.txt', 'w') as file:
        if benzerlik_orani >= 0.5:
            result = "Metinler birbirine benziyor."
        else:
            result = "Metinler birbirine benzemiyor."
        print("Benzerlik Durumu: " + result + "Oran:" + str(benzerlik_orani))
        file.write("Benzerlik Durumu: " + result + "   Oran:" + str(benzerlik_orani) + "\n")
        file.write("Benzer Kelimeler: \n")
        print("Benzer Kelimeler: ")
        for kelime in benzerKelimeler:
            print(kelime)
            file.write(kelime + "\n")

# Sonuçları yazdır
yazdırma(benzerlik_orani)
