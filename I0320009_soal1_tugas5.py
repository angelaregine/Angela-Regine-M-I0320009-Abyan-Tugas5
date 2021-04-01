nama = str(input("Masukkan nama anda: "))
jenis_kelamin = str(input("Masukkan jenis kelamin (P/W): "))

if jenis_kelamin == "P":
    print("Selamat datang, Tuan", nama+"!")
elif jenis_kelamin == "W":
    print("Selamat datang, Nyonya", nama+"!")
else:
    pass
