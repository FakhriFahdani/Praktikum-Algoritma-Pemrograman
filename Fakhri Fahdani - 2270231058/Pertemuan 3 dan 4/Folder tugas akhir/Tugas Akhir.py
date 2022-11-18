# Tugas Akhir Praktikum Algoritma Pemrograman
# Create by ASLAB ELITS 2022

"""
Kasir Tiket Wahana Permainan

Program ini berfungsi untuk melakukan pencetakan bon transaksi wahana Tiket Wahana Permainan. Program akan 
meminta memasukan identitas customer, kemudian menghitung biaya dari layanan jasa laundry tersebut dan
mencetak bon hasil transaksi.
"""
import datetime

identitas = ["Nama Pelanggan", "Alamat", "No Telepon", "Jumlah Tiket", "Harga per Tiket"]
data = []
biayaLayanan = 16000
tanggal = datetime.datetime.now()

print(30*"="+"""
Nama\t: Fakhri Fahdani
NIM\t: 2270231058
Program\t: Kasir Wahana Permainan
""" + 30*"=" + "\n")

for x in range(len(identitas)):
    val = input("Masukkan " + identitas[x] + ": ")
    data.append(val)

serviceCheck = str(data[4]).upper()

if(serviceCheck == "Weekdays"):
    biayaLayanan = 8000* int(data[3])
elif(serviceCheck == "Weekend"):
    biayaLayanan = 15000 * int(data[3])
else:
    print("Harap masukkan jumlah tiket")

print("\n"+8*"=" + "Transaksi Wahana Permainan" + 8*"="+"\n") 

print("Tanggal : " + tanggal.strftime("%d - %m - %Y %X"))

for x in range(4):
    print(identitas[x] + " : " + data[x])

if(biayaLayanan % 8000 == 0):
    print("Price : 8000/tiket")
else:
    print("Price : 8000/tiket")
print("Total biaya: " + str(biayaLayanan))