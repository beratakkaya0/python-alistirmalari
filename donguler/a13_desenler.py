"""
Şimdi işleri biraz zorlaştıralım. İlk aşamada kullanıcıdan aldığın sayıyı kullanarak basit bir
desen oluşturman gerekiyor. 

Bir sayı giriniz: 5

*
**
***
****
*****


"""
satır_sayısı=int(input("Bir sayı giriniz: "))
i=1
while i<=satır_sayısı :
   print(i*'*')
   i+=1

"""
Ikinci asamada kullanicidan alacagin sayiya kadar olan sayilarla asagidaki deseni olusturman
gerekiyor.

Bir sayi giriniz: 9
1
22
333
4444
55555
666666
7777777
88888888
999999999
"""
