"""
Gorevin kullanicinin girdigi bir cumle icerisindeki karakterleri bir `kume` icerisinde
gostermek. Bir `kume`de ayni eleman birden fazla kez bulunamaz. 

Bir cumle giriniz: I'm perfect coder man
Girdiginiz cumledeki karakterler: {'d', 'm', 'c', 'e', 'p', ' ', 'r', 'o', 'n', 'a', 't', 'f', "'", 'I'}
"""
cumle=input('Bir cumle giriniz: ')
cumle_kumesi=set(cumle)
print(cumle_kumesi)
