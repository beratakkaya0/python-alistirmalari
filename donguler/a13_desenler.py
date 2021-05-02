"""
Şimdi işleri biraz zorlaştıralım. İlk aşamada kullanıcıdan aldığın sayıyı kullanarak basit bir
desen oluşturman gerekiyor. 

Bir sayı giriniz: 5
Ikinci sayıyi giriniz: 5

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
