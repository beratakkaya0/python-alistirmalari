"""
Görevin kullancının yaşını sorup oy kullanabilme durumunu yazdıran bir 
program yazmak.

Kaç yaşındasınız? 14
Oy kullanamazsınız.

Kaç yaşındasınız? 20
Oy kullanabilirsiniz.
"""

from turkish import *

#############################################

yaş=değeral("Kaç yaşındasınız? ")
if yaş>=18:
    yazdır("Oy kullanabilirsiniz.")
else:
    yazdır("Oy kullanamazsınız.")

