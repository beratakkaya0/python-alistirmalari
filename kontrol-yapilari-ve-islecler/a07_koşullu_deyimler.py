"""
Görevin kullancının yaşını sorup oy kullanabilme durumunu yazdıran bir 
program yazmak.

Kaç yaşındasınız? 14
Oy kullanamazsınız.

Kaç yaşındasınız? 20
Oy kullanabilirsiniz.
"""

yas=int(input("Kaç yaşındasınız? "))
if yas>=18:
   print("Oy kullanabilirsiniz.")
elif yas<18:
     print("Oy kullanamazsınız.")
else:
    print('Lutfen gecerli bir deger girin')

"""

Görevin kullanıdan kullanıcı adı ve parola alıp toplam uzunluğu 40'tan az
ise sisteme kabul eden bir program yazmak.

Kullanıcı adınız: Şahin
Parolanız       : 123456
Kullanıcı adı ve parolanız toplam 11 karakterden oluşuyor!
Sisteme hoşgeldiniz!

Kullanıcı adınız: Çok uzun bir kullanıcı adı
Parolanız       : Çok uzun bir parola
Kullanıcı adı ve parolanız toplam 45 karakterden oluşuyor!
Kullanıcı adınız ile parolanızın  toplam uzunluğu 40 karakteri geçmemeli!
"""
kullanıcı_adı=input("Kullanıcı adınız: ")
parola=input("Parolanız       : ")
karakter_toplamı=uzunluk(parola)+uzunluk(kullanıcı_adı)
if karakter_toplamı>40:
    print(f"Kullanıcı adı ve parolanız toplam {karakter_toplamı} karakterden oluşuyor!")
    print("Kullanıcı adınız ile parolanızın  toplam uzunluğu 40 karakteri geçmemeli!")
else:
    print(f"Kullanıcı adı ve parolanız toplam {karakter_toplamı} karakterden oluşuyor!")
    print("Sisteme hoşgeldiniz!")


"""
Görevin kullanıcının girdiği aritmetik işlece göre işlem yapan bir program yazmak.

Birinci sayıyı giriniz: 5
İkinci sayıyı giriniz: 3
Ne işlemi yapmak istiyorsunuz(+, -, *, /)? +
5 + 3 = 8
"""
ilk_sayı=float(input("Birinci sayıyı giriniz: "))
ikinci_sayı=float(input("İkinci sayıyı giriniz: "))
işlem=input("Ne işlemi yapmak istiyorsunuz(+, -, *, /, ^)? ")

if işlem=="+":
    print(ilk_sayı+ikinci_sayı)
elif işlem=="-":
    print(ilk_sayı-ikinci_sayı)
elif işlem=="*":
    print(ilk_sayı*ikinci_sayı)
elif işlem=="/":
    if ikinci_sayı == noktalısayı(0):
        print("Bölen sıfır olamaz")
    else:
        print(ilk_sayı/ikinci_sayı)
elif işlem == "^":
    print(ilk_sayı **ikinci_sayı)

else:
    print(f"{işlem} tanımlı değil")
