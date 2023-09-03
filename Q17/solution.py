# http://www.pythonchallenge.com/pc/return/romance.html

from requests import get
from requests.compat import unquote
from urllib.parse import unquote_to_bytes
import re
from bz2 import decompress
import xmlrpc.client

linkedlist_response =  get(f'http://www.pythonchallenge.com/pc/def/linkedlist.php')
linkedlist_cookies = linkedlist_response.cookies

print(unquote(linkedlist_cookies.values()[0]))
# you should have followed busynothing...

info=''
nothing, i = 12345, 0
while True:
    with get(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={nothing}') as response:
        html, cookie = response.text, response.cookies
        info+=str(cookie.values()[0])
        print(f'{i}, {html}')
        print(f'\tcookies - info: {cookie.values()[0]}')
        if (n := re.findall(r'and the next busynothing is (\d+)', html)):
            nothing = n[0]
        else:
            break
    i+=1
    
print(info, end='\n\n')
# BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0%20%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90

cookies_deURL = unquote_to_bytes(info.replace("+", " "))
print(cookies_deURL, end='\n\n')
# b'BZh91AY&SY\x94:\xe2I\x00\x00!\x19\x80P\x81\x11\x00\xafg\x9e\xa0 \x00hE=M\xb5#\xd0\xd4\xd1\xe2\x8d\x06\xa9\xfa&S\xd4\xd3!\xa1\xeai7h\x9b\x9a+\xbf`"\xc5WX\xe1\xadL\x80\xe8V<\xc6\xa8\xdbH&32\x18\xa8x\x01\x08!\x8dS\x0b\xc8\xaf\x96KO\xca2\xb0\xf1\xbd\x1du\xa0\x86\x05\x92s\xb0\x92\xc4Bc\xf1w$S\x85\t\tC\xae$\x90'

cookies_deBZ2 = decompress(cookies_deURL).decode()
print(cookies_deBZ2, end='\n\n')
# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.



url = "http://www.pythonchallenge.com/pc/phonebook.php"
with xmlrpc.client.ServerProxy(url) as proxy:
    print(proxy.phone('Leopold')) # 555-VIOLIN
    
# http://www.pythonchallenge.com/pc/stuff/violin.php
msg = 'the flowers are on their way'
url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
res = get(url, headers={'Authorization': ''}, cookies={'info': 'the flowers are on their way'})
print(res.text)
# oh well, don't you dare to forget the balloons.