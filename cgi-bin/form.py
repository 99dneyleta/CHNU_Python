#!/usr/bin/env python
import cgi

form = cgi.FieldStorage()
number = float(form.getfirst("number", "Missing number value."))

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Result</title>
        </head>
        <body>""")

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

print("""</body>
        </html>""")