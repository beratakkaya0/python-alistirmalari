"""
Görevin girilen değeri bir değişkene atayıp o değişkenin değerini değiştirmek.

Bir sayı giriniz: 5
Bir kelime yazınız: selam

Girdiğiniz sayının 8 fazlası 13.
Girdiğiniz kelimenin  büyük harflere çevrilmiş hali: SELAM
"""

from turkish import *
sayı = tamsayı(değeral("Bir sayı giriniz: "))
kelime = değeral("Bir kelime giriniz: ")
######################################################
sayı=sayı+8
kelime=kelime.upper()


######################################################
yazdır(f"Girdiğiniz sayının 8 fazlası {sayı}.")
yazdır(f"Girdiğiniz kelimenin  büyük harflere çevrilmiş hali: {kelime}")


