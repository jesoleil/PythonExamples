import random
import time

class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["TRT"],kanal="TRT"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal

    def tvAc(self):
        if(self.tv_durum=="Açık"):
            print(">> Televizyon zaten açık !!")
        else:
            print(">> Televizyon açılıyor !! ")
            time.sleep(1)
            self.tv_durum="Açık"
    def tvKapat(self):
        if (self.tv_durum == "Kapalı"):
            print(">> Televizyon zaten kapalı !!")
        else:
            print(">> Televizyon kapanıyor !! ")
            time.sleep(1)
            self.tv_durum = "Kapalı"
    def sesAyarları(self):
        while True:
            cevap=input("Sesi azatmak için '<' : \nSesi arttırmak için '>' : \nÇıkış için 'çık' : ")
            if(cevap=="<"):
                if(self.tv_ses!=0):
                    self.tv_ses -=1
                    print(">> Ses : ",self.tv_ses)
            elif(cevap==">"):
                if(self.tv_ses!=31):
                    self.tv_ses +=1
                    print(">> Ses : ",self.tv_ses)
            else:
                print(">> Ses güncellendi !! : ",self.tv_ses)
                break
    def kanalEkle(self,kanal_adi):
        print(">> Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_adi)
        print(">> Kanal eklendi !!")
    def rastgeleKanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print(">> Şu anki kanal : ",self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "**********\nTv Durumu : {}\nTv Ses : {}\nKanal Listesi : {}\nAçık Olan Kanal : {}\n**********".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)


kumanda=Kumanda()

print("""
TELEVİZYON UYGULAMASI
1.TV AÇ
2.TV KAPAT
3.SES AYARLARI
4.KANAL EKLE
5.KANAL SAYISINI ÖĞREN
6.RASTGELE KANAL AÇ
7.TELEVİZYON BİLGİLERİNİ GÖSTER
ÇIKMAK İÇİN 'q' YA DA 'Q' YA BASIN
""")

while True:
    islem=input("**** İslemi giriniz : ")
    if(islem=="q" or islem=="Q"):
        print(">> Program sonlandırılıyor ...")
        time.sleep(2)
        break
    elif(islem=="1"):
        kumanda.tvAc()
    elif(islem=="2"):
        kumanda.tvKapat()
    elif(islem=="3"):
        kumanda.sesAyarları()
    elif(islem=="4"):
        kanal_adları=input("Kanal isimlerini virgül ile ayırarak giriniz : ")
        kanal_listesi=kanal_adları.split(",")
        for eklenen in kanal_listesi:
            kumanda.kanalEkle(eklenen)
    elif(islem=="5"):
        print(">>Kanal sayısı : ",len(kumanda))
    elif(islem=="6"):
        kumanda.rastgeleKanal()
    elif(islem=="7"):
        print(kumanda)
    else:
        print("GEÇERSİZ İŞLEM YAPTINIZ !!")




