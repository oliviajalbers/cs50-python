from fpdf import FPDF

#get users name
name = input("What's your name? ")
shirt_text = name + " took CS50"

#create the pdf and set font
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "", 48)

#add CS50 Shirtificate to the top of the pdf
pdf.cell(200, 10, "CS50 Shirtificate", align="C", new_x="LEFT", new_y="NEXT")

#add the shirt
pdf.image("shirtificate.png", x=0.5, y=60)

#change font size and color
pdf.set_font("helvetica", "", 28)
pdf.set_text_color(255, 255, 255)

#add text to shirt
pdf.cell(200, 200, shirt_text, align="C")

#output new pdf
pdf.output("shirtificate.pdf")
