# Praktikum4

**program data mahasiswa**

Pada praktikum 4, kita akan membuat program sederhana untuk menginput data ke dalam sebuah list.

*Berikut codingnya:*

```python
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


```
**Penjelasan**:

1.  Langkah awal kita buat sebuah list terlebih dahulu.
2.  Setelah kita membuat sebuah list data, langkah selanjutnya ialah menggunakan **while** untuk mengulang kembali data. setelah itu input semua data contoh: NAMA,NIM,TUGAS,UTS,UAS,akhir.(kalian bisa lihat contoh di atas)
3.  Terakhir mencetak hasil dari program yang telah dibuat.

**contoh hasil**

![output praktikum 4](https://user-images.githubusercontent.com/56957271/69405069-4fb45b80-0d31-11ea-8912-25055ddc1042.JPG)

**Flowchart**

![1](https://user-images.githubusercontent.com/56957271/69475349-8c01bd80-0dfe-11ea-87be-2501688d7df3.JPG)

# SELESAI
