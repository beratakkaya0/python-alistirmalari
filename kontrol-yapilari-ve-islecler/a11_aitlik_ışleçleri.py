"""
Görevin girilen bir kelimenin içerisinde kullancının girdiği bir
harfin olup olmadığını kontrol etmek

Bir kelime giriniz: selam
Bir harf giriniz: a

Girdiğiniz harf kelimenin içinde vardır.

Bir kelime giriniz: otobüs
Bir harf giriniz: g

Girdiğiniz harf kelimenin içinde yoktur.
"""
from turkish import *
kelime=değeral("Bir kelime giriniz: ")
harf=değeral("Bir harf giriniz: ")
harfin_uzunluğu=uzunluk(harf)
if harfin_uzunluğu==1:
    if harf in kelime:
        yazdır("Girdiğiniz harf kelimenin içinde vardır.")
    else:
        yazdır("Girdiğiniz harf kelimenin içinde yoktur.")
else:
    yazdır("Girdiğiniz değer hatalıdıdır.")