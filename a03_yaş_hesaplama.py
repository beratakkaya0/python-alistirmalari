"""Görevin kullanıcının yaşını hesaplamak.
Adınızı giriniz: Fahri
Doğum yılınızı giriniz: 2004
17 yaşındasın Fahri.
"""

from turkish import *
from datetime import datetime

şimdiki_yıl = datetime.now().year
#################################
isim=değeral("Adınızı giriniz: ")
doğum_yılı=tamsayı(değeral("Doğum yılınzı giriniz: "))
yaş=şimdiki_yıl-doğum_yılı
yazdır(f"{yaş} yaşındasın {isim}")