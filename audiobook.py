import pyttsx3
import PyPDF2
#import ebooklib
#from ebooklib import epub

book = open('oop.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
#pdfReader = epub.read_epub('oop.pdf')
pages = pdfReader.numPages
print(pages)

#One time initialization
engine = pyttsx3.init()

#set voice properties
sp_voice_id = 'english'
fr_voice_id = 'french'

engine.setProperty('voice', sp_voice_id)

#set properties _before you add things to say
engine.setProperty('rate',180) # Speed percent
engine.setProperty('volume',0.9) #volume 0-1

for num in range(1, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()

'''for voice in voices:
    print('Voice:')
    print(' - ID: %s' % voice.id)
    print(' - Name: %s' % voice.name)
    print(' - Languages: %s' % voice.languages)
    print(' - Gender: %s' % voice.gender)
    print(' - Age: %s' % voice.age)'''
