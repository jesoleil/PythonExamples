print("1 den 100 e kadar olan çift sayılar : ")
liste1 = range(1,101)
liste2 = [i for i in liste1 if (i%2==0)]
print(liste2)