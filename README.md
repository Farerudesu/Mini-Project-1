Muhammad Fahriel <br/>
2509116050

<pre> 
 __          __ ______  _       _____  ____   __  __  ______ 
 \ \        / /|  ____|| |     / ____|/ __ \ |  \/  ||  ____|
  \ \  /\  / / | |__   | |    | |    | |  | || \  / || |__   
   \ \/  \/ /  |  __|  | |    | |    | |  | || |\/| ||  __|  
    \  /\  /   | |____ | |____| |____| |__| || |  | || |____ 
     \/  \/    |______||______|\_____|\____/ |_|  |_||______| 
     </pre>

# Program Manajemen Projek Multimedia

Program sederhana berbasis **Python (CLI)** untuk mengelola daftar projek multimedia (Video Editing).  
Dengan fitur **CRUD** (Create, Read, Update, Delete) 
# Alur Program

## 1.Home Page
>Menu ini akan tampil pada saat pertama kali program dijalankan, User dapat memilih opsi dengan memasukan input nomor ataupun mengetik 
<img width="965" height="440" alt="image" src="https://github.com/user-attachments/assets/1b763ec1-d7a7-4fe8-86aa-fcd0601db3f1" /> <br/>
                        
## 2.Menu Tambah Projek 
>Menu ini berfungsi untuk menambahkan projek baru dengan detail:
>- **Judul**
>- **Jenis Konten** (Vlog, Short Movie, Dokumenter, Youtube, Reels, dll.)
>- **Durasi** (detik)
>- **Deadline** (DD-MM-YYYY)
>- **Status** (Selesai/Belum)
<img width="977" height="581" alt="image" src="https://github.com/user-attachments/assets/572e130d-a326-4eb1-9b2e-220465e96455" />

## 3.Menu Hapus Projek
>Menu ini berfungsi untuk menghapus projek dengan memasukan Nomor projek
<img width="860" height="331" alt="image" src="https://github.com/user-attachments/assets/ef52fe83-cb7d-45f7-8370-117a5881bf2c" />

## 4.Menu Perbarui Projek  
Alur:
1. Masukkan **nomor** projek yang ingin diperbarui.  
2. Jika ditemukan, masukkan **status baru** (Selesai/Belum).  
3. Data lain (judul/jenis/durasi/deadline) **tetap**, hanya status yang berubah.

> Catatan: Pencarian berdasarkan **nomor** projek

<img width="687" height="443" alt="image" src="https://github.com/user-attachments/assets/b81a9522-7c92-4758-b4ee-648adf9bdd6c" />

## 5.Menu List Projek 
>Menu ini berfungsi untuk menampilkan seluruh projek yang tersimpan dalam bentuk tabel.  
<img width="1292" height="592" alt="image" src="https://github.com/user-attachments/assets/c478a1c4-773c-4249-802b-3c64e7e26d6a" />


## 6.Menu Keluar 
 >Menu ini berfungsi untuk keluar dari program 
<img width="584" height="315" alt="image" src="https://github.com/user-attachments/assets/d92b7db0-f8ef-46f1-9411-fa61e1c1b0f5" />


# Penjelasan Kode <br/>

>Inisiasi Data
```
projek = [
    ("Teaser PKKMB", "Vlog", "120", "20-09-2025", "Belum"),
    ("Short Film Desa", "Short Movie", "600", "30-09-2025", "Selesai"),
    ("Cinematic Motor", "Reels", "180", "25-09-2025", "-"),
    ("Dokumentasi Kampus", "Dokumenter", "900", "15-10-2025", "Belum"),
    ("Konten Tutorial Editing", "Youtube", "420", "05-10-2025", "-"),
    ("Tutorial Masak Royco", "Vlog", "90", "20-08-2020", "Selesai"),
    ("Podcast with Windah Batubara", "Youtube", "390", "20-08-2022", "Selesai"),
    ("Makan bang ft Young lex", "Vlog", "1390", "03-02-2020", "Belum"),
]

```
Variabel projek berupa list yang berisi data proyek dalam bentuk tuple.
Setiap tuple berisi lima elemen: (judul, jenis, durasi, deadline, status).
Data awal ini berfungsi sebagai isi database sederhana sebelum pengguna menambah/mengubah data.
<br/>
>mencetak ASCII Art (dekorasi), dan menjalankan Loop tak terhingga serta menampilkan Menu
```
print (""" ...ASCII... """)
while True:
    print("")
    print("-" * 38)
    print(f"|Program manajemen projek multimedia |\n| {"1.Tambah projek":<34} |\n| {"2.Hapus projek":<34} |\n| {"3.Update Projek":<34} |\n| {"4.List Projek":<34} |\n| {"5.Keluar" :<34}|")
    print("-" * 38) 

    userchoice = input("Pilih 1-5 atau Ketik opsi\n>>>")
```
kode di atas mencetak ASCII art (dekorasi) di menu utama,
kemudian menjalankan Infinite loop (While true) agar program terus menampilkan menu sampai user memilih Keluar.
print(" ") dengan "-"*38 membuat  bingkai menu agar terlihat rapih.
f-string dengan ":<34" artinya mencetak rata kiri agar tulisan sejajar.
kemudian meminta input dari user (angka "1"–"5" atau teks seperti "Tambah").

