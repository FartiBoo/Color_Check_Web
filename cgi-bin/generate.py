#!/usr/bin/env python3

#A simple script to accept an input from an HTML form,
#parse the information and answer if that input is a color.
#In this case is to give user feedback with a simple HTML page.

#use python´s Common Gateway Interface
import cgi

#get the output of the form
form = cgi.FieldStorage()

#get an input from the form called 'color'
#and assign it´s value to a local variable called v_color

file = 'colors.txt'
with open(file) as f_obj:
  colors = f_obj.read()

v_color = form.getvalue('color')

if v_color in colors:
  #send an HTML response
  print("""
  <html>
    <head>
    <title>Color check!</title>
    </head>
    <body>
      <h1>{} is a color</h1>
    </body>
  </html>""" .format(v_color))

else:
  print("""
  <html>
    <head>
    <title>Color check!</title>
    </head>
    <body>
      <h1>{} is not a color</h1>
    </body>
  </html>""" .format(v_color))