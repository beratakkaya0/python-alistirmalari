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

from turkish import *
# a=1
# while a<101:
    # yazdır(a)
    # a+=1


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
# alt_sınır=tamsayı(değeral("Alt sınır:"))
# üst_sınır=tamsayı(değeral("Üst sınır:"))
# i=alt_sınır
# while i<=üst_sınır:
    # yazdır(i)
    # i+=1

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
alt_sınır=tamsayı(değeral("Alt sınır:"))
üst_sınır=tamsayı(değeral("Üst sınır:"))
i=alt_sınır
kalan=alt_sınır%2
kalan_2=üst_sınır%2
while kalan==0 and kalan_2==0 and üst_sınır>=i:
    yazdır(i)
    i+=2
while kalan==1 and kalan_2==1 and üst_sınır>i:
    yazdır(i+1)
    i+=2
while kalan==1 and kalan_2==0 and üst_sınır>i:
    yazdır(i+1)
    i+=2
while kalan==0 and kalan_2==1 and üst_sınır>i:
    yazdır(i)
    i+=2


