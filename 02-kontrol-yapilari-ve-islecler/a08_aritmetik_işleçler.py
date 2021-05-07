"""
Görevin kullanıcının girdiği iki sayının birbirine tam bölünüp bölünmediğini kullanıcıya bildirmek.


Birinci sayıyı giriniz: 6
İkinci sayıyı giriniz: 3
6 sayısı 3 sayısına tam bölünüyor.

Birinci sayıyı giriniz: 12
İkinci sayıyı giriniz: 5
12 sayısı 5 sayısına tam bölünmüyor.
"""
ilk_sayı=float(input("Birinci sayıyı giriniz: "))
ikinci_sayı=float(input("İkinci sayıyı giriniz: "))
if ikinci_sayı==0:
    print("Hiçbir sayı sıfıra bölünemez")
elif ilk_sayı%ikinci_sayı==0:
    print(f"{ilk_sayı} sayısı {ikinci_sayı} sayısına tam bölünüyor.")
elif ilk_sayı%ikinci_sayı!=0:
    print(f"{ilk_sayı} sayısı {ikinci_sayı} sayısına tam bölünmüyor.")
else:
    print('girdiginiz deger tanimli degil')
"""
Görevin kullanıcıdan iki sayı alıp bu iki sayının bölünmesiyle oluşan bölüm ve kalanı bulmak


Birinci sayıyı giriniz: 12
İkinci sayıyı giriniz: 5  
Bölüm: 2
Kalan: 2

"""
birinci_sayı=float(input("Birinci sayıyı giriniz: "))
ikinci_sayı=float(input("İkinci sayıyı giriniz: "))
if ikinci_sayı==0:
    print("Hiçbir sayı sıfıra bölünemez")
else:
    b=birinci_sayı//ikinci_sayı
    k=birinci_sayı%ikinci_sayı
    print(f"Bölüm: {b}")
    print(f"Kalan: {k}")

"""
Görevin kullanıcından bir taban ve bir üs alıp taban üzeri üssü hesaplamak.
Taban sayısını giriniz: 3
Üs sayısını giriniz: 4
3^4 = 81
"""
taban=float(input("Taban sayısını giriniz: "))
üs=float(input("Üs sayısını giriniz: "))
sonuç=taban**üs
print(f"{taban}^{üs} = {sonuç}")
