liste1=range(1,11)
liste2=range(1,11)
for i in liste1:
    for j in liste2:
       print("{}x{}={}".format(i,j,i*j),end = "\t")
    print(end = "\n")
    