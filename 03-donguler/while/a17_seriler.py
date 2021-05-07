"""
Kullanicidan bir sayi al ve 1'den bu sayiya kadar olan tum sayilarin toplamini
yazdiran bir program yaz.

Bir sayi giriniz: 10

Toplam = 55.
"""
#  a=int(input('Bir sayi giriniz: '))
#  i=1
#  toplam=0
#  while i<=a:
    #  toplam+=i
    #  i+=1
#  print(f'Toplam = {toplam}')

"""
Simdi de kullanicidan aldigin bir sayiyi kullanarak asagidaki gibi bir seri olustur
ve toplamini bul.


Bir sayi giriniz: 4

2 + 22 + 222 + 2222 = 2468 


2
22
222
2222

11
22
33
44
55
"""
# sayi=int(input('Bir sayi giriniz: '))
# i=2
# toplam=0
# a=1
# while a<=sayi:
#     c=int(a*str(i))
#     toplam+=c 
#     print(f'{c}',end='')   
#     if a==sayi:
#         print(' = ',toplam,end='')   
#     else:
#         print(' + ',end='')
#     a+=1
#  print(toplam)
#
# print()

"""
Kullanicidan 1 ve 9 arasinda bir sayi girmesini iste ve aldigin sayiyi kullanarak 
asagidaki gibi bir seri olustur. Sonra bu serinin toplamini bul.

Bir sayi giriniz: 4

1 + 12 + 123 + 1234 = 1370
"""
sayi=int(input('Bir ve dokuz arasinda bir sayi giriniz: '))
i=0
while 1>sayi or sayi>9:
    sayi=int(input('Lutfen bir ve dokuz arasinda sayi girin:'))
    
toplam = 0
while i < sayi:
    a = 1
    yazdirilacak_sayi = ''
    while a <= i+1:
        yazdirilacak_sayi += str(a)
        a += 1

    print(yazdirilacak_sayi, end='')
    toplam += int(yazdirilacak_sayi)

    
    if i == sayi - 1:
        print(' = ', end='')
    else:
        print(' + ', end='')

    i += 1

print(toplam)
