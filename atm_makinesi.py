print("ATM MAKİNESİNE HOŞGELDİNİZ")
print("1.Bakiye Sorgulama\n2.Para Yatırma\n3.Para Çekme")
print("Programdan çıkmak için F tuşuna basınız..")

bakiye=1000
while True:
    işlem=input("İşlemi giriniz :")
    if(işlem=="F" or işlem=="f"):
        print("Yine bekleriz..")
        break
    elif(işlem=="1"):
        print("Bakiyeniz {} TL dir..".format(bakiye))

    elif(işlem=="2"):
        miktar=int(input("Yatırılacak miktarı giriniz :"))
        bakiye+=miktar

    elif(işlem=="3"):
        miktar=int(input("Çekilecek miktarı giriniz :"))
        if(bakiye<miktar):
            print("Hesabınızdaki para yetersiz !!!")
            continue
        bakiye-=miktar

    else:
        print("Geçersiz işlem !!!")


