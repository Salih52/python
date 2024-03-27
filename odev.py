class Personel:
    def __init__(self, adi, departmani, çalisma_yili, maasi):
        self.adi = adi
        self.departmani = departmani
        self.çalisma_yili = çalisma_yili
        self.maasi = maasi

class Firma:
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        for personel in self.personel_listesi:
            print("adi:", personel.adi)
            print("Departmanidepartmani:", personel.departmani)
            print("Çalışma Yılı:", personel.çalisma_yili)
            print("Maasi:", personel.maasi)
            print()

    def maaş_zammi(self, personel, zam_orani):
        for p in self.personel_listesi:
            if p == personel:
                p.maasi += p.maasi * (zam_orani / 100)

    def personel_cikart(self, personel):
        self.personel_listesi.remove(personel)

personel1 = Personel("Ali", "Muhasebe", 5, 3000)
personel2 = Personel("Veli", "İnsan Kaynakları", 3, 2500)
personel3 = Personel("Ayşe", "Pazarlama", 2, 2000)




firma1 = Firma()


print("Personel Listesi")
firma1.personel_ekle(personel1)
firma1.personel_ekle(personel2)
firma1.personel_listele()

print("Zamlı Personel Listesi")
firma1.maaş_zammi(personel1,10)
firma1.maaş_zammi(personel2,20)
firma1.personel_listele()

print("Personel çıkarıldıktan sonraki Personel Listesi")
firma1.personel_cikart(personel2)
firma1.personel_listele()