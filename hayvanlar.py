class Hayvan():
    def __init__(self,sube,sinif,takim,aile,cins,tur,adet):
        self.sube=sube
        self.sinif=sinif
        self.takim=takim
        self.aile=aile
        self.cins=cins
        self.tur=tur
        self.adet=adet
    def eklemeYap(self,sayi):
        self.adet += sayi
    def __str__(self):
        return "HAYVANLAR ALEMİ\nŞube: {}\nSınıf: {}\nTakım: {}\nAile: {}\nCins: {}\nTür: {}\nAdet: {}".format(self.sube,self.sinif,self.takim,self.aile,self.cins,self.tur,self.adet)
    def __len__(self):
        return self.adet
class Kopek(Hayvan):
    def __init__(self,sube,sinif,takim,aile,cins,tur,adet,gelismis_ozellik):
        super().__init__(sube,sinif,takim,aile,cins,tur,adet)
        self.gelismis_ozellik=gelismis_ozellik
    def __str__(self):
        return "HAYVANLAR ALEMİ\nŞube: {}\nSınıf: {}\nTakım: {}\nAile: {}\nCins: {}\nTür: {}\nAdet: {}\nGelişmiş Özellik: {}".format(self.sube,self.sinif,self.takim,self.aile,self.cins,self.tur,self.adet,self.gelismis_ozellik)
class Kus(Hayvan):
    def __init__(self,sube,sinif,takim,aile,cins,tur,adet,renk):
        super().__init__(sube,sinif,takim,aile,cins,tur,adet)
        self.renk=renk
    def __str__(self):
        return "HAYVANLAR ALEMİ\nŞube: {}\nSınıf: {}\nTakım: {}\nAile: {}\nCins: {}\nTür: {}\nAdet: {}\nRenk: {}".format(self.sube,self.sinif,self.takim,self.aile,self.cins,self.tur,self.adet,self.renk)
class At(Hayvan):
    def __init__(self,sube,sinif,takim,aile,cins,tur,adet,fiyat):
        super().__init__(sube,sinif,takim,aile,cins,tur,adet)
        self.fiyat=fiyat
    def __str__(self):
        return "HAYVANLAR ALEMİ\nŞube: {}\nSınıf: {}\nTakım: {}\nAile: {}\nCins: {}\nTür: {}\nAdet: {}\nFiyat: {}".format(self.sube,self.sinif,self.takim,self.aile,self.cins,self.tur,self.adet,self.fiyat)
    def fiyatDegistir(self,yeni_fiyat):
        self.fiyat=yeni_fiyat


hayvan=Hayvan("Bilgi Yok","Bilgi Yok","Bilgi Yok","Bilgi Yok","Bilgi Yok","Bilgi Yok","Bilgi Yok")
kopek1=Kopek("Kordalılar","Memeliler","Etçiller","Köpekgiller","Canis Lupus","Canis Lupu Familiaris",5,"Koku Alma")
kus1=Kus("Kordalılar","Aves","Passeriformes","Fringillidae","Cardinalis","Cardinalis Cardinalis",12,"Kırmızı-Beyaz")
at1=At("Kordalılar","Memeliler","Perissodactyla","Equiedae","Equus","Equus Caballus",8,17900)

print("""
HAYVANLAR ALEMİNE HOŞGELDİNİZ
1.KÖPEK
2.KUŞ
3.AT
ÇIKMAK İÇİN q YA DA Q YA BASINIZ..
""")

while True:
    secim=input("Seçiminiz : ")
    if(secim=="1"):
        print(kopek1)
        print("Hayvan Sayısı : ",len(kopek1))
        ekle=int(input("Kaç tane eklemek istersiniz ? : "))
        kopek1.eklemeYap(ekle)
        print("Güncellenmiş hayvan sayısı : ",len(kopek1))
    elif(secim=="2"):
        print(kus1)
        print("Hayvan Sayısı : ", len(kus1))
        ekle = int(input("Kaç tane eklemek istersiniz ? : "))
        kus1.eklemeYap(ekle)
        print("Güncellenmiş hayvan sayısı : ", len(kus1))
    elif(secim=="3"):
        print(at1)
        print("Hayvan Sayısı : ", len(at1))
        ekle = int(input("Kaç tane eklemek istersiniz ? : "))
        at1.eklemeYap(ekle)
        print("Güncellenmiş hayvan sayısı : ", len(at1))
        para=int(input("Yeni fiyatı belirleyiniz : "))
        at1.fiyatDegistir(para)
        print("Fiyat değiştirildi ..")
        print(at1)
    elif(secim=="q" or secim=="Q"):
        print("Programdan çıktınız..")
        break
    else:
        print("Hatalı Tuş !! ")






