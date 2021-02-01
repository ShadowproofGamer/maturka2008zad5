import string
plik_slowa = open("slowa.txt")
dane = plik_slowa.read().split()
#zad a
plik_ha = open("hasla_a.txt", "w+")
dl_maks = 0
dl_max_txt = ""
dl_min = 99
dl_min_txt = ""

for i in dane:
    temp = ""
    for j in i[-1::-1]:
        temp += j
    #print(temp)
    plik_ha.write(temp+"\n")
    if len(temp)>dl_maks:
        print(temp+"  max")
        dl_maks=len(temp)
        dl_max_txt=temp
    if len(temp) < dl_min:
        print(temp+"  min")
        dl_min=len(temp)
        dl_min_txt=temp

plik_sa=open("slowa_a.txt", "w+")
plik_sa.write("najdluzse slowo: "+dl_max_txt+"\t"+str(dl_maks)+"\t"+"najkrotsze slowo: "+dl_min_txt+"\t"+str(dl_min))

#zad b
plik_hb = open("hasla_b.txt", "w+")
plik_sb = open("slowa_b.txt", "w+")

len_12 = 0
maks = 0
maks_txt = ""
min = 99
min_txt = ""
suma = 0

for i in dane:
    text = ""
    pal = i[0]
    dl_tmp = 0
    #print(i)
    for j in range(2,len(i),2):
        #print(j)
        if i[j] == i[0]:
            #print("spr")
            tru = True
            for k in range(1,j,1):
                if i[k] != i[j-k]:
                    tru = False
            if tru:
                pal = i[0:(j+1)]
                dl_tmp = j-1
    for k in i[-1:dl_tmp:-1]:
        text+=k
    text+=i
    print(text)
    if len(text)==12:
        len_12+=1
    if len(text)>maks:
        maks_txt=text
        maks=len(text)
    if len(text)<min:
        min_txt=text
        min=len(text)
    suma+=len(text)
    plik_hb.write(text+"\n")
plik_sb.write("suma: "+str(suma)+"\n"+"najkrotsze: "+min_txt+"\n"+"najdlozsze: "+maks_txt+"\n"+"liczace 12: "+str(len_12)+"\n")




