import pyttsx3
import PyPDF2
import os
#-----------START ---------Parameters Required Before Running the Project --------------------------------------------------
CONST_BOOK_NAME = 'The Monk Who Sold His Ferrari.pdf'                      #PDF File Name
CONST_START_BOOK_PAGE_NUMBER = int(11)         #Starting Page No
CONST_INDEX_PAGE_NO = int(9)                   #Index Page No
#----------END ------------------------------------------------------------------------------------------

book = open(CONST_BOOK_NAME, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages                      #Total Number of Pages in PDF File
print("Total No of Pages in the Book: ")
print(pages)


#-----------------------"START" The Initializing of Engine Configuration --------------------------------------------------------
engine = pyttsx3.init()

rate = engine.getProperty('rate')           # getting details of current speaking rate
engine.setProperty('rate', 110)             # setting up new voice rate
print("rate: ")
print(rate)                                 #printing current voice rate

volume = engine.getProperty('volume')       #getting to know current volume level (min=0 and max=1)
print("Volume: ")
print (volume)                              #printing current volume level
engine.setProperty('volume',1.0)            # setting up volume level  between 0 and 1

voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

#--------------------------"END" The Initializing of Engine------------------------------------------------------



""""
for num in range(1, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()
"""


#---------Naming the TextFile Generated from PDF File Name of Book-----------------------------------
tempStr = CONST_BOOK_NAME.split(".")
CONST_NEW_TEXT_FILENAME = tempStr[0] + str("_TEXT_FILE.txt")
#print(CONST_NEW_TEXT_FILENAME)
#----------------------------------ENDS-------------------------------------------------------------


#------------Starting the PDF To Text File Conversion-------------------------------------
def PDFToTextFile(StartPageNo, EndPageNo,counter):
    CONST_START_BOOK_PAGE_NUMBER  = StartPageNo - 1
    pages = EndPageNo-1
    flag = int(1)
    for num in range(CONST_START_BOOK_PAGE_NUMBER, pages):
        page = pdfReader.getPage(num)
        #print(num)                       Prints Page No of Book
        text = page.extractText()
        #print(text)
        tempStr = CONST_BOOK_NAME.split(".")
        CONST_NEW_TEXT_FILENAME = tempStr[0] + str("_TEXT_FILE_" + str(counter) + ".txt")
        if(flag == 1):
            if os.path.exists(CONST_NEW_TEXT_FILENAME):
                print(CONST_NEW_TEXT_FILENAME + " file found ")
                print("Deleting the OLD File")
                os.remove(CONST_NEW_TEXT_FILENAME)
            else:
                print(CONST_NEW_TEXT_FILENAME +  " file does not exist creating new file")


        f = open(CONST_NEW_TEXT_FILENAME, "at")             #Opening the File in Append Mode and File Type = 'text'
        PageNoStr = str(num)                                #PageNoStr Stores the page no of Book
        NewLineChar = str("\n")                             #To add a New Line

        if(flag == 1):
            f.write('Starting Reading the Book ' + CONST_BOOK_NAME)
            flag = 2

        f.write(NewLineChar+"Page No " + PageNoStr)
        f.write(NewLineChar)
        try:
            f.write(text)
        except:
            #print("Something went wrong when writing to the file")
            print("Encountered Unreadable Text on Page No:" + str(num))
            #print(text.isprintable())
            pass

    f.close()                                              #Closing the File
    print(CONST_NEW_TEXT_FILENAME)
#------------Ending the PDF To Text File Conversion-------------------------------------



def textFileToAudioConverter(fileName, counter):
    f = open(fileName, "r")
    text = f.read()
    mp3FileName = "Audio" + str(counter) + ".mp3"
    engine.save_to_file(text, mp3FileName)  # Saving Voice to a file
    engine.runAndWait()
    for x in f:
        print(x)
    f.close()

    #print("Audio Files Generated" + str(counter))



# Splitting the text file into N Text Files Chapter wise and creating separate Audio File for each Chapter
def split_PDF_To_Text_Files():
    list = [11,18,22,34,37,42,51,82,103,154,169,183,191,208]
    count = 1
    length = len(list)
    length = length - 1
    for i in range(length):
        print("Page No: " + str(list[i]) + " " + str(list[i + 1]))
        PDFToTextFile(list[i], list[i+1], count)
        count = count + 1


def generateTextToAudioFiles():
    tempStr = CONST_BOOK_NAME.split(".")
    count = 1
    ChaptersCount = 13
    print("ChaptersCount : " + str(ChaptersCount))
    for i in range(ChaptersCount):
        CONST_NEW_TEXT_FILENAME = tempStr[0] + str("_TEXT_FILE_" + str(count) + ".txt")
        textFileToAudioConverter(CONST_NEW_TEXT_FILENAME,count)
        mp3FileName = "Audio" + str(count) + ".mp3"
        print(mp3FileName + "generated Successfully")
        count = count + 1

def readingIndexPage():
    CONST_INDEX_PAGE_NO = int(9)
    page = pdfReader.getPage(CONST_INDEX_PAGE_NO)
    # print(num)                       Prints Page No of Book
    indexPageText = page.extractText()
    print(indexPageText)



def main():
    split_PDF_To_Text_Files()
    generateTextToAudioFiles()
    readingIndexPage()

main()
print("Starting the Main Function..")