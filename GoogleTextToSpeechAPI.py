import pyttsx3
from gtts import gTTS
import PyPDF2
import os

#gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API.
           # Write spoken mp3 data to a file, a file-like object (bytestring) for further audio manipulation, or stdout. Or simply pre-generate Google Translate TTS request URLs to feed to an external program
# $ pip install gTTS
#>>> from gtts import gTTS
#>>> tts = gTTS('hello')
#>>> tts.save('hello.mp3')

#-----------------Prequisites Before Running The AudioBookProject-------------------------------------------
# 1. Install Packages
        #1.1 pip install gTTS
        #1.2 pip install PyPDF2
        #1.3 pip install playsound

# 2. System MUST BE CONNECTED TO THE INTERNET While Running the Project

#-----------START ---------Parameters Required Before Running the Project --------------------------------------------------
CONST_BOOK_NAME = 'sp.pdf'                      #PDF File Name
CONST_START_BOOK_PAGE_NUMBER = int(1)           #Starting Page No
#----------END ------------------------------------------------------------------------------------------

book = open(CONST_BOOK_NAME, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages                      #Total Number of Pages in PDF File
print("Total No of Pages in the Book: ")
print(pages)

#---------Naming the TextFile Generated from PDF File Name of Book-----------------------------------
tempStr = CONST_BOOK_NAME.split(".")
CONST_NEW_TEXT_FILENAME = tempStr[0] + str("_TEXT_FILE.txt")
#print(CONST_NEW_TEXT_FILENAME)
#----------------------------------ENDS-------------------------------------------------------------

#---------Naming the AudioBook-----------------------------------
tempStr = CONST_BOOK_NAME.split(".")
CONST_NEW_AUDIO_FILENAME = tempStr[0] + str("_AUDIOBOOK.mp3")
#print(CONST_NEW_AUDIO_FILENAME)
#----------------------------------ENDS-------------------------------------------------------------

#------------Starting the PDF To Text File Conversion-------------------------------------
flag = int(1)
for num in range(CONST_START_BOOK_PAGE_NUMBER, pages):
    page = pdfReader.getPage(num)
    #print(num)                       Prints Page No of Book
    text = page.extractText()
    #print(text)

    if (flag == 1):
        if os.path.exists(CONST_NEW_TEXT_FILENAME):
            os.remove(CONST_NEW_TEXT_FILENAME)
        else:
            print("The file does not exist")

    f = open(CONST_NEW_TEXT_FILENAME, "at")             #Opening the File in Append Mode and File Type = 'text'
    PageNoStr = str(num)                                #PageNoStr Stores the page no of Book
    NewLineChar = str("\n")                             #To add a New Line

    if(flag == 1):
        f.write('Starting Reading the Book ' + CONST_BOOK_NAME)
        flag = 2

    f.write(NewLineChar +"Page No " + PageNoStr)
    f.write(NewLineChar)
    f.write(text)

f.close()                                               #Closing the File
#------------Ending the PDF To Text File Conversion------------------------------------------------------


#-----------------------------------------Google Text To Speech API STARTS---------------------------------
engine = pyttsx3.init(driverName='sapi5')
fileName = "File.txt"
f1 = open(fileName, 'rt')
theText = f1.read()
print(f1.read())

#Saving part starts from here
tts = gTTS(text=theText, lang='en')
tts.save(CONST_NEW_AUDIO_FILENAME)
print("Audiobook Created Successfully")
f1.close()

#----------------------------------------Google Text To Speech API ENDS--------------------------------------