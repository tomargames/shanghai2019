#!/Users/tomar/Anaconda3/python.exe
"""
Created on Thu November 14 2019 by tomar
#!/usr/bin/python3
#!C:\ProgramData\Anaconda3\python.exe#!/Users/tomar/Anaconda3/python.exe
"""
import cgi
import Shanghai

form = cgi.FieldStorage() # instantiate only once!
moves = form.getvalue('moves', '')	#remove default
#gid = form.getvalue('gId', '106932376942135580175')	#remove default
gid = form.getvalue('gId', '')	#remove default
shg = Shanghai.Shanghai()
print("Content-type: text/html \n")
print(shg.recordGame(gid, moves))
