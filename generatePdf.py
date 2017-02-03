# -*- coding: utf-8 -*-
#Generate PDF
from reportlab.pdfgen import canvas
#The units of measurement
from reportlab.lib.units import cm
#connect with the printer
import cups
# convert pdf to image
from PythonMagick import Image

def content(c):
#   Size of page
    c.setPageSize((6*cm, 9.5*cm))

    c.line(0.5*cm,0.5*cm,5.5*cm,0.5*cm)
    c.line(0.5*cm,0.5*cm,0.5*cm,9.1*cm)
    c.line(0.5*cm,9.1*cm,5.5*cm,9.1*cm)
    c.line(5.5*cm,0.5*cm,5.5*cm,9.1*cm)
    c.translate(0.5*cm,0.5*cm)
#   color of content page
    c.setFillColorRGB(0,0,0)
#   line(x1,y1,x2,y2)
    c.line(0.15*cm,0.15*cm,4.85*cm,0.15*cm)
    c.line(0.15*cm,0.15*cm,0.15*cm,8.40*cm)
    c.line(0.15*cm,8.40*cm,4.85*cm,8.40*cm)
    c.line(4.85*cm,0.15*cm,4.85*cm,8.40*cm)
#   drawString(x,y)

    c.setFont('Times-BoldItalic', 16)
    c.rotate(90)
    c.drawString(0.5*cm, -1.2*cm, "JOSE ALBERTO")
    c.drawString(1.8*cm, -1.9*cm, "EVANAN MAUCAYLLE")
    c.setFont('Times-BoldItalic', 12)
    c.drawString(1.1*cm, -3.3*cm,"* Evento: ENTRENAMIENTO 1")
    c.setFont('Times-BoldItalic', 11)
    c.drawString(1.1*cm, -4*cm, "* Ingreso - 11:10 AM")

c = canvas.Canvas("ticket.pdf")
content(c)
c.save()
conn = cups.Connection ()
printers = conn.getPrinters ()
for printer in printers:
    print "IMPRESORA"
    print "NOMBRE:",printer
    print printers[printer]["device-uri"]

file = "ticket.pdf"
to = file.replace(".pdf",".png")

p = Image()
p.density('300')
p.read(file)
p.write(to)


import subprocess

command = 'brother_ql_create --model QL-710W ./ticket.JPEG > ticket.bin; nc 192.168.1.50 9100 < ticket.bin'
subprocess.check_call(command, shell=True)

"""conn = cups.Connection ()
printer_returns = conn.printFile('ZINK-hAppyCMD:JPEG,PNG,URF', 'ticket.png', 'test', {})
print "ID JOB : ",printer_returns"""


