#!C:\Users\Yoochan\AppData\Local\Programs\Python\Python38-32\python.exe
print("Content-Type: text/html")
print()
import cgi
form = cgi.FieldStorage()
pageID = form["id"].value
print(pageID)
import sys
import io                                                              #encoding utf-8 설정
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8') #encoding utf-8 설정
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8') #encoding utf-8 설정
print('''<!doctype html>
<html>
<head>
    <title> WEB1 - welcome </title>
    <meta charset="UTF-8">
</head>
<body>
    <h1><a href="index.py?id=WEB">WEB</a></h1>
    <ol>
        <li><a href ="index.py?id=HTML"> HTML</a></li>
        <li><a href ="index.py?id=CSS"> CSS</a></li>
        <li><a href ="index.py?id=JavaScript"> JavaScript</a></li>
    </ol>
    <h2>{title}</h2>
    <p><a href= "https://en.wikipedia.org/wiki/World_Wide_Web"
        target = "_blank" title = "html5 specification">  Web </a>
        is an information system.
        <br>
        Web은 World Wide Web (www)라고 부릅니다.

    </p>
    <img src="ilya-pavlov-OqtafYT5kTw-unsplash.jpg" alt="My Image" width = 40%">
</body>
</html>
'''.format(title=pageID))