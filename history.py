#!/Users/tomar/Anaconda3/python.exe
"""
Created on Sat May 27 16:34:21 2017 by tomar
#!/usr/bin/python3
#!C:\ProgramData\Anaconda3\python.exe#!/Users/tomar/Anaconda3/python.exe
"""
import cgi
import Shanghai
import json

def formatNumber(num, length):
	""" this will pad a number with zeroes to length """
	return ("0" * length + str(num))[-length:]

def formatDate(inYYYYMMDD):
	return inYYYYMMDD[0:4]+"&ndash;"+formatNumber(inYYYYMMDD[4:6], 2)+"&ndash;"+formatNumber(inYYYYMMDD[6:], 2)

form = cgi.FieldStorage() # instantiate only once!
gid = form.getvalue('gId', '106932376942135580175')	#remove default
print("Content-type: text/html \n")
with open("games.json") as gData:
	games = json.load(gData)
gDict = {}
for g in games:
	id = g["I"]
	if (id in gDict):
		gDict[id].append((g["T"], g["M"]))
	else:
		gDict[id] = [((g["T"], g["M"]))]
print('''Number of games: {}<br><br>'''.format(len(gDict[gid])))
print('''<table border=0><tr><th>Date</th><th>Moves</th>''')
for g in sorted(gDict[gid], reverse=True):
	print('''<tr><td>{}</td><td class="textR">{}</td></tr>'''.format(formatDate(g[0][0:8]), g[1]))
print('''</table>''')
