
#json akan di pakai read file sbagai isi list (next update)
projek = [("Teaser PKKMB", "Vlog", "120", "20-09-2025", "Belum"),
        ("Short Film Desa", "Short Movie", "600", "30-09-2025", "Selesai"),
        ("Cinematic Motor", "Reels", "180", "25-09-2025", "-"),
        ("Dokumentasi Kampus", "Dokumenter", "900", "15-10-2025", "Belum"),
        ("Konten Tutorial Editing", "Youtube", "420", "05-10-2025", "-"),
        ("Tutorial Masak Royco", "Vlog", "90", "20-08-2020", "Selesai"),
        ("Podcast with Windah Batubara", "Youtube", "390", "20-08-2022", "Selesai"),
        ("Makan bang ft Young lex", "Vlog", "1390", "03-02-2020", "Belum"),
]
print ("""                                                                                 
,--.   ,--.,--. ,--.,--.,--------.,--.,--.   ,--.,------.,------.  ,--.  ,---.   
|   `.'   ||  | |  ||  |'--.  .--'|  ||   `.'   ||  .---'|  .-.  \ |  | /  O  \  
|  |'.'|  ||  | |  ||  |   |  |   |  ||  |'.'|  ||  `--, |  |  \  :|  ||  .-.  | 
|  |   |  |'  '-'  '|  '--.|  |   |  ||  |   |  ||  `---.|  '--'  /|  ||  | |  | 
`--'   `--' `-----' `-----'`--'   `--'`--'   `--'`------'`-------' `--'`--' `--'  """)
#perulangan agar program tetap berjalan sampai user menginput keluar
while True:
    print("")
    print("-" * 38)
    print(f"|Program manajemen projek multimedia |\n| {"1.Tambah projek":<34} |\n| {"2. Hapus projek":<34} |\n| {"3.Update Projek":<34} |\n| {"4.List Projek":<34} |\n| {"5.Keluar" :<34} |")
    print("-" * 38)

    userchoice = input("Pilih 1-5 atau Ketik opsi\n>>>") 
    
    if userchoice == "1" or userchoice == "Tambah":
        namaprojek = input("Masukan nama projek:\n>>>")
        jeniskonten = input("Masukan jenis konten: \n Vlog, Short Movie, Dokumenter, Youtube, Reels, lainnya \n>>>")
        durasi = input ("Masukan durasi konten (dalam detik):\n>>>")
        deadline= input("Masukan deadline projek (DD-MM-YYYY):\n>>>")
        status = input("Masukan status:\n>>>")
        projek.append((namaprojek, jeniskonten, durasi, deadline, status))
        print(f"Berhasil menambahkan: {namaprojek}")
        
    elif userchoice =="2" or userchoice== "Hapus":
        cari = int(input("Masukkan Nomor projek yang mau dihapus: "))
        cari -=1
        if cari  < 0 or cari >= len(projek):
            print("Nomor projek tidak valid!")
            continue
        else:
            terhapus = projek.pop(cari)
            print(f"Projek '{terhapus[0]}' berhasil dihapus.")

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
    
    elif userchoice =="4" or userchoice=="List":
        print("-" * 100)
        print(f" {"No" :<2} | {'Projek':<27} | {'Jenis':<12} | {'Durasi':<12} | {'Deadline':<15} | {'Status':<10}" )
        print("-" * 100)
        number = 0
        for i in projek:
            number +=1
            print(f"{number:<3} | {i[0]:<28}| {i[1]:<13}| {i[2]:<12} | {i[3]:<15} | {i[4]:<10}")
        print ("-" * 100)

        
    elif userchoice == "5" or userchoice=="Keluar":
        print("Menyimpan data....")
        #simpan data pakai json (next update)
        print("Data Tersimpan..") 
        break    
    else:
        print("Masukan input yang valid!")
        