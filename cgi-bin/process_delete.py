import cgi, os
form = cgi.FieldStorage()
page_id = form['page_id'].value # 사용자 모르게 보낸 삭제 대상
data_dir = '../web2/data'
old_file = os.path.join(data_dir, '{name}.txt'.format(name=page_id))
os.remove(old_file)

print('Content-type: text/html')
print()

print('<html><head><meta http-equiv="refresh" content="0;url={url}" /></head></html>'.format(url='index.py'))
