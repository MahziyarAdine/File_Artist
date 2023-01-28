import fitz as PyMuPDF
from googletrans import Translator
import os,sys
from time import sleep
from colorama import Fore,init

init()

def banner(): 
    os.system('cls' or 'clear')
    print(Fore.CYAN+"""
  _______  __    ___       _______        __        _______  ___________  __      ________  ___________  
 /"     "||" \  |"  |     /"     "|      /""\      /"      \("     _   ")|" \    /"       )("     _   ") 
(: ______)||  | ||  |    (: ______)     /    \    |:        |)__/  \\__/ ||  |  (:   \___/  )__/  \\__/  
 \/    |  |:  | |:  |     \/    |      /' /\  \   |_____/   )   \\_ /    |:  |   \___  \       \\_ /     
 // ___)  |.  |  \  |___  // ___)_    //  __'  \   //      /    |.  |    |.  |    __/  \\      |.  |     
(:  (     /\  |\( \_|:  \(:      "|  /   /  \\  \ |:  __   \    \:  |    /\  |\  /" \   :)     \:  |     
 \__/    (__\_|_)\_______)\_______) (___/    \___)|__|  \___)    \__|   (__\_|_)(_______/       \__|   
                                                      
                    Version : 1.0
                    Coded By : Mahziyar Adine
                    Website :  mahziyar-adine.gigfa.com

    
    """ +Fore.RESET)
    print(Fore.GREEN+"""
    Hello, I am a File Artist. I can process subtitles and PDF files and translate them from English to Persian.
    """ +Fore.RESET)

    print(Fore.MAGENTA+"""

    __/__/_   __/__/_   __/__/_   __/__/_   __/__/_   __/__/_   __/__/_   __/__/_ 
 __/__/_   __/__/_   __/__/_   __/__/_   __/__/_   __/__/_   __/__/_   __/__/_  
  /  /      /  /      /  /      /  /      /  /      /  /      /  /      /  /    
  
    [1] PDF
    [2] SUBTITLE

    """ +Fore.RESET)


banner()

typeWork = input(f"{Fore.MAGENTA} Do you work with pdf or subtitle ??? {Fore.RESET}")


def extract_images(fileName) :

    fileName = fileName
    document = PyMuPDF.open(fileName)
    pagesPdf = document.pages()

    print(f"{Fore.YELLOW} Extract PDF Images has started {Fore.RESET}") 
    for page in pagesPdf :

        images = page.get_images(True)

        for index,image in enumerate(images) : 

            xref = image[0]

            imageData = document.extract_image(xref)

            imageBytes = imageData['image']
            imageExt   = imageData['ext']

            pixmap = PyMuPDF.Pixmap(imageBytes)
            pixmap.save(f"PDF/Images/page{page.number + 1}-{index}.png")

    print(f" {Fore.GREEN} Pdf file image extraction was done successfully!!!")        

        

def Translation_Pdf(fileName):

    fileName = fileName
    document = PyMuPDF.open(fileName)
    translator = Translator()

    pagesPdf = document.pages()

    try :
      print(f"{Fore.YELLOW} PDF translation has started {Fore.RESET}")  
      for page in pagesPdf :

        numberPage = page.number + 1
        textPage = page.get_text(option='text')

        if textPage != '' :
            translate = translator.translate(textPage , 'fa' , 'en')

            with open(f'PDF/Text-Translation/page-{numberPage}.txt' , 'w' , encoding='utf8') as fileStream:
                fileStream.write(f"ترجمه محتوای صفحه : {numberPage} \n")
                fileStream.write(str(translate.text))

    except ConnectionError :
        print(f"{Fore.RED} Internet connection has been lost, please try again {Fore.RESET}")
    except TimeoutError :
        print(f"{Fore.RED} connection Time out, please try again {Fore.RESET}")

    print(f" {Fore.GREEN} Extraction of file Images was done successfully!!! {Fore.RESET}")


def extract_links(fileName) : 

    fileName = fileName
    document = PyMuPDF.open(fileName)

    PDFName = os.path.splitext(fileName)[0]

    pagesPdf = document.pages()

    haslinks = document.has_links()

        
    if haslinks :
        print(f"{Fore.YELLOW} Extract PDF Links has started {Fore.RESET}") 
        for page in pagesPdf : 

          links = page.get_links()

          if len(links) != 0 :  
            with open(f'PDF/Links/Links-{PDFName}.txt' , 'a' , encoding='utf8' ) as fileStream:
                fileStream.write(f"لینک های موجود در فایل : \n")
                for link in links : 
                    fileStream.write(f"page-{page.number + 1} : {link['uri']} \n")
        print(f" {Fore.GREEN} Extraction of file links was done successfully!!! {Fore.RESET}")
    else : 
         print(f"{ Fore.YELLOW } There is no link in the desired file!!")
                

def Translation_Subtitle(fileName) :
   try :
    translator = Translator()
    SubtitleName = os.path.splitext(fileName)[0]
    file = open(fileName, "r")
    # fileread = file.read()
    lines = file.readlines()
    file.close()


    lines = [i for i in lines if i[:-1]]

    with open(f'Subtitles/sub-{SubtitleName}-pershian.srt' , 'a' , encoding='utf8' ) as fileStream:
      print(f"{Fore.YELLOW} Subtitle translation has started {Fore.RESET}")
      for line in lines : 
        line = line.strip()
        translateLine =  translator.translate(line , 'fa' , 'en')
        fileStream.write(str(translateLine.text)+'\n')
        sleep(1)
   except ConnectionError :
        print(f"{Fore.RED} Internet connection has been lost, please try again {Fore.RESET}")
   except TimeoutError :
        print(f"{Fore.RED} connection Time out, please try again {Fore.RESET}")

   print(f" {Fore.GREEN} The translation of Subtitle was done successfully!!! {Fore.RESET}")



if typeWork == '1' :
    print(Fore.MAGENTA+"""
    [1] Translation PDF
    [2] Extract Images
    [3] Extract Links

    """ +Fore.RESET)

    pdfWork = input(f"{Fore.MAGENTA} Which one do you want to do? ??? {Fore.RESET}") 

    if pdfWork == '1' :
      fileName = input(f" {Fore.YELLOW} Enter the desired pdf file address: {Fore.RESET}")
      Translation_Pdf(fileName=fileName)
    elif pdfWork == '2' :
      fileName = input(f" {Fore.YELLOW} Enter the desired pdf file address: {Fore.RESET}")
      extract_images(fileName=fileName)
    elif pdfWork == '3' :
      fileName = input(f" {Fore.YELLOW} Enter the desired pdf file address: {Fore.RESET}")
      extract_links(fileName=fileName)   
    else :
        print(f"{Fore.RED} The value entered is incorrect, please try again!! {Fore.RESET}")  
elif typeWork == '2' :
      fileName = input(f" {Fore.YELLOW} Enter the desired pdf file address: {Fore.RESET}")
      Translation_Subtitle(fileName=fileName)      

else :
        print(f"{Fore.RED} The value entered is incorrect, please try again!! {Fore.RESET}")   