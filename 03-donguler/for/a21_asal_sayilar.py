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
alt_sinir=int(input('Alt siniri giriniz: '))
ust_sinir=int(input('Ust siniri giriniz: '))
for x in range(alt_sinir+1,ust_sinir) :
    deger=x
    deger=int(deger)
# <<<
    bolunme=0
# >>>
    for i in range(1,deger+1):
# <<<
        kalan=deger%i
        if kalan==0:
            bolunme+=1
            if bolunme>2:
                break
# >>>
    if bolunme == 2:
        print(i,end=' ')
print()
# <<<
