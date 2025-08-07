from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from docx import Document
from reportlab.pdfgen import canvas
import uuid
import os

app = FastAPI()

@app.post("/generate/docx")
async def generate_docx(text: str = Form(...)):
    filename = f"/tmp/{uuid.uuid4()}.docx"
    doc = Document()
    doc.add_paragraph(text)
    doc.save(filename)
    return FileResponse(filename, media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

@app.post("/generate/pdf")
async def generate_pdf(text: str = Form(...)):
    filename = f"/tmp/{uuid.uuid4()}.pdf"
    c = canvas.Canvas(filename)
    c.drawString(100, 750, text)
    c.save()
    return FileResponse(filename, media_type="application/pdf")