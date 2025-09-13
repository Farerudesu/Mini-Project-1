import time
import json
#json read file sbagai isi list 
with open('data.json', 'r') as f:
    projek = json.load(f)   

print ("""                                                                                 
,--.   ,--.,--. ,--.,--.,--------.,--.,--.   ,--.,------.,------.  ,--.  ,---.   
|   `.'   ||  | |  ||  |'--.  .--'|  ||   `.'   ||  .---'|  .-.  \ |  | /  O  \  
|  |'.'|  ||  | |  ||  |   |  |   |  ||  |'.'|  ||  `--, |  |  \  :|  ||  .-.  | 
|  |   |  |'  '-'  '|  '--.|  |   |  ||  |   |  ||  `---.|  '--'  /|  ||  | |  | 
`--'   `--' `-----' `-----'`--'   `--'`--'   `--'`------'`-------' `--'`--' `--'  """)
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
        print(f"Berhasil ditambahkan: {namaprojek} | {jeniskonten} | {durasi} detik | {deadline} | {status}")
        
    elif userchoice =="2" or userchoice== "Hapus":
        cari = input("Masukkan judul projek yang mau dihapus: ").strip()
        pencarian =next((i for i, t in enumerate(projek) if t[0] == cari), None)
        if pencarian is None:
            print("Judul tidak ditemukan.")
        else:
            terhapus = projek.pop(pencarian)
            print(f"Projek '{terhapus[0]}' berhasil dihapus.")

    elif userchoice == "3" or userchoice=="Update":
        update= input("Masukan judul projek yang ingin di perbarui\n>>").strip()
        pencarian =next((i for i, t in enumerate(projek) if t[0] == update), None)
        if pencarian is None: 
            print("Judul tidak ada dalam database!!!")
        else: 
            print("Menyimpan...")
            inputstatus = input("Update Status (Selesai/Belum) \n>>") 
            projek [pencarian] = (    
                projek[pencarian][0],
                projek[pencarian][1],
                projek[pencarian][2],
                projek[pencarian][3],   
                inputstatus
            )
            time.sleep(1)
            print(f"projek '{update}' berhasil di perbarui ")
    
    elif userchoice =="4" or userchoice=="List":
        print("-" * 100)
        print(f"{'Projek':<27} | {'Jenis':<12} | {'Durasi':<12} | {'Deadline':<15} | {'Status':<10}" )
        print("-" * 100)
        for i in projek:
            print(f"{i[0]:<28}| {i[1]:<13}| {i[2]:<12} | {i[3]:<15} | {i[4]:<10}")
        print ("-" * 100)

        
    elif userchoice == "5" or userchoice=="Keluar":
        print("Menyimpan data....")
        time.sleep(2)
        #simpan data pakai json
        with open('data.json', 'w') as f:
            json.dump(projek, f)
        print("Data Tersimpan..") 
        break    
    else:
        print("Masukan input yang valid!")
        