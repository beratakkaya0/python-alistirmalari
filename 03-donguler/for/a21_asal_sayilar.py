"""
Bu gorevde 19. alistirmada kullandigin asal sayi bulma kodunu biraz degistirerek
iki sayi arasindaki asal sayilari bulan bir kod yazman gerekiyor. for dongusu
konusunda oldugumuz icin while dongusunu for'a cevirmelisin.
Sadece 
# >>>
# <<<
ile isaretlenmis bolgeler arasini degistirebilirsin.


Alt siniri giriniz: 5
Ust siniri giriniz: 15

5 ile 10 arasindaki asal sayilar: 7, 11, 13
"""


# >>>
while True:
    i=1
    deger=input('Bir sayi giriniz (cikmak icin q): ')
    if deger =='q':
        print('cikiliyor...')
        break
    deger=int(deger)
# <<<
    bolunme=0
# >>>
    while i<=deger:
# <<<
        kalan=deger%i
        i+=1
        if kalan==0:
            bolunme+=1
            if bolunme==2 :
                a=i-1
            if bolunme>2:
                break
# >>>
    if bolunme == 2:
        print(f'{deger} sayisi asaldir.')
    elif bolunme!=2:
        print(f'{deger} sayisi asal degildir.') 
        print(f'{a} sayisina bolunuyo.')
# <<<
