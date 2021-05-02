"""
Görevin girilen değeri bir değişkene atayıp o değişkenin değerini değiştirmek.

Bir sayı giriniz: 5
Bir kelime yazınız: selam

Girdiğiniz sayının 8 fazlası 13.
Girdiğiniz kelimenin  büyük harflere çevrilmiş hali: SELAM
"""

sayı = int(input("Bir sayı giriniz: "))
kelime = input("Bir kelime giriniz: ")
######################################################
sayı=sayı+8
kelime=kelime.upper()


######################################################
print(f"Girdiğiniz sayının 8 fazlası {sayı}.")
print(f"Girdiğiniz kelimenin  büyük harflere çevrilmiş hali: {kelime}")


