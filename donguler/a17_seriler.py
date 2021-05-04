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
sayi=int(input('Bir sayi giriniz: '))
i=2
toplam=0
a=1
while a<=sayi:
    c=int(a*str(i))
    toplam+=c 
    print(f'{c}',end='')   
    if a==sayi:
        print(' = ',toplam,end='')   
    else:
        print(' + ',end='')
    a+=1
#  print(toplam)
#
print()
