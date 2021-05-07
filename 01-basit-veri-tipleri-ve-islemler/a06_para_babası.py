"""
Üç kardeş olan Helin, Selin ve Pelin'in babası Abidin cebindeki paranın çeyreğini
çocuklarına eşit bir şekilde paylaştırmak istiyor. Görevin Abidin'e yardım etmek.

Kaç paran var Abidin? 240
Her bir çocuğa 20 TL düşüyor.
"""


para=float(input("Kaç paran var Abidin?\n "))
kişi_başı_para=para/4/3


print(f"Her bir çocuğa {kişi_başı_para:.3g} TL düşüyor")

"""Bu kolaydı! Hadi şimdi biraz matematik yapalım. Abidin *aynı* parayı eşit paylaştırmak
yerine çocuklarının yaşlarıyla doğru orantılı olacak şekilde paylaştırmak istiyor.
Görevin Abidin'e çocuklarının yaşını sorup parayı yaşlarla doğru orantılı olacak şekilde 
paylaştırmak. Unutma, Abidin cebindeki paranın çeyreğini paylaştırmak istiyor!

Helin kaç yaşında? 10
Selin kaç yaşında? 14
Pelin kaç yaşında? 8
Kaç paran var Abidin? 256
Helin 20 TL alacak.
Selin 28 TL alacak.
Pelin 16 TL alacak.
"""
helin_yasi=int(input("Helin kaç yaşında? "))
selin_yasi=int(input("Selin kaç yaşında? "))
pelin_yasi=int(input("pelin kaç yaşında? "))
Abidinin_parasi=float(input("Kaç paran var Abidin? "))
toplam_yas=helin_yasi+selin_yasi+pelin_yasi
heline_düşen_para=para/4/(toplam_yas)*helin_yasi
seline_düşen_para=para/4/(toplam_yas)*selin_yasi
peline_düşen_para=para/4/(toplam_yas)*pelin_yasi
print(f"Helin {heline_düşen_para} TL alacak.")
print(f"Selin {seline_düşen_para} TL alacak.")
print(f"Pelin {peline_düşen_para} TL alacak.")
