#!C:\Users\2054069\AppData\Local\Programs\Python\Python39\python.exe
#print("Content-Type: text/html; charset=UTF-8")
#print("")

import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form['description'].value
 
opened_file = open('data/'+title, 'w')
opened_file.write(description)
opened_file.close()
 
#Redirection
print('Location: index_3_form.py?id='+title)
print()
