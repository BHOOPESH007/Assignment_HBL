##import os
##print("test")
##CountList=[0,1,2,3,4,5]
##
##filename='C:/Users/Bhoopesh/Pictures/Desktop/Assinment/index1.html'
##webbrowser.open_new_tab(filename)

##import webbrowser
##import os
##print ()
##f = open('helloworld.html','w')
##a=5
##message = """<html>
##<head></head>
##<body><p>""" + str(a) + """</p></body>
##</html>"""
## 
##f.write(message)
##f.close()

##
###Change path to reflect file location
##filename = 'file:///'+os.getcwd()+'/' + 'helloworld.html'
##webbrowser.open_new_tab(filename)

import webbrowser
index1 = open("index1.html").read().format(CountList_1='World',CountList_2='World',CountList_3='World',CountList_4='World',CountList_5='World')
with open('new_index.html','w') as f:
    f.write(index1)
    f.close()
filename='C:/Users/Bhoopesh/Pictures/Desktop/Assinment/new_index.html'
webbrowser.open_new_tab(filename)
