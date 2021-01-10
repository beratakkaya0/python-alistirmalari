"""Görevin kullanıcının yaşını hesaplamak.
Adınızı giriniz: Fahri
Doğum yılınızı giriniz: 2004
17 yaşındasın Fahri.
"""

from turkish import *
from datetime import datetime

şimdiki_yıl = datetime.now().year
#################################
# isim=değeral("Adınızı giriniz: ")
# doğum_yılı=tamsayı(değeral("Doğum yılınzı giriniz: "))
# yaş=şimdiki_yıl-doğum_yılı
# yazdır(f"{yaş} yaşındasın {isim}")

"""Görevin ilk aşamasını başarıyla tamamladın. Şimdi
aynı görevi farklı bir yöntemle yapman gerekiyor. 
Sadece ### ile işaretlenmiş bölgeler arasına kod 
yazabilirsin.
"""
####################################################
isim=değeral("Adınızı giriniz: ")
doğum_yılı=tamsayı(değeral("Doğum yılınzı giriniz: "))
yaş=yazı(şimdiki_yıl-doğum_yılı)


###################################################

sonuç = yaş + " yaşındasın " + isim + "."
yazdır(sonuç)
