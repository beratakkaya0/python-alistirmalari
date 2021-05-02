"""
Simdiki gorevin basit bir tahmin oyunu hazirlamak. Bilgisayar 1 ile 100 arasinda
rastgele bir sayi belirleyip senden tahmin yapmani istesin ve sen sayiyi bulana 
kadar oyunu devam ettirsin:

(B: bilgisayar, O: oyuncu)
B: Aklimdan bir sayi tuttum; bil bakalim ne tuttum.
O: 50
B: yukari
O: 75
B: yukari
O: 87
B: asagi
O: 81
B: asagi
O: 78
B: Bildin! Aklimdan tuttugum sayi 78'di.


Bilgisayarin urettigi rastgele sayiya 'tuttugum_sayi' isimli degiskenden
ulasabilirsin.
"""

from random import randint

tuttugum_sayi = randint(1, 100)
while True:
    tahmin=int (input('Aklimdan bir sayi tuttum;bil bakalim ne tuttum.\n'))
    if tuttugum_sayi<tahmin:
        print('asagi')
    elif tuttugum_sayi>tahmin:
        print('yukari')
    elif tuttugum_sayi==tahmin:
        print(f'Bildin!Aklimdan {tuttugum_sayi} tutmustum.')
        break

