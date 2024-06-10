import os

def hitung_volume_balok():
    print('hitung volume balok')
    p = float(input('masukan panjang: '))
    l = float(input('masukan lebar: '))
    t = float(input('masukan tinggi: '))
    v = p * l * t
    print('volume balok adalah', v)
    return v

def hitung_volume_kubus():
    print("hitung volume kubus")
    s = float(input("masukan sisi: "))
    v = s ** 3
    print("volume kubus adalah:", v)
    return v

def hitung_volume_tabung():
    print("hitung volume tabung!")
    r = float(input('masukan jari jari: '))
    t = float(input('masukan tinggi: '))
    v = 3.14 * r * r * t
    print('volume tabung adalah', v)
    return v

def hitung_volume_kerucut():
    print("hitung volume kerucut!")
    r = float(input('masukan jari jari: '))
    t = float(input('masukan tinggi: '))
    v = 3.14 * r * r * t / 3
    print('volume kerucut adalah', v)
    return v

def hitung_volume_bola():
    print("hitung volume bola!")
    r = float(input('masukan jari jari: '))
    v = 4/3 * 3.14 * r ** 3
    print('volume bola adalah', v)
    return v

def hitung_volume_prisma_segitiga():
    print("hitung volume prisma segitiga!")
    a = float(input('masukan alas: '))
    t = float(input('masukan tinggi: '))
    v = 0.5 * a * t * t
    print('volume prisma segitiga adalah', v)
    return v

def hitung_volume_limas_segitiga():
    print("hitung volume limas segitiga!")
    a = float(input('masukan alas segitiga: '))
    t = float(input('masukan tinggi: '))
    v = 0.5 * a * t * t / 3
    print('volume limas segitiga adalah', v)
    return v

def hitung_volume_limas_segiempat():
    print("hitung volume limas segiempat!")
    s = float(input('masukan sisi persegi: '))
    t = float(input('masukan tinggi: '))
    v = s * s * t / 3
    print('volume limas segiempat adalah', v)
    return v

hasil_perhitungan = []

while True:
    userInput = int(input('Program Rumus Matematika \nVolume Bangun Ruang\n1. Rumus volume balok\n2. Rumus volume kubus\n3. Rumus volume tabung\n4. Rumus volume kerucut\n5. Rumus volume bola\n6. Rumus volume prisma segitiga\n7. Rumus volume limas segitiga\n8. Rumus volume limas segiempat\n9. Tampilkan hasil perhitungan\n10.Keluar dari program\n\npilih opsi no: '))
    os.system('clear')
    if userInput == 1:
        hasil_perhitungan.append(('Balok', hitung_volume_balok()))
    elif userInput == 2:
        hasil_perhitungan.append(('Kubus', hitung_volume_kubus()))
    elif userInput == 3:
        hasil_perhitungan.append(('Tabung', hitung_volume_tabung()))
    elif userInput == 4:
        hasil_perhitungan.append(('Kerucut', hitung_volume_kerucut()))
    elif userInput == 5:
        hasil_perhitungan.append(('Bola', hitung_volume_bola()))
    elif userInput == 6:
        hasil_perhitungan.append(('Prisma Segitiga', hitung_volume_prisma_segitiga()))
    elif userInput == 7:
        hasil_perhitungan.append(('Limas Segitiga', hitung_volume_limas_segitiga()))
    elif userInput == 8:
        hasil_perhitungan.append(('Limas Segiempat', hitung_volume_limas_segiempat()))
    elif userInput == 9:
        if hasil_perhitungan:
            print("Hasil perhitungan yang telah disimpan:")
            for index, (nama, volume) in enumerate(hasil_perhitungan, 1):
                print(f"{index}. Volume {nama}: {volume}")
        else:
            print("Belum ada hasil perhitungan yang disimpan.")
    elif userInput == 10:
        print("program selesai")
        break
    else:
        print("pilih salah satu program")