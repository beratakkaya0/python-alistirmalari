"""
Gorevin kullanicinin girdigi bir cumle icerisindeki karakterleri bir `kume` icerisinde
gostermek. Bir `kume`de ayni eleman birden fazla kez bulunamaz. 

Bir cumle giriniz: I'm perfect coder man
Girdiginiz cumledeki karakterler: {'d', 'm', 'c', 'e', 'p', ' ', 'r', 'o', 'n', 'a', 't', 'f', "'", 'I'}
"""
# cumle=input('Bir cumle giriniz: ')
# cumle_kumesi=set(cumle)
# print(cumle_kumesi)

"""
Simdi, gorevin ilk asamasinda verdigin ciktiyi alfabetik bir sekilde siralaman gerek.
Daha sonra her bir harfin kac kez gectigini hesaplayip kullaniciya gostermelisin.

Unutma; kumeler sirali degildir ve ayni eleman birden fazla kez tekrar edemez, 
listeler siralidir ve ayni eleman birden fazla kez tekrar edebilir.

Bir cumle giriniz: i am perfect coder man

' ': 4
'a': 2
'c': 2
'd': 1
'e': 3
'f': 1
'i': 1
'm': 2
'n': 1
'o': 1
'p': 1
'r': 2
't': 1
"""
cumle=input('Bir cumle giriniz: ')
cumle_kumesi=set(cumle)
cumle_listesi=list(cumle_kumesi)
cumle_listesi.sort()
print(cumle_listesi)
cumlenin_uzunlugu=len(cumle_listesi)
sayac=0
while sayac<cumlenin_uzunlugu:
    print(cumle_listesi[sayac],': ',cumle.count(cumle_listesi[sayac]),sep='')
    sayac+=1


