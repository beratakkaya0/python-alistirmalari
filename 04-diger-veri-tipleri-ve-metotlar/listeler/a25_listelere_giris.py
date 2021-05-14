"""
Gorevin kullanicin girdigi sayilari bir listeye atip bu sayilarin karesini yazdiran
bir program yazmak.

Sayilari giriniz: 3, 5, 8, 2, 6

Girdiginiz sayilarin kareleri sirasiyla 9, 25, 64, 4, 36
"""
# sayi_listesi=input('Sayilari giriniz: ').split(', ')
#
#
# sayilarin_karesi=[]
# for sayi in sayi_listesi:
#     sayi=(int(sayi))
#     sayilarin_karesi.append(str(sayi** 2))
#     
# #  print(sayilarin_karesi)
# print('Girdiginiz sayilarin kareleri sirasiyla',', '.join(sayilarin_karesi))
#


"""
Simdiki gorevin kullanicinin girdigi bir sayinin onceden olusturulmus olan listede
1'den fazla kez gecip gecmedigini bulmak.


Asagidaki tum ornek programlar icin elimizdeki liste soyle olsun: [9, 2, 8, 4, 9, 6]
Bir sayi giriniz: 8
8 sayisi listede sadece bir kez geciyor.

Bir sayi giriniz: 9
9 sayisi listede birden fazla kez geciyor.

Bir sayi giriniz: 3
3 sayisi listede yok.
"""


from random import randint
sayi_listesi = [randint(1, 10) for _ in range(10)]
print(f'{sayi_listesi=}')
sayi=int(input('Bir sayi giriniz: '))
sayac=0
for i in sayi_listesi:
    if i == sayi:
        sayac+=1
if sayac ==1:
    print(f'{sayi} sayisi listede bir kez geciyor.')
elif sayac==0:
    print(f'{sayi} sayisi listede gecmiyor.')
else:
    print(f'{sayi} sayisi listede birden fazla kez geciyor.')
