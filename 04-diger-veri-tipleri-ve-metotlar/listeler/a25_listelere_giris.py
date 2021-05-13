"""
Gorevin kullanicin girdigi sayilari bir listeye atip bu sayilarin karesini yazdiran
bir program yazmak.

Sayilari giriniz: 3, 5, 8, 2, 6

Girdiginiz sayilarin kareleri sirasiyla 9, 25, 64, 4, 36
"""
sayi_listesi=input('Sayilari giriniz: ').split(', ')


sayilarin_karesi=[]
for sayi in sayi_listesi:
    sayi=(int(sayi))
    sayilarin_karesi.append(str(sayi** 2))
    
#  print(sayilarin_karesi)
print('Girdiginiz sayilarin kareleri sirasiyla',', '.join(sayilarin_karesi))

