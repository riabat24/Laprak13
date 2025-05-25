# Data diri
data_diri = ('Andi Setiawan', '12345678', 'Malang, Jawa Timur')

# Memecah data diri menjadi tuple
nama, nim, alamat = data_diri

# Output data diri
print("NIM:", nim)
print("NAMA:", nama)
print("ALAMAT:", alamat)

# Mengubah NIM menjadi tuple
nim_tuple = tuple(nim)
print("\nNIM (tuple):", nim_tuple)

# Mengubah nama depan menjadi tuple
nama_depan = tuple(nama.split()[0])
print("NAMA DEPAN:", nama_depan)

# Membalik urutan nama menjadi tuple
nama_terbalik = tuple(reversed(nama.split()))
print("NAMA TERBALIK:", nama_terbalik)
