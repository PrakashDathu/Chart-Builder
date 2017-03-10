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
	   a=int(getData('rows'))
	   b=int(getData('cds'))
	   title=str(getData("title"))
	   k=[[getData(str(int(s)*10)+str(h)) for s in range(a)] for h in range(b)] 
	   data = [go.Bar(
            x=k[0],
            y=k[1],
    		)]
	   layout = go.Layout(
	   	title=title,
			)
	   fig = go.Figure(data=data, layout=layout)
	   plotly.offline.plot(fig, filename='basic-bar')
	except:
	   cgi.print_exception()
