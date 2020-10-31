def pisagor_bulma():
    liste=list()
    for i in range(1,101):
        for j in range(1,101):
            k=((i * i) + (j * j)) ** 0.5
            if(k==int(k)):
                liste.append((i,j,int(k)))
    return liste
for i in pisagor_bulma():
    print(i)