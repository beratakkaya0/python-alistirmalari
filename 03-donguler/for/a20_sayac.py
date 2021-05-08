"""
Kullanicidan "alt sinir" ve "sayi limiti" alarak alt sinirdan sonraki sayi limiti
kadar sayiyi ekrana yazdirmak.

Alt sinir: 12
Sayi limiti: 5

12
13
14
15
16
"""
alt_sinir=int(input('Alt siniri giriniz: '))
sayi_limiti=int(input('Sayi limtini girniz: '))
for a in range(alt_sinir,alt_sinir+sayi_limiti):
    print(a)
