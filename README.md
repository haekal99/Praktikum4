# Praktikum4

**program data mahasiswa**

Pada praktikum 4, kita akan membuat program sederhana untuk menginput data ke dalam sebuah list.

*Berikut codingnya:*

``` python
nilai = []
ulang = True

while ulang:
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    tugas = int(input("Masukkan Nilai Tugas: "))
    uts = int(input("Masukkan Nilai UTS: "))
    uas = int(input("Masukkan Nilai UTS: "))
    akhir = (tugas * 30/100) + (uts * 35/100) + (uas * 35/100)

    nilai.append([nama, nim, int(tugas), int(uts), int(uas), int(akhir)])
    if (input("Tambah data (y/t)?") == 't'):
        ulang = False

print("\t\t\tDaftar Nilai Mahasiswa")
print("====================================================================")
print("|No. |     Nama     |    NIM    |  Tugas  |  UTS  |  UAS  |  Akhir |")
print("====================================================================")
i = 0
for item in nilai:
    i += 1
    print("| {no:2d} | {nama:12s} | {nim:9s} | {tugas:7d} | {uts:5d} | {uas:5d} | {akhir:6.2f} |"
          .format(no=i, nama=item[0], nim=item[1], tugas=item[2], uts=item[3], uas=item[4], akhir=item[5]))
print("====================================================================")
```
**penjelasan**:

1. pertama membuat variable list kosong
```python 
nilai = []
ulang = True
```
Variable ```ulang = True``` digunakan untuk mengontrol perulangan.

2. Lalu kita membuat kondisi perulangan dan statement yang akan dijalankan ketika perulangan terjadi.
```python
while ulang:
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    tugas = int(input("Masukkan Nilai Tugas: "))
    uts = int(input("Masukkan Nilai UTS: "))
    uas = int(input("Masukkan Nilai UTS: "))
    akhir = (tugas * 30/100) + (uts * 35/100) + (uas * 35/100)

    nilai.append([nama, nim, tugas, uts, uas, int(akhir)])
   ```
   Dari statment di atas, Setelah menginput berbagai data atau item, inputan item tersebut akan masuk ke dalam list 'nilai'
   
3. Setelah membuat perulangan, kita membuat statement untuk menghentikan atau keluar dari perulangan yang terjadi.
   ```python
    if (input("Tambah data (y/t)?") == 't'):
        ulang = False
   ```
   Untuk keluar dari perulangan kita hanya perlu menginputkan 't' apabila diminta pada saat program dijalankan. 't' akan membuat variable ```ulang = True``` menjadi ```ulang = False``` yang mana akan menghentikan perulangan yang terjadi.
   
4. Terakhir mencetak hasil dari program yang telah dibuat.
```python
print("\t\t\tDaftar Nilai Mahasiswa")
print("====================================================================")
print("|No. |     Nama     |    NIM    |  Tugas  |  UTS  |  UAS  |  Akhir |")
print("====================================================================")
i = 0
for item in nilai:
    i += 1
    print("| {no:2d} | {nama:12s} | {nim:9s} | {tugas:7d} | {uts:5d} | {uas:5d} | {akhir:6.2f} |"
          .format(no=i, nama=item[0], nim=item[1], tugas=item[2], uts=item[3], uas=item[4], akhir=item[5]))
print("====================================================================")
```   
