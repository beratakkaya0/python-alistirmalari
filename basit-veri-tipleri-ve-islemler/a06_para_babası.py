"""
Üç kardeş olan Helin, Selin ve Pelin'in babası Abidin cebindeki paranın çeyreğini
çocuklarına eşit bir şekilde paylaştırmak istiyor. Görevin Abidin'e yardım etmek.

Kaç paran var Abidin? 240
Her bir çocuğa 20 TL düşüyor.
"""

from turkish import *

################################################
# para=noktalısayı(değeral("Kaç paran var Abidin?\n "))
# kişi_başı_para=para/4/3

#################################################

# yazdır(f"Her bir çocuğa {kişi_başı_para:.3g} TL düşüyor")

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
helin=tamsayı(değeral("Helin kaç yaşında? "))
selin=tamsayı(değeral("Selin kaç yaşında? "))
pelin=tamsayı(değeral("pelin kaç yaşında? "))
para=noktalısayı(değeral("Kaç paran var Abidin? "))
heline_düşen_para=para/4/(helin+selin+pelin)*helin
seline_düşen_para=para/4/(helin+selin+pelin)*selin
peline_düşen_para=para/4/(helin+selin+pelin)*pelin
yazdır(f"Helin {heline_düşen_para} TL alacak.")
yazdır(f"Selin {seline_düşen_para} TL alacak.")
yazdır(f"Pelin {peline_düşen_para} TL alacak.")