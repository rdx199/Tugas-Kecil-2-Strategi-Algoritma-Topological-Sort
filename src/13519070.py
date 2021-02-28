#function to make list to string separated by comma
def listtostring(x):
    temp = ", ".join(x)
    return temp

#logo matkul counter
strip1 = ("         ---------------------------------------")
strip2 = ("        -----------------------------------------")
strip3 = ("       -------------------------------------------")
print("")
print(str(strip1))
print(str(strip2))
print(str(strip3))
print("      -----• ▌ ▄ ·.  ▄▄▄· ▄▄▄▄▄▄ •▄ ▄• ▄▌▄▄▌-------")  
print("      -----·██ ▐███▪▐█ ▀█ •██  █▌▄▌▪█▪██▌██•-------")
print("      -----▐█ ▌▐▌▐█·▄█▀▀█  ▐█.▪▐▀▀▄·█▌▐█▌██▪-------")
print("      -----██ ██▌▐█▌▐█ ▪▐▌ ▐█▌·▐█.█▌▐█▄█▌▐█▌▐▌-----")
print("      -----▀▀  █▪▀▀▀ ▀  ▀  ▀▀▀ ·▀  ▀ ▀▀▀ .▀▀▀------")
print("      ----- ▄▄·       ▄• ▄▌ ▐ ▄ ▄▄▄▄▄▄▄▄ .▄▄▄------")
print("      -----▐█ ▌▪▪     █▪██▌•█▌▐█•██  ▀▄.▀·▀▄ █·----")
print("      -----██ ▄▄ ▄█▀▄ █▌▐█▌▐█▐▐▌ ▐█.▪▐▀▀▪▄▐▀▀▄-----")
print("      -----▐███▌▐█▌.▐▌▐█▄█▌██▐█▌ ▐█▌·▐█▄▄▌▐█•█▌----")
print("      -----·▀▀▀  ▀█▄▀▪ ▀▀▀ ▀▀ █▪ ▀▀▀  ▀▀▀ .▀  ▀----")
print(str(strip3))
print(str(strip2))
print(str(strip1))
print("")

#input file
finput = input("Input file (.txt): ")
file = open(finput, "r")
content = file.read()
content = content.replace(".","") #remove .
content = content.split("\n") #split list indicate by \n

#store matkul beserta preqnya di list content separated by comma
for i in range(len(content)):
    content[i] = content[i].split(", ") #contoh list content = [["matkul1","prereq1"],["matkul2","prereq2"], dst]

prq = [] #store count prerequisite tiap matkul, list contoh prq = [1,0,3,1]
arrprq = [] #store prequisite tiap matkul, list contoh arrprq = [["IF1"],[],["IF2","IF3","IF4"],["IF6"]]

#proses mengisi prq dengan count prerequisite masing-masing matkul
#proses mengisi arrprq dengan prerequisite masing-masing matkul, jika prerequisite = 0, maka akan diisi dengan list kosong ([])
for i in range(len(content)):
    arr1 = [] #prerequisite matkul indeks saat ini
    j = len(content[i]) - 1
    for k in range(j):
        l = 1 + k #digunakan agar pada content[i][0] tidak masuk
        arr1.append(content[i][l])
    tmp = len(arr1)
    prq.append(tmp)
    arrprq.append(arr1)
    
semester = 1 #value output semester pada print output
done = [] #list yang berisikan matkul yang sudah dihitung menjadi prerequisite
#  ide algoritma:
#      - mecari prerequisite yang 0 di list prq
#      - memasukkan matkul yang memiliki 0 prerequisite ke list done (yang dimasukkan adalah content[i][0])
#      - mengupdate list prq dan arrprq dengan menghilangkan matkul yang sudah dihitung
#        sebagai prerequisite pada proses sebelumnya
#      - ketika sum(prq) = 0 (ketika list prq sudah berbentuk [0,0,0,0,...,0]), maka
#        akan di print matkul terakhir yang TIDAK MENJADI prerequisite di matkul manapun
while (sum(prq) != 0):
    matkulsmt = [] #list yang digunakan untuk mengoutput matkul yang eligible pada semester ke-n (n = 1,2,....)
    #proses mengisi list done dan matkulsmt
    for i in range(len(prq)):
        if (prq[i] == 0 and content[i][0] not in done):
            done.append(content[i][0])
            matkulsmt.append(content[i][0])
    #proses update list prq dan arrprq (penghilangan matkul yang sudah dihitung menjadi prerequisite)
    for i in range(len(matkulsmt)):
        x = matkulsmt[i]
        for j in range(len(prq)):
            if x in arrprq[j]:
                prq[j] -= 1
                arrprq[j].remove(x)
    #output
    temp = listtostring(matkulsmt) #convert list to string
    print("Semester " + str(semester) + ": " + str(temp))
    #next loop semester + 1
    semester += 1

#proses output matkul terakhir yang tidak menjadi prerequisite matkul manapun
matkulsisa = [] #matkul terakhir yg tidak menjadi prerequisite (tidak ada di list arrprq)
for i in range(len(content)):
    if (content[i][0] not in done):
        matkulsisa.append(content[i][0])
temp = listtostring(matkulsisa) #convert list to string
#output
print("Semester " + str(semester) + ": " + str(temp))