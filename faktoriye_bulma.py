print("Faktöriyel Bulma\nÇıkmak için Q/q ya basınız..")
while True:
    sayı=input("Sayı : ")
    if(sayı=="q" or sayı=="Q"):
        print("Program sonlandı..")
        break
    else:
        sayı=int(sayı)
        faktöriyel=1
        for i in range(2,sayı+1):
            faktöriyel*=i
        print("Faktöriyel : ",faktöriyel)