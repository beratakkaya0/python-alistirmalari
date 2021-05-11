"""
Gorevin Fibonacci dizisinin ilk N terimini yazdirmak. (N sayisini kullanici belirleyecek)
Fibonacci dizisi 0, 1 diye baslar ve bundan sonraki her terim kendinden once gelen iki 
terimin toplami ile bulunur.

Ornek: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

N sayisini giriniz: 7

0
1
1
2
3
5
8

"""
n=int(input('N sayisini giriniz: '))
fibonacci_listesi=[0,1]
for b in range(n-2):
    if b==0:
        print(0)
        print(1)
    c=fibonacci_listesi[-1]
    d=fibonacci_listesi[-2]
    fibonacci_listesi.append(c+d)
    print(c+d)
