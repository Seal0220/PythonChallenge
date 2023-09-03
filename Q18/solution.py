# http://www.pythonchallenge.com/pc/return/balloons.html

from difflib import Differ

with open('delta.txt', 'r') as delta:
    d1, d2 = [], []
    for d in delta.readlines():
        d1.append(d[:55].strip()+'\n')
        d2.append(d[55:].strip()+'\n')

    
    imgA = open('A.png', 'wb')
    imgB = open('B.png', 'wb')
    imgC = open('C.png', 'wb')
    
    for compare in Differ().compare(d1, d2):
        print(compare)
        byte = bytes([int(b, 16) for b in compare[2:].split() if b])
        # print(compare[2:].split())
        match compare[0]:
            case '+':
                imgA.write(byte)
            case '-':
                imgB.write(byte)
            case _:
                imgC.write(byte)
    
    imgA.close()
    imgB.close()
    imgC.close()