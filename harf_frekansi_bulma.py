cumle="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
sozluk=dict()
for i in cumle:
    if(i in sozluk):
        sozluk[i]+=1
    else:
        sozluk[i]=1
for i,j in sozluk.items():
    print(i,"--->",j)