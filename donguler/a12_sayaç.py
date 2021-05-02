"""
Görevin 1'den 100'e kadar olan sayıları ekrana yazdıran bir program yapmak

1
2
3
.
.
.
99
100
"""

from time import sleep
a=1
while a<101:
    print(a)
    a+=1


"""
Şimdi de kullanıcıdan aldığın alt sınır ve üst sınır arasındaki
sayıları yazdıran bir program yazman gerekiyor.

Alt sınır: 4
Üst sınır: 12

4
5
6
.
.
.
11
12
"""
alt_sınır=int(input("Alt sınır:"))
üst_sınır=int(input("Üst sınır:"))
i=alt_sınır
while i<=üst_sınır:
    print(i)
    i+=1

"""
Şimdi kullanıcıdan aldığın alt ve üst sınır arasındaki çift sayıları
yazdıran bir program yazman gerekiyor.

Alt sınır: 5
Üst sınır: 12

6
8
10
12
"""
alt_sınır=int(input("Alt sınır:"))
üst_sınır=int(input("Üst sınır:"))
i=alt_sınır
while i<=üst_sınır:
    if i % 2 == 0:
        print(i)
    i+=1

"""
Sayaçlar konusundaki son görevin verilen bir değerden geri sayım yapan program yazmak.

Bir sayı giriniz: 10

Geri sayım başladı.
10
9
8
7
6
5
4
3
2
1
0
Geri sayım bitti!

Küçük bir not:
Sayıları yazarken arada 1 saniye boşluk olmalı. Örneğin 10 yazdıktan sonra 1 saniye bekleyip
9 yazmalı. Bunu yapmak için sleep fonksiyonundan yararlanabilirsin. sleep(10) dersen program orada
10 saniye bekleyip kaldığı yerden devam eder.
"""
i=int(input("Bir sayı giriniz: "))
print("Geri sayım başladı.")
while i>=0:
    print(i)
    i-=1
    sleep(1)
print("Geri sayım bitti!")
