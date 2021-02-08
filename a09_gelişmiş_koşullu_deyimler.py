"""
Görevin girilen ortalamaya göre harf notu yazdıran bir program yazmak.

Girilen ortalamanın harf notu karşılığını aşağıdaki tablodan bulabilirsin.
0-40   -> F
41-54  -> D
55-69  -> C
70-84  -> B
85-100 -> A

Notunuz: 73
B aldınız.

Notunuz: 1000
Hatalı değer girdiniz.
"""
from turkish import *
girilen_not=noktalısayı(değeral("Notunuzu giriniz: "))
if girilen_not <0 or girilen_not>100:
    yazdır("Hatalı değer girdiniz.")
elif girilen_not <= 40:
    yazdır("F aldınız.")
elif girilen_not<=54:
    yazdır("D aldınız.")
elif girilen_not<=69:
    yazdır("C aldınız.")
elif girilen_not<=84:
    yazdır("B aldınız.")
else:
    yazdır("A aldınız.")
