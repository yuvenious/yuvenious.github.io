import cgi, os

form = cgi.FieldStorage()
data_dir = '../web2/data'

page_id = form['id'].value
data_path = os.path.join(data_dir, '{}.txt'.format(page_id))
description = open(data_path, 'r').read()

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
        <form action='process_update.py' method='POST'>
            <p><input type='hidden' name='page_id' value='{form_default_title}'></p>
            <p><input type='text' name='title' placeholder='title' value='{form_default_title}'></p>
            <p><textarea rows=4 name = 'description' placeholder='description'>{form_default_description}</textarea></p>
            <p><input type='submit'></p>
        </form>
    <h2>{title}</h2>
      <p>{desc}</p>
  </body>
</html>
'''.format(title=page_id, desc=description, list_string=list_string, form_default_title=page_id, form_default_description=description))
