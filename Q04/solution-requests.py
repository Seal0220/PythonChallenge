# http://www.pythonchallenge.com/pc/def/linkedlist.php

import requests
import re

nothing = 12345
for i in range(1000):
    with requests.get(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}') as response:
        html = response.text
        print(f'{i}, {html}')
        if len(n := re.findall(r'\d+', html)) == 1:
            nothing = n[0]
        else:
            nothing = input()