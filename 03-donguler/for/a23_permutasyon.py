"""
Gorevin kullanicidan iki sayi alarak bu iki sayi arasindaki sayilarin ikili 
permutasyonlarini yazdiran bir program yazmak

Ilk sayiyi giriniz: 4
Ikinci sayiyi giriniz: 7

4-4
4-5
4-6
4-7
5-4
5-5
5-6
5-7
6-4
6-5
6-6
6-7
7-4
7-5
7-6
7-7
"""
ilk_sayi=int(input('Ilk sayiyi giriniz: '))
ikinci_sayi=int(input('Ikinci sayisyi giriniz: ')) 
for a in range(ilk_sayi,ikinci_sayi+1):
    for b in range(ilk_sayi,ikinci_sayi+1):
        print(f'{a}-{b}')

