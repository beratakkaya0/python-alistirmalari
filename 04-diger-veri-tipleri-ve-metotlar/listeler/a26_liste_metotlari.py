"""
Gorevin bos bir listeyle baslayip verilen komutlarla listeyi degistiren bir 
program yazmak. 

>>> print
[]
>>> append 1
>>> append 8
>>> append 4
>>> print
[1, 8, 4]
>>> insert 0 'selam'
>>> print
['selam', 1, 8, 4]
>>> remove 8
>>> print
['selam', 1, 4]
>>> clear
>>> print
[]
>>> append 3
>>> append 7
>>> append 5
>>> insert 2 3
>>> print
[3, 7, 3, 5]
>>> count 3
2
>>> quit
"""
liste=list()
while True:
    deger=input('>>> ').split(' ')
    if deger[0] == 'print':
        print(liste)
    elif deger[0] == 'append':
        liste.append(deger[1])
    elif deger[0] == 'insert':
        deger[1]=int(deger[1])
        liste.insert(deger[1],deger[2])
    elif deger[0] == 'remove':
        liste.remove(deger[1])
    elif deger[0] == 'clear':
        liste.clear()
    elif deger[0] == 'count':
        print(liste.count(deger[1]))
    elif deger[0] == 'quit':
        break
