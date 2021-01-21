"""
Görevin kullanıcının girdiği iki sayının birbirine tam bölünüp bölünmediğini kullanıcıya bildirmek.


Birinci sayıyı giriniz: 6
İkinci sayıyı giriniz: 3
6 sayısı 3 sayısına tam bölünüyor.

Birinci sayıyı giriniz: 12
İkinci sayıyı giriniz: 5
12 sayısı 5 sayısına tam bölünmüyor.
"""
from turkish import *
#ilk_sayı=noktalısayı(değeral("Birinci sayıyı giriniz: "))
#ikinci_sayı=noktalısayı(değeral("İkinci sayıyı giriniz: "))
# if ikinci_sayı==0:
    # yazdır("Hiçbir sayı sıfıra bölünemez")
# elif ilk_sayı%ikinci_sayı==0:
    # yazdır(f"{ilk_sayı} sayısı {ikinci_sayı} sayısına tam bölünüyor.")
# else:
    # yazdır(f"{ilk_sayı} sayısı {ikinci_sayı} sayısına tam bölünmüyor.")

"""
Görevin kullanıcıdan iki sayı alıp bu iki sayının bölünmesiyle oluşan bölüm ve kalanı bulmak


Birinci sayıyı giriniz: 12
İkinci sayıyı giriniz: 5  
Bölüm: 2
Kalan: 2

"""
# birinci_sayı=noktalısayı(değeral("Birinci sayıyı giriniz: "))
# ikinci_sayı=noktalısayı(değeral("İkinci sayıyı giriniz: "))
# if ikinci_sayı==0:
    # yazdır("Hiçbir sayı sıfıra bölünemez")
# else:
    # bölüm=birinci_sayı//ikinci_sayı
    # kalan=birinci_sayı%ikinci_sayı
    # yazdır(f"Bölüm: {bölüm}")
    # yazdır(f"Kalan: {kalan}")

"""
Görevin kullanıcından bir taban ve bir üs alıp taban üzeri üssü hesaplamak.
Taban sayısını giriniz: 3
Üs sayısını giriniz: 4
3^4 = 81
"""
taban=noktalısayı(değeral("Taban sayısını giriniz: "))
üs=noktalısayı(değeral("Üs sayısını giriniz: "))
sonuç=taban**üs
yazdır(f"{taban}^{üs} = {sonuç}")