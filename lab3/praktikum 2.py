angka = []
stop = False
i = 0

# Mengisi angka
while(not stop):
    angka_baru = input("Inputkan angka yang ke-{}: ".format(i))
    angka.append(angka_baru)

    # Increment i
    i += 1    
    if(angka_baru == "0"): 
        stop = True


# Cetak Semua angka
print ("=" * 10 )
print (max(angka))
