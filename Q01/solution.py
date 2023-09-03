# http://www.pythonchallenge.com/pc/def/map.html

hint = '''
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
'''

url = 'map.html'


# The translation
def Translate(txt):
    return ''.join(chr(ord(s)+2) for i,s in enumerate(txt)).translate(str.maketrans('{"|0)*+', 'a b.\'()'))

# The Hint
print(Translate(hint))

# The url
print(Translate(url))