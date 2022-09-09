kode_baju = input("Masukkan Kode Baju [SP/AD] : ")
ukuran = input("Masukkan Ukuran Bahy S/M/L] : ")

if kode_baju == "SP" or kode_baju == "sp" :
    merk = "SuperDry"
    if ukuran =="S" or ukuran == "s" :
        harga = 45000
    elif ukuran == "M" or ukuran =="m" :
        harga = 50000
    elif ukuran == "L" or ukuran =="l" :
        harga = 60000
    else:
        harga=0
        
elif kode_baju == "AD" or kode_baju == "ad" :
    merk = "Adidas"
    if ukuran =="S" or ukuran == "s" :
        harga = 45000
    elif ukuran == "M" or ukuran =="m" :
        harga = 50000
    elif ukuran == "L" or ukuran =="l" :
        harga = 60000
    else:
        harga=0
        
else:
    merk = "Anda Salah Memasukkan Kode Merk"
    harga=0
    
print("-------------------------")
print("Merk Bajuu:"+str(merk))
print("Harga Baju : Rp.",harga)