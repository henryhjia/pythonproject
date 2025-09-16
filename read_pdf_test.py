import pdfplumber

with pdfplumber.open('./data/python_data_pdf.pdf') as pdf:
  for i, page in enumerate(pdf.pages):
    text = page.extract_text()
    print(text)

