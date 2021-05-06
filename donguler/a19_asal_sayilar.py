


while True:
    i=1
    deger=input('Bir sayi giriniz (cikmak icin q): ')
    if deger =='q':
        print('cikiliyor...')
        break
    deger=int(deger)
    bolunme=0
    while i<=deger:
        kalan=deger%i
        i+=1
        if kalan==0:
            bolunme+=1
            if bolunme==2 :
                a=i-1
            if bolunme>2:
                break
    if bolunme == 2:
        print(f'{deger} sayisi asaldir.')
    elif bolunme!=2:
        print(f'{deger} sayisi asal degildir.') 
        print(f'{a} sayisina bolunuyo.')
