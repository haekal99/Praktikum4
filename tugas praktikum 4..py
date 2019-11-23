Nama=[]
Nim=[]
TGS=[]
UTS=[]
UAS=[]
Akhir=[]
jawab = 'y'
while jawab =='y':
    nama = input("Nama  : ")
    kelas = input("NIM  : ")
    nilaitugas = float(input("Nilai Tugas    :"))
    nilaiuts = float(input("Nilai UTS :"))
    nilaiuas = float(input("Nilai UAS :"))
    akhir = (nilaitugas)*30/100 + (nilaiuts)*35/100 + (nilaiuas)*35/100
    
    Nama.append(nama)
    Nim.append(kelas)
    TGS.append(nilaitugas)
    UTS.append(nilaiuts)
    UAS.append(nilaiuas)
    Akhir.append(akhir)
    
    jawab = (input('tambah data?(y/t)'))
    if jawab == 't':
    
        print("==========================================================================");
        print("| No |  Nama   |    NIM    |  Tugas  |  UTS  |  UAS  |  Akhir  |");
        print("==========================================================================");
        for i in range(len(Nama)):
            print("|", i+1 ," |",  Nama[i]  ,"|",  Nim[i]  ," |",  TGS[i]  ," |",  UTS[i]  ," |",  UAS[i]  ," |",  Akhir[i]," |")
