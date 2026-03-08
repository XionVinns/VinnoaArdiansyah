NamaSiswa = input("Masukan Nama : ")
Absen = input("Masukan absensi : ")
password = input("Masukan Password Siswa : ")

data_user = {
    "vinno": ["30", "vinno123"],
    "dios": ["12", "dios123"]
}

if NamaSiswa in data_user and data_user[NamaSiswa] == [Absen, password]:
    print("Login Berhasil")
    
   
    print("\nSilahkan pilih status kehadiran hari ini:")
    print("1. Hadir")
    print("2. Tidak Hadir")
    
    pilihan = input("Pilih (1/2): ")

    if pilihan == "1":
        print(f"Konfirmasi: {NamaSiswa} (Absen {Absen}) tercatat HADIR di kelas.")
        
    elif pilihan == "2":
        print("\n--- Menu Alasan Tidak Hadir ---")
        print("a. Sakit")
        print("b. Izin")
        print("c. Tanpa Keterangan (Alpa)")
        
        alasan = input("Pilih alasan (a/b/c): ")
        
        if alasan == "a":
            print(f"Catatan: {NamaSiswa} tidak hadir karena SAKIT.")
        elif alasan == "b":
            print(f"Catatan: {NamaSiswa} tidak hadir karena IZIN.")
        elif alasan == "c":
            print(f"Catatan: {NamaSiswa} ALPA (Tanpa Keterangan).")
        else:
            print("Pilihan alasan tidak valid.")
    else:
        print("Pilihan menu salah.")

else:
    print("Login Gagal")