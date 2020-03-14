import cgi, os
form = cgi.FieldStorage()
page_id = form['page_id'].value # 사용자 모르게 이루어진 일
title = form['title'].value # 사용자가 수정해서 보낸 제목
description = form['description'].value
print(page_id, title)

data_dir = '../web2/data'
data_path = os.path.join(data_dir, '{name}.txt'.format(name=title))
data_file = open(data_path, 'w')
data_file.write(description)
data_file.close()

url = 'index.py?id={id}'.format(id=title)
old_file = os.path.join(data_dir, '{name}.txt'.format(name=page_id))
os.remove(old_file)

print('Content-type: text/html')
print()
print('<html><head><meta http-equiv="refresh" content="0;url={url}" /></head></html>'.format(url=url))
