#!C:\Users\2054069\AppData\Local\Programs\Python\Python39\python.exe
print("Content-Type: text/html; charset=UTF-8")
print("")


import cgi, os
files = os.listdir('data')
#print(files)
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index_2_if.py?id={name}">{name}</a></li>'.format(name=item)
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
<meta charset="UTF-8">
</head>
<body>
<h1><a href="index_2_if.py">WEB</a></h1>
<ol>
    {listStr}
</ol>
<h2>{title}</h2>
<p>{desc}
</p>
<img src="engine.jpg" alt="My Image" width = 40%">
</body>
</html>
'''.format(title=pageID, desc=description, listStr=listStr))
