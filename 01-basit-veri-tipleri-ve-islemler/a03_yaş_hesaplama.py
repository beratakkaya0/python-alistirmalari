"""Görevin kullanıcının yaşını hesaplamak.
Adınızı giriniz: Fahri
Doğum yılınızı giriniz: 2004
17 yaşındasın Fahri.
"""

from datetime import datetime

simdiki_yil = datetime.now().year
#################################
ad=input('Adinizi giriniz:')
dogum_yili=int(input('Dogum yilinizi giriniz:'))
yas= simdiki_yil-dogum_yili
print(f'{yas} yasindasin {ad}')
"""Görevin ilk aşamasını başarıyla tamamladın. Şimdi
aynı görevi farklı bir yöntemle yapman gerekiyor. 
Sadece ### ile işaretlenmiş bölgeler arasına kod 
yazabilirsin.
"""
####################################################


###################################################

