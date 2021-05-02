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
kelime=input("Bir kelime giriniz: ")
harf=input("Bir harf giriniz: ")
harfin_uzunluğu=len(harf)
if harfin_uzunluğu==1:
    if harf in kelime:
        print("Girdiğiniz harf kelimenin içinde vardır.")
    else:
        print("Girdiğiniz harf kelimenin içinde yoktur.")
else:
    print("Girdiğiniz değer hatalıdıdır.")
