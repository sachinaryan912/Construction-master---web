#!C:\Users\ASUS\AppData\Local\Programs\Python\Python39\python.exe

import cgi

form = cgi.FieldStorage() 

print ("Content-type:text/html\r\n\r\n")

num_1 = form.getvalue('num_1')
num_2 = form.getvalue('num_2')

# num_1 = int(input("Enter the first number : "))
# num_2 = int(input("Enter second number : "))

sum = num_1+num_2
multiply = num_1*num_2

print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print("<p>sum of two number is %s</p><br>" %sum)
print("<p>multiply of two number is %s</p>" %multiply)

# if multiply>sum:
#     name = "sachin"
#     print("<p>your name is %s </p>" %name)
# else:
#     print("<h2>less value</h2>")

print ("</body>")
print ("</html>")