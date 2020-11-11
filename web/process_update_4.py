#!C:\Users\2054069\AppData\Local\Programs\Python\Python39\python.exe
#print("Content-Type: text/html; charset=utf-8")
#print("")

import cgi, os
form = cgi.FieldStorage()
pageID = form["pageID"].value
title = form["title"].value
description = form['description'].value
 
opened_file = open('data/'+title, 'w')
opened_file.write(description)
opened_file.close()

os.rename('data/'+pageID, 'data/'+title)
 
#Redirection
print('Location: index_4_update.py?id='+title)
print()
