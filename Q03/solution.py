# http://www.pythonchallenge.com/pc/def/equality.html

with open('codes.txt', 'r') as codes:
    print(''.join(__import__('re').findall(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', codes.read().strip())))
