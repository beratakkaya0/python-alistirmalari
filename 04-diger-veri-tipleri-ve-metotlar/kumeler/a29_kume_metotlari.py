"""
Gorevin bos bir kumeyle baslayip verilen komutlarla kumeyi degistiren bir 
program yazmak. 

>>> print
set()
>>> add 1
>>> add 8
>>> add 4
>>> print
{8, 1, 4}
>>> add 'selam'
>>> print
{8, 1, 4, 'selam'}
>>> remove 8
>>> print
{1, 4, 'selam'}
>>> clear
>>> print
set()
>>> add 3
>>> add 7
>>> add 5
>>> add 3
>>> print
{3, 5, 7}
>>> quit
"""
from time import sleep
kume=set()
while True:
    girilen_komut=input().split(' ')    
    if girilen_komut[0]=='print':
        print('{',', '.join(kume),'}')
    elif girilen_komut[0]=='add':
        kume.add(girilen_komut[1])  
    elif girilen_komut[0]=='remove':
        kume.remove(girilen_komut[1])  
    elif girilen_komut[0]=='clear':
        kume.clear()  
    elif girilen_komut[0]=='quit':
        print('Program kapatiliyor...')
        sleep(1)
        break






