"""Görevin kare şeklindeki bir bahçenin alanını hesaplamak.

Bahçenin bir kenar uzunluğunu giriniz: 5
Alan 25.00

Bahçenin bir kenar uzunluğunu giriniz: 2.5
Alan 6.25
"""



uzunluk=(float(input("Bahçenin bir kenar uzunluğunu giriniz: ")))
alan=uzunluk*uzunluk
print(alan)

"""Görevin ilk aşamasını başarıyla tamamladın. İkinci
aşamada bir dairenin alanını hesaplaman gerekiyor. 
Yarıçapının uzunluğu r olan bir dairenin alanı π*r²'dir.
π -> pi diye okunur. Değeri 3.141... diye sonsuza kadar
gider. Bilgisayar sonsuz uzunluğundaki bir sayıyı belleğinde
tutamadığı için yaklaşık bir değer kullanman gerekecek. 
Bu değere "pi" ismiyle ulaşabilirsin.

Dairenin yarıçapını giriniz: 3
Alan: 28.27
"""

from math import pi
r=(float(input("Dairenin yarıçapını giriniz: ")))
alan=pi*r**2
print(alan)
from math import pi
r=(("Dairenin yarıçapını giriniz: "))

"""Görevin ikinci aşamasını başarıyla tamamladın. Son aşamada
bir kenar uzunluğu verilen eşkenar üçgenin alanını hesaplaman
gerekiyor. Kenar uzunluğu a olan bir üçgenin alanı 
a² * √3 / 4'tür.
Bir sayının karekökünü hesaplamak için "karekök" fonksiyonunu
kullanabilirsin.

Eşkenar üçgenin bir kenar uzunluğunu giriniz: 3
Alan: 3.89
"""

kenar=(float(input("Eşkenar üçgenin bir kenar uzunluğunu giriniz: ")))
alan=kenar**2* karekök(3)/4







print(f"Alan: {alan:.2f}")
