from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format='A4')

df = pd.read_csv("topics.csv")
"""
pdf.add_page()
pdf.set_font(family='Times', style='B')
pdf.cell(w=0, h=12, align='L', txt="Let's try this", ln=1, border=1)
pdf.cell(w=0, h=12, align='L', txt="Another line added", ln=1)
"""
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 254)
    pdf.cell(w=0, h=12, align="L", txt=row["Topic"], ln=1)
    pdf.line(10, 20, 200, 21)

    for i in range(row["Pages"] - 1):
        pdf.add_page()

pdf.output("sample.pdf")
