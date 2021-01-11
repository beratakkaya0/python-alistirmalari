"""
Üç kardeş olan Helin, Selin ve Pelin'in babası Abidin cebindeki paranın çeyreğini
çocuklarına eşit bir şekilde paylaştırmak istiyor. Görevin Abidin'e yardım etmek.

Kaç paran var Abidin? 240
Her bir çocuğa 20 TL düşüyor.
"""

from turkish import *

################################################
para=noktalısayı(değeral("Kaç paran var Abidin?\n "))
kişi_başı_para=para/4/3









#################################################

yazdır(f"Her bir çocuğa {kişi_başı_para:.3g} TL düşüyor")
