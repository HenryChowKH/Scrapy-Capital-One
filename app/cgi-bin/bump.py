import cgi

form = cgi.FieldStorage()

print(form.getvalue('item'))