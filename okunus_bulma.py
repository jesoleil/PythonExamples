
birler_bas = ["bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar_bas = ["on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
def okunus_bulma(sayi):

   birler = sayi%10
   onlar = sayi//10
   return onlar_bas[onlar-1]+" "+birler_bas[birler-1]

sayi=int(input("Sayı gir : "))
print(okunus_bulma(sayi))