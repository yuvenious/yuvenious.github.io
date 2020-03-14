import cgi, os
form = cgi.FieldStorage()
title = form['title'].value
description = form['description'].value

data_dir = '../web2/data'
data_path = os.path.join(data_dir, '{name}.txt'.format(name=title))
data_file = open(data_path, 'w')
data_file.write(description)
data_file.close()

url = 'index.py?id={id}'.format(id=title)

print('Content-type: text/html')
print()
print('<html><head><meta http-equiv="refresh" content="0;url={url}" /></head></html>'.format(url=url))
