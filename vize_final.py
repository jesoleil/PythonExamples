print("*****NOT HESAPLAMA*****")
vize1=int(input("Birinci vize notu : "))
vize2=int(input("İkinci vize notu : "))
final=int(input("Final notu : "))
ort=(vize1*0.3)+(vize2*0.3)+(final*0.4)
print("Ortalamanız = {}".format(ort))
if(ort>=90):
    print("AA")
elif(ort>=85):
    print("BA")
elif(ort>=80):
    print("BB")
elif(ort>=75):
    print("CB")
elif(ort>=70):
    print("CC")
elif(ort>=65):
    print("DC")
elif(ort>=60):
    print("DD")
elif(ort>=55):
    print("FD")
else:
    printf("FF")