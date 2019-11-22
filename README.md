# Praktikum4

**program data mahasiswa**

Pada praktikum 4, kita akan membuat program sederhana untuk menginput data ke dalam sebuah list.

*Berikut codingnya:*

```python
nama1=[]
nim1=[]
nilaitugas1=[]
nilaiuts1=[]
nilaiuas1=[]
akhir1=[]
jawab = 'y'
while jawab =='y':
    nama = input("Nama  : ")
    kelas = input("NIM  : ")
    nilaitugas = float(input("Nilai Tugas    :"))
    nilaiuts = float(input("Nilai UTS :"))
    nilaiuas = float(input("Nilai UAS :"))
    akhir = (nilaitugas)*30/100 + (nilaiuts)*35/100 + (nilaiuas)*35/100
    
    nama1.append(nama)
    nim1.append(kelas)
    nilaitugas1.append(nilaitugas)
    nilaiuts1.append(nilaiuts)
    nilaiuas1.append(nilaiuas)
    akhir1.append(akhir)
    
    jawab = (input('tambah data?(y/t)'))
    if jawab == 't':
    
        print("==========================================================================");
        print("| No |  Nama   |    NIM    |  Tugas  |  UTS  |  UAS  |  Akhir  |");
        print("==========================================================================");
        for i in range(len(nama1)):
            print("|", i+1 ," |",  nama1[i]  ,"|",  nim1[i]  ," |",  nilaitugas1[i]  ," |",  nilaiuts1[i]  ," |",  nilaiuas1[i]  ," |",  akhir1[i]," |")
```
**Penjelasan**:

1.  Langkah awal kita buat sebuah list terlebih dahulu.
2.  Setelah kita membuat sebuah list data, langkah selanjutnya ialah menggunakan **while** untuk mengulang kembali data. setelah itu input semua data contoh: NAMA,NIM,TUGAS,UTS,UAS,akhir.(kalian bisa lihat contoh di atas)
3.  Terakhir mencetak hasil dari program yang telah dibuat.

**contoh hasil**

![output praktikum 4](https://user-images.githubusercontent.com/56957271/69405069-4fb45b80-0d31-11ea-8912-25055ddc1042.JPG)

**Flowchart**

![flochart praktikum 4](https://user-images.githubusercontent.com/56957271/69406748-62309400-0d35-11ea-999d-f3230d816359.JPG)

# SELESAI
