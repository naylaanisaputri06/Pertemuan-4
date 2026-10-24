# hitung = 1
# while hitung <= 3:
#     print(hitung)
#     hitung = hitung + 1

# #contoh
# nama = (input("Masukkkan Nama:"))
# i = 0  
# while i < len(nama):
#     print(nama)
#     i += 1
    
# #contoh
# a = int(input("Masukkan angka:"))
# for i in range(1, a + 1):
#     if  i % 3 == 0:
#        print("Fizz")
#     if i % 5 == 0:
#        print("Buzz")
#     elif i % 3 == 0 and i % 5 == 0:
#          print("FizzBuzz")
#     else:
#        print(i)

#contoh
angka = []
while True:
    n = int(input("Masukkan angka ke dalam list. \n(Ketik '-999' jika dirasa sudah cukup)\n:"))
    if n == -999:
        break
    angka.append(n)

print(f"Final list anda adalah {angka}")

if len(angka) == 0:
    print("List anda kosong. Tolong isi beberapa")
else:
    angka_terbesar = angka[0]
    for n in angka:
        if n > angka_terbesar:
            angka_terbesar = n
    print(f"Angka terbesar adalah {angka_terbesar}")


