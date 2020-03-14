import cgi, os

form = cgi.FieldStorage()
data_dir = '../web2/data'

list_string = ''
for filename_full in os.listdir(data_dir):
    filename, extension = os.path.splitext(filename_full)
    item = '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=filename)
    list_string += item

page_id, description = '', ''

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
        <form action='process_create.py' method='POST'>
            <p><input type='text' name='title' placeholder='title'></p>
            <p><textarea rows=4 name = 'description' placeholder='description'></textarea></p>
            <p><input type='submit'></p>
        </form>
    <h2>{title}</h2>
      <p>{desc}</p>
  </body>
</html>
'''.format(title=page_id, desc=description, list_string=list_string))
