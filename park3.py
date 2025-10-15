#1
def konversi_suhu(value, suhu):
    if suhu == 'C':
        #mengonfersi celsius ke farenheit
        return (value * 9/5) + 32
    elif suhu == 'F':
        #mengofersi farenheit ke celsius
        return (value - 32) *5/9
    else:
        raise ValueError("suhu tidak valid. gunakan" \
                         "'C' untuk celsius atau 'F' untuk farenheit.")
    print(konversi_suhu(200, 'C'))
    print(konversi_suhu(38, 'F'))

#2
luas_lingkaran = lambda jari_jari: 3.14 * (jari_jari ** 2)

n = float(input("Masukkan Nilai nari-jari lingkaran: "))

print("Luas lingkaran dengan jari-jari", n, "adalah:", luas_lingkaran(n))