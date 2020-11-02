class Yazilimci():
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maas=maas
        self.diller=diller
    def bilgileriGoster(self):
        print("""ÇALIŞAN BİLGİSİ
        İsim : {}
        Soyisim : {}
        Numara : {}
        Maaş : {}
        Bildiği Diller : {} 
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))
    def dilEkle(self,yeni_dil):
        print("Yeni dil eklendi..")
        self.diller.append(yeni_dil)
    def zamYap(self,zam_miktari):
        print("Zam yapıldı..")
        self.maas += zam_miktari

class Yonetici(Yazilimci):
    def ekUcret(self,bonus):
        print("Ek ücret maaşa eklendi...")
        self.maas+=bonus

class Sorumlu(Yazilimci):
    def __init__(self,isim,soyisim,numara,maas,diller,kisi_sayisi):
        super().__init__(isim,soyisim,numara,maas,diller)
        self.kisi_sayisi=kisi_sayisi
    def bilgileriGoster(self):
        print("""ÇALIŞAN BİLGİSİ
        İsim : {}
        Soyisim : {}
        Numara : {}
        Maaş : {}
        Bildiği Diller : {} 
        Sorumlu Olduğu Kişi Sayısı : {}
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller,self.kisi_sayisi))


yazilimci1=Yazilimci("Soley","Çapar",150518057,3000,["C","C#","Python"])
yazilimci1.bilgileriGoster()
yazilimci1.dilEkle("JavaScript")
yazilimci1.zamYap(450)
yazilimci1.bilgileriGoster()
yonetici1=Yonetici("Nil","Çapar",150518058,4500,["Java","MySql","Ruby"])
yonetici1.bilgileriGoster()
yonetici1.dilEkle("C++")
yonetici1.ekUcret(1050)
yonetici1.bilgileriGoster()
sorumlu1=Sorumlu("Sabahattin","Çapar",150518059,5150,["C","C++","C#","Java","Ruby","Python"],7)
sorumlu1.bilgileriGoster()
sorumlu1.zamYap(970)
sorumlu1.bilgileriGoster()

