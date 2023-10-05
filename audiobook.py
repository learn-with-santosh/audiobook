import pyttsx3
import PyPDF2
book = open('oop.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)
num_pages = pdf_reader.numPages

speaker = pyttsx3.init()
for num in range(num_pages):
    page = pdf_reader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()