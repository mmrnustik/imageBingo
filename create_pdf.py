from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Spacer, Image
import os

input_dir = 'out/'

doc = SimpleDocTemplate(
    'bingo.pdf', pagesize=A4,
    topMargin=0.8*cm, bottomMargin=0.8*cm
    )

content = []

files = [input_dir + f for f in os.listdir(input_dir)]

for i, imgfile in zip(range(len(files)), files):
    img = Image(imgfile, 13.4*cm, 13.4*cm)
    content.append(img)
    if i % 2 == 0:
        content.append(Spacer(1, 0.5*cm))
doc.build(content)