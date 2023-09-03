# http://www.pythonchallenge.com/pc/def/channel.html

import re, zipfile

comments = []
nothing = 90052

with zipfile.ZipFile('channel.zip', 'r') as zip_file:
    print(zip_file.read('readme.txt').decode())
    
    while True:
        comment = zip_file.getinfo(f'{nothing}.txt').comment.decode()
        comments.append(comment)
        
        text = zip_file.read(f'{nothing}.txt').decode()
        if (n := re.search(r'\d+', text)):
            nothing = n[0]
            print(f'NOTHING: {nothing}, COMMENT: {comment}')
        else:
            print(f'TEXT: {text}')
            break

print(''.join(comments))