nama = str(input("Masukkan nama anda: "))
nilai = float(input("Masukkan nilai anda: "))

if nilai < 60:
    print("Halo,", nama+"!", "Nilai anda setelah dikonversi adalah E")
elif nilai < 65:
    print("Halo,", nama+"!", "Nilai anda setelah dikonversi adalah C")
elif nilai < 70:
    print("Halo,", nama+"!", "Nilai anda setelah dikonversi adalah C+")
elif nilai < 75:
    print("Halo,", nama+"!", "Nilai anda setelah dikonversi adalah B")
elif nilai < 80:
    print("Halo,", nama+"!", "Nilai anda setelah dikonversi adalah B+")
elif nilai < 85:
    print("Halo,", nama+"!", "Nilai anda setelah dikonversi adalah A-")
elif nilai >= 85:
    print("Halo,", nama+"!", "Nilai anda setelah dikonversi adalah A")
else:
    print("Tidak valid")