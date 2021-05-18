"""
Gorevin kullaniciya X-O-X oyununu oynatan bir program yazmak.
Oyunun nasil oynanacagi, kullanicidan girdiyi nasil alacagin sana kalmis.

Tahtayi soyle gosterebilirsin:
_ _ _
_ _ _
_ _ _

Sag ust koseye X konulmus hali:
_ _ X
_ _ _
_ _ _


Kullanicinin X ya da O koymak istedigi yeri anlamak icin ilk once satir numarasi
sonra sutun numarasi alabilirsin:
3 1 x
Yani 3. satirdaki ilk sutuna X koy, gibi.

Veya her bir kutucuga numara verip o numara girildiginde o kutucugu doldurabilirsin:
8 o
Yani 8. kutucuga O koy, gibi.

X ya da O konulmasi isi sirayla olacagi icin bu isi bilgisayara yaptirabilirsin.
Boylece kullanicilar x ya da o yazmak zorunda kalmaz. 


Bunlar aklima gelen birkac fikir. Oyunu istedigin gibi yazmakta ozgursun.

Kolay gelsin!
"""
from random import choice
kullanici_1=input('Birinci Kullanicinin adini giriniz: ')
kullanici_2=input('Ikinci kullanicinin adini giriniz: ')
a=choice([kullanici_1,kullanici_2])
sayac=2
print(a.title(),'basliyor.')
satirlar=[['-','-','-'],['-','-','-'],['-','-','-']]
while True:
    b=choice([kullanici_1,kullanici_2])
    if a!=b:
        break
b.title()
while True:
    kalan=sayac%2
    if kalan ==0:
        simge='X'
    else:
        simge='O'
    if sayac != 2:
        if kalan ==0:
            print(f'{a} sende sira!')
        else:
            print(f'{b} sende sira!')
    sayac+=1
    for satir in satirlar:
        print(' '.join(satir))
    satir=input('Satir numarasini giriniz: ')   
    if satir == 'bitti':
        print('Oyun bitti!')
        if kalan == 0:
            print(f'{b} kazandi!')
        else:
            print(f'{a} kazandi!')
        break
    elif satir == 'berabere':
        print('Oyun bitti!')
        print('Dostluk kazandi!')
        break
    sutun=int(input('Sutun numarasini giriniz: '))
    satir = int(satir)
    if satir>3 or sutun>3:
         print('Yanlis bir deger girdiginizden dolayi hakkinizi kaybettiniz.')
    elif satir <=3:
        satirlar[satir-1][sutun-1]=simge
