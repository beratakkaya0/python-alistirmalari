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
girilen_not=float(input("Notunuzu giriniz: "))
if girilen_not <0 or girilen_not>100:
    print("Hatalı değer girdiniz.")
elif girilen_not <= 40:
    print("F aldınız.")
elif girilen_not<=54:
    print("D aldınız.")
elif girilen_not<=69:
    print("C aldınız.")
elif girilen_not<=84:
    print("B aldınız.")
else:
    print("A aldınız.")
