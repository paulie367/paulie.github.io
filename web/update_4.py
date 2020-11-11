#!C:\Users\2054069\AppData\Local\Programs\Python\Python39\python.exe
print("Content-Type: text/html; charset=utf-8")
print("")


import cgi, os
files = os.listdir('data')
#print(files)
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index_4_update.py?id={name}">{name}</a></li>'.format(name=item)
#print(listStr)

form = cgi.FieldStorage()

if 'id' in form:
    pageID = form["id"].value
    description = open('data/'+pageID, 'r').read()
else:
    pageID = 'welcome'
    description = 'hello, web'

print("hello world")
print("of ")
print(pageID)

import sys
import io #encoding utf-8 설정
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8') #encoding utf-8 설정
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8') #encoding utf-8 설정

print('''<!doctype html>
<html>
<head>
<title> WEB1 - welcome </title>
<meta charset="utf-8">
</head>
<body>
<h1><a href="index_4_update.py">WEB</a></h1>
<ol>
    {listStr}
</ol>
<h2>{title}</h2>
<p>{desc}
</p>
<a href="create_4.py">create</a>
<form action="process_update_4.py" method="post">
  <p><input type="hidden" name="pageID" value="{form_default_title}" ></p>
  <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
  <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></p>
  <p><input type="submit" value="submit" ></p>
</form>
<img src="engine.jpg" alt="My Image" width = 40%">
</body>
</html>
'''.format(title=pageID, desc=description, listStr=listStr, form_default_title=pageID, form_default_description=description))
