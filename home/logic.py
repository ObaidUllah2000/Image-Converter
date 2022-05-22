from ctypes import sizeof
import cv2
from PIL import Image
from pytesseract import pytesseract
from PIL import Image
import nltk
import pyttsx3
import string
import os

def convert(iobj,cap):
    pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # img_path = os.path.join()
    img_path = "A:/Web Development/Django Coding/Project_2/"+iobj.image.url
    img1= Image.open(img_path)
    # img1= cv2.imread(img_path)
    # width, height = img1.size
    # print(width, height)

    text = pytesseract.image_to_string(img1)
    text1 = str(text)

    sen = nltk.sent_tokenize(text1)
    print(type(sen))
    print(sen)
    new_sent1 = []
    for i in sen:
        j = i.replace("\n"," ")
        new_sent1.append(j)

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    # print(rate)
    engine.setProperty('rate', 150 )
    engine.setProperty('voice', voices[0].id  )
    engine.save_to_file(new_sent1,'A:/Web Development/Django Coding/Project_2/media/audios/'+cap+'.mp3')
    # engine.say(new_sent1)
    engine.runAndWait()

    return text