>Menu Tambah (Create)
```
    if userchoice == "1" or userchoice == "Tambah":
        namaprojek = input("Masukan nama projek:\n>>>")
        jeniskonten = input("Masukan jenis konten: \n Vlog, Short Movie, Dokumenter, Youtube, Reels, lainnya \n>>>")
        durasi = input ("Masukan durasi konten (dalam detik):\n>>>")
        deadline= input("Masukan deadline projek (DD-MM-YYYY):\n>>>")
        status = input("Masukan status:\n>>>")
        projek.append((namaprojek, jeniskonten, durasi, deadline, status))
        print(f"Berhasil menambahkan: {namaprojek}")
        
```
Pada bagian ini, user diminta memasukkan lima komponen utama dari suatu projek yaitu judul,  jenis, durasi, deadline, dan status.
Data yang dimasukkan akan disimpan dalam bentuk tuple, kemudian ditambahkan ke dalam list projek dengan menggunakan fungsi .append().
Program menampilkan kembali data yang baru ditambahkan sebagai bentuk konfirmasi bahwa proses "Create" telah berhasil.


>Menu Hapus (Delete)
```
    elif userchoice =="2" or userchoice== "Hapus":
        cari = int(input("Masukkan Nomor projek yang mau dihapus: "))
        cari -=1
        if cari  < 0 or cari >= len(projek):
            print("Nomor projek tidak valid!")
            continue
        else:
            terhapus = projek.pop(cari)
            print(f"Projek '{terhapus[0]}' berhasil dihapus.")
```

user diminta memasukkan nomor projek yang ingin dihapus.
program menggunakan input integer kemudian di kurangi 1 agar sama dengan index [] . Jika nomor tidak ditemukan, maka akan menampilkan pesan kesalahan.
Jika ditemukan, projek nya akan dihapus dengan metode .pop(), dan program menampilkan judul projek yang berhasil dihapus.

>Menu Update (Update)
```
       elif userchoice == "3" or userchoice=="Update":
        
        update= int(input("Masukan nomor projek yang ingin di perbarui\n>>"))
        update -= 1
        if update < 0 or update >= len(projek):
            print("Nomor projek tidak valid!")
            continue  
        else:
            inputstatus = input("Update Status (Selesai/Belum) \n>>") 
            print("Menyimpan...")
            projek [update] = (    
            projek[update][0],
            projek[update][1],
            projek[update][2],
            projek[update][3],   
            inputstatus
            )
        print(f"projek '{projek[update][0]}' berhasil di perbarui ")

```
user memasukkan nomor projek yang ingin diperbarui statusnya.
program menggunakan input integer untuk menemukan indeks projek yang dimaksud.
Jika ditemukan, elemen status pada tuple diganti dengan input yang dimasukkano oleh user, dan elemen lainnya hanya di duplikat  
Program kemudian menampilkan pesan konfirmasi bahwa status telah berhasil diperbarui.
jika tidak di temukan nomor proyek maka akan menampilkan pesan invalid


>Menu List Projek (Read)
```
elif userchoice =="4" or userchoice=="List":
    print("-" * 100)
    print(f"{'Projek':<27} | {'Jenis':<12} | {'Durasi':<12} | {'Deadline':<15} | {'Status':<10}" )
    print("-" * 100)
    for i in projek:
        print(f"{i[0]:<28}| {i[1]:<13}| {i[2]:<12} | {i[3]:<15} | {i[4]:<10}")
    print ("-" * 100)
```
Program menampilkan seluruh data projek dalam bentuk tabel dengan kolom: Judul, Jenis, Durasi, Deadline, dan Status.
Format string dengan spesifikasi :<width digunakan agar setiap kolom rata kiri dan sejajar.

>Menu Exit Program
```
elif userchoice == "5" or userchoice=="Keluar":
    print("Menyimpan data....")
    print("Data Tersimpan..") 
    break

```
Saat user memilih keluar, Menampilkan pesan penyimpanan data.
Menghentikan loop dengan break.

```
else:
    print("Masukan input yang valid!")

```
Jika user memasukkan pilihan menu yang tidak valid, program memberikan pesan kesalahan dan menampilkan ulang menu utama.


# Flowchart

flowchart 

![Flowchart Github (1)](https://github.com/user-attachments/assets/977df08d-3985-42c7-bbc8-16f510956b88)


