mely = ["a", "á", "o", "ó", "u", "ú"]
magas = ["e", "é", "i", "í", "ö", "ő", "ü", "ű"]
szavak = []

fbe = open("input.txt")
fki1 = open("vegyes.txt", "w")
fki2 = open("magas.txt", "w")
fki3 = open("mely.txt", "w")


for line in fbe:
    line = line.strip().split()

    me = False
    ma = False
    for i in line:
        for j in i:
            if j in mely:
                me = True
            if j in magas:
                ma = True
        if me and ma:
            print(i, file=fki1)
        elif me and ma == False:
            print(i, file=fki3)
        elif ma and me == False:
            print(i, file=fki2)

fbe.close()
fki1.close()
fki2.close()
fki3.close()
