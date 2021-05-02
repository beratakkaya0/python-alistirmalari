"""
Esengül'ün alışveriş yaptığı manav artık yaşlandığı için hesap yaparken zorlanıyor.
Sadece meyvelerin üstündeki fiyat etiketlerinden meyvenin kilosunun kaça olduğunu
müşterilerine söyleyip kaç kilo almak istediklerini soruyor. Sonra toplam fiyatı
müşteriye söylüyor. Müşteriden aldığı paradan toplam fiyatı çıkarıp para üstü veriyor.
Görevin bu işlemleri yapması için manava yardım edecek bir program yazmak. 

Elmanın kilosu ... lira, muzun kilosu ... lira.
Kaç kilo elma alacaksınız? ...
Kaç kilo muz alacaksınız? ...
Toplam ... TL tuttu.
Kaç TL veriyorsunuz? ...
Para üstünüz ... TL'dir.
Yine bekleriz.
"""


elma_kg = 2.5
muz_kg = 8

##########################################
print(f"Elmanın kilosu {elma_kg} lira, muzun kilosu {muz_kg} lira.")
elma=(float(input("Kaç kilo elma alacaksınız? ")))
muz=(float(input("Kaç kilo muz alacaksınız? "))
toplam=elma*elma_kg+muz*muz_kg
print(f"Toplam {toplam} TL tuttu")
para=float(input("Kaç TL veriyorsunuz? "))
para_üstü=para-toplam

##########################################

print(f"Para üstünüz {para_üstü:.2f} TL'dir")
print('Yine bekleriz.')

