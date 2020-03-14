# python -m http.server --cgi 8000

import cgi, os

form = cgi.FieldStorage()
data_dir = '../web2/data'

if 'id' in form:
    page_id = form['id'].value
    data_path = os.path.join(data_dir, '{}.txt'.format(page_id))
    description = open(data_path, 'r').read()
    update_link = '<a href="update.py?id={}">update</a>'.format(page_id)
    delete_action = '''
    <form action='process_delete.py' method='post'>
        <input type='hidden' name='page_id' value='{}'>
        <input type='submit' value='delete'>
    </form>
    '''.format(page_id)

else:
    page_id = 'Welcome'
    description = 'Hello, web'
    update_link = ''
    delete_action = ''

list_string = ''
for filename_full in os.listdir(data_dir):
    filename, extension = os.path.splitext(filename_full)
    item = '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=filename)
    list_string += item

print('Content-type: text/html')
print()
print ('''
<!doctype html>
<html>
  <head>
    <title>WEB - welcome</title>
    <meta charset="utf-8">
  </head>

  <body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
      {list_string}
    </ol>
    <a href='create.py'>create</a>
    {update_link}
    {delete_action}
    <h2>{title}</h2>
      <p>{desc}</p>
  </body>
</html>
'''.format(title=page_id, desc=description, list_string=list_string, update_link=update_link, delete_action=delete_action))
