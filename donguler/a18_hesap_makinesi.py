"""
Bu gorevde kullanicinin istedigi kadar islem yapan basit bir hesap makinesi 
yapman gerekiyor. Asagidaki ornekte sadece 4 islem var ama daha fazla ozellik
eklemekten cekinme!

(1) topla
(2) çıkar
(3) çarp
(4) böl

Yapmak istediginiz islemin numarasini girin (cikmak icin q): 1
Toplama islemi icin ilk sayiyi girin: 5
Toplama islemi icin ikinci sayiyi girin: 10
5 + 10 = 15


(1) topla
(2) çıkar
(3) çarp
(4) böl

Yapmak istediginiz islemin numarasini girin (cikmak icin q): 3
Carpma islemi icin ilk sayiyi girin: 3
Carpma islemi icin ikinci sayiyi girin: 7
3 x 7 = 21


(1) topla
(2) çıkar
(3) çarp
(4) böl

Yapmak istediginiz islemin numarasini girin (cikmak icin q): q
Cikiliyor...
"""
deger=0
while deger!='q':
    print('(1) topla')
    print('(2) cikar')
    print('(3) carp')
    print('(4) bol') 
    print('(5) ussunu al')
    print('(6)karekokonu al')
    deger=(input('Yapmak istdiginiz islemin numarisini girin (cikmak icin q): '))
    if deger == 'q':
        print('Cikiliyor...')
        break
    islemler = {"1": "Toplama", "2": "Cikarma", "3" : 'carpma', '4' : 'bolme', '5' : 'us alma', '6' : 'karekokonu alma'}
    islem = islemler[deger]
    deger=int(deger)
    ilk_sayi=float(input(f'{islem} islemi icin ilk sayiyi girin: '))
    if deger!=6:
        ikinci_sayi=float(input(f'{islem} islemi icin ikinci sayiyi girin: '))
    if deger== 1:
        print(f'{ilk_sayi} + {ikinci_sayi} = {ilk_sayi+ikinci_sayi}')
    elif deger== 2:
        print(f'{ilk_sayi} - {ikinci_sayi} = {ilk_sayi-ikinci_sayi}')
    elif deger == 3:
        print(f'{ilk_sayi} x {ikinci_sayi} = {ilk_sayi*ikinci_sayi}')
    elif deger == 4:
        if ikinci_sayi==0:
            print('Hicbir sayi sifira bolunemez.')
            continue
        print(f'{ilk_sayi} / {ikinci_sayi} = {ilk_sayi/ikinci_sayi}')
    elif deger == 5:
        print(f'{ilk_sayi} ^ {ikinci_sayi} = {ilk_sayi**ikinci_sayi}')
    elif deger == 6:
        print(f'{ilk_sayi} ^ 0.5 = {ilk_sayi**0.5}')
    else:
        print('girdiginiz deger tanimli degil.')

