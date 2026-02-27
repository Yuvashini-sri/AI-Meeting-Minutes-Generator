# pdf_generator.py
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from textwrap import wrap

def save_to_pdf(text, filename="meeting_summary.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    x, y = 50, height - 50
    line_height = 15

    # Wrap long lines to fit page
    lines = text.split("\n")
    for line in lines:
        wrapped_lines = wrap(line, width=100)
        for wline in wrapped_lines:
            if y < 50:
                c.showPage()
                y = height - 50
            c.drawString(x, y, wline)
            y -= line_height

    c.save()
