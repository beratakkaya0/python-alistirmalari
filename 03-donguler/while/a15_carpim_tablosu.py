"""
Kullanicidan aldigin bir sayi ile asagidaki gibi bir carpim tablosu olusturman 
gerekiyor

Bir sayi giriniz: 6

6 x 1 = 6                                                               
6 x 2 = 12                                                              
6 x 3 = 18                                                              
6 x 4 = 24                                                              
6 x 5 = 30                                                              
6 x 6 = 36                                                              
6 x 7 = 42                                                              
6 x 8 = 48                                                              
6 x 9 = 54                                                              
6 x 10 = 60 
"""
sayi=int (input('Bir sayi giriniz: '))
a=int(input('Carpim tablosu kac satir olsun?\n'))
i=1
while i<=a: 
    sonuc=i*sayi
    print(f'{sayi} x {i} = {sonuc}')
    i+=1
