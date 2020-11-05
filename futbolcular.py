file=open("Futbolcular.txt","w",encoding="utf-8")
file.write("Fernando Muslera,Galatasaray\nAtiba Hutchinson,Beşiktaş\nSimon Kjaer,Fenerbahçe\nDiego Perotti,Fenerbahçe\nRadamel Falcao,Galatasaray\nVincent Aboubakar,Beşiktaş\n")
file.close()

with open("Futbolcular.txt","r",encoding="utf-8") as file:
    fb=list()
    gs=list()
    bjk=list()

    for satir in file:
        satir=satir[:-1]
        liste=satir.split(",")
        if(liste[1]=="Fenerbahçe"):
            fb.append(satir+"\n")
        elif(liste[1]=="Galatasaray"):
            gs.append(satir+"\n")
        elif(liste[1]=="Beşiktaş"):
            bjk.append(satir+"\n")

    with open("Galatasaray.txt","w",encoding="utf-8") as file1:
        for i in gs:
            file1.write(i)
    with open("Fenerbahçe.txt","w",encoding="utf-8") as file2:
        for i in fb:
            file2.write(i)
    with open("Beşiktaş.txt","w",encoding="utf-8") as file3:
        for i in bjk:
            file3.write(i)








