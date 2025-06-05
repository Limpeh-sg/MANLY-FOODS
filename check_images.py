import os
import re

html_file = 'index.html'
missing = []
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()
for match in re.findall(r'<img[^>]+src="([^"]+)"', content):
    src = match
    if src.startswith('http://') or src.startswith('https://'): 
        continue
    # remove query parameters
    src = src.split('?')[0]
    if not os.path.exists(src):
        missing.append(src)

if missing:
    print('Missing images:')
    for m in missing:
        print('-', m)
else:
    print('All images exist.')
