#!C:\Users\ASUS\AppData\Local\Programs\Python\Python39\python.exe

# Import modules for CGI handling 
import cgi

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/css/bootstrap.min.css" rel="stylesheet"><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/js/bootstrap.bundle.min.js"></script>')
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')



# Get data from fields
if form.getvalue('fav_language'):
   subject = form.getvalue('fav_language')
else:
   subject = "Not set"

if form.getvalue('age'):
   subject2 = form.getvalue('age')
else:
   subject2 = "Not set"



print ("<h2>Hello %s %s</h2>" % (first_name, last_name))
print ("<h2> favourite subject is : %s</h2>" % subject)
print ("<h2> favourite age is : %s</h2>" % subject2)
print ('<h2 id="getData">hello</h2>')
print ("<button type='button' class='btn btn-primary' data-bs-toggle='modal' data-bs-target='#myModal'>Open modal</button>")




print('<div class="modal" id="myModal"><div class="modal-dialog"><div class="modal-content"><div class="modal-header"><h4 class="modal-title">Modal Heading</h4><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div><div class="modal-body"><div><input type="text" id="dia" placeholder="enter diameter" ></div></div><div class="modal-footer"><button type="button" class="btn btn-danger" data-bs-dismiss="modal" onclick="getInputValue();">okey!</button></div></div></div></div>')
print ('<script>function getInputValue(){ var inputVal = document.getElementById("dia").value; document.getElementById("getData").innerHTML = "Value is : "+inputVal;}</script>')



print ("</body>")

print ("</html>")