import PyPDF2, docx

def extract_text_from_pdf(in_file_name, out_file):
  with open(in_file_name, 'rb') as pdf:
      reader = PyPDF2.PdfFileReader(pdf, strict=False)
      pdf_text = []
      for page in reader.pages:
          content = page.extract_text()
          pdf_text.append(content)

      #TODO write to a file

def extract_text_from_docx(in_file_name, out_file):
  # Open the Word document
  document = docx.Document(in_file_name)
  # Create a new text file
  with open(out_file, 'w') as f:
      # Loop through each page in the Word document
      for i, page in enumerate(document.pages):
          # Extract the text from each page
          text = page.text
          # Write the text from each page to the text file, along with the page number
          f.write(f'Page {i+1}:\n{text}\n\n')
  # Close the text file
  f.close()

def extract_text(file_name):
  if file == docx: #TODO this doesn't work yet
    extract_text_from_docx(file)
  else:
    extract_text_from_pdf(file)

if __name__ == "__main__":
  extract_text()
