import json
import os
fd = os.open('tb_comments_1.json', os.O_RDONLY, mode=0o777)
str1 = os.read(fd, 200)
print(str1)

with open('tb_comments_1.json', encoding='utf-8') as f:
    comments = json.load(f)
    print(comments)
