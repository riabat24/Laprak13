# Membuka file
file_name = input("Enter a file name: ")
try:
    with open(file_name) as file:
        # Membuat dictionary untuk menghitung distribusi jam
        hour_counts = dict()

        # Mengiterasi setiap baris dalam file
        for line in file:
            # Memeriksa jika baris mengandung string "From "
            if line.startswith("From "):
                # Memisahkan baris menjadi kata-kata
                words = line.split()
                # Mengecek jika panjang kata-kata cukup untuk mengambil jam
                if len(words) >= 6:
                    # Mengambil jam dari kata ke-6 (indeks 5)
                    hour = words[5].split(":")[0]
                    # Menambahkan jam ke dalam dictionary atau menambahkan hitungan
                    hour_counts[hour] = hour_counts.get(hour, 0) + 1

        # Menampilkan distribusi jam
        for hour, count in sorted(hour_counts.items()):
            print(f"{hour} {count}")

except FileNotFoundError:
    print("File tidak ditemukan.")
except Exception as e:
    print(f"Error: {e}")
