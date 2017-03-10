#!C:\Python27\python.exe

import cgi
import plotly
import plotly.graph_objs as go
formData=cgi.FieldStorage()
def getData(id):
	firstname= formData.getvalue(id)
	return firstname
def htmlTop():
	print """Content-type: text/plain\n\n<!DOCTYPE html><html lang="en">
				<head>
				<meta charset="utf-8"/>
				<title>Pie Chart</title>
				</head>
				<body>"""
def htmlTail():
	print """</body>
		</html>"""
if __name__=="__main__":
	try:
	   x=int(getData('rows'))
	   y=int(getData('cds'))
	   title=str(getData("title"))
	   k=[[getData(str(int(s)*10)+str(h)) for s in range(x)] for h in range(y)] 
	   fig = {
				'data': [{'labels':k[0],
				'values': k[1],
				'type': 'pie'}],
				'layout': {'title': title}
			 }	
	   plotly.offline.plot(fig)
	except:
	   cgi.print_exception()
