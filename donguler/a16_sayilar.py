"""
Gorevin kullanicidan aldigin sayilarin ortalamasini yazdiran bir program yazmak.
Kullanici istedigi kadar sayi girebilir. Sayi girisini durdurmak icin 0 girilmelidir.

Sayi girin: 5
Sayi girin: 10
Sayi girin: 45
Sayi girin: 0

3 sayi girdiniz. Girdiginiz sayilarin ortalamasi 20.
"""
a=1
sayi_alma=0
toplam=0
while a!=0:
    a=int(input('Sayi girin: '))
    toplam+=a 
    sayi_alma+=1
a=sayi_alma-1
ortalama=toplam//(a)
print(f'{a} sayi girdiniz:Girdiginiz sayilarin ortalamasi {ortalama}.')
