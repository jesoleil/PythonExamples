class Kitap():
    def __init__(self,isim,yazar,sayfa,tur):
        self.isim=isim
        self.yazar=yazar
        self.sayfa=sayfa
        self.tur=tur
    def __str__(self):
        return "İsim : {}\nYazar : {}\nSayfa Sayısı : {}\nTürü : {}".format(self.isim,self.yazar,self.sayfa,self.tur)
    def __len__(self):
        return self.sayfa
    def __del__(self):
        print("Kitap Objesi Silindi...")

kitap1=Kitap("Böyle Buyurdu Zerdüşt","Friedrich Nietzsche",380,"Felsefi Kurgu")
print("Kitap Özellikleri")
print(kitap1)
print("Len fonksiyonu çağırıldı : ")
print(len(kitap1))
del kitap1
