# membuat kalkulator sederhana


print(20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")

angka_1 = float(input("Bilangan 1 = "))
operator = input("Pilih operator (+, -, x, /, **, %, //) ")
angka_2 = float(input("Bilangan 2 = "))

# Percabangan banyak kondisi
if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == "x":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == "/":
   hasil = angka_1 / angka_2
   print(f"Hasilnya adalah = {hasil}")
elif operator == "**":
    hasil = angka_1 ** angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == "%":
    hasil = angka_1 % angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == "//":
    hasil = angka_1 // angka_2
    print(f"Hasilnya adalah = {hasil}")
else:
    print("Masukkan dengan benar")

print("program berakhir")