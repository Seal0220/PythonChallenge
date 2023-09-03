# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib.request as request
import re

nothing = 12345
for i in range(400):
    with request.urlopen(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}') as response:
        html = response.read().decode()
        print(f'{i}, {html}')
        if len(n := re.findall(r'\d+', html)) == 1:
            nothing = n[0]
        else:
            nothing = input()
                