# Image-Converter
This is an image converter website created using Django HTML CSS JS making use of python libraries nltk pytesseract etc. for conversion of image to text and audio format

ABSTRACT

The aim of this project is to develop an image to text, text to speech, and image to speech converter webpage. With the development of technology, the content of image is needed in text format in cases of registrations which include information passing where only some part of information present in the image is required. Typing the whole thing takes a lot of time thus this method of text conversion is the best solution which saves a lot a time as well as eases the task. Sometimes this text is needed in audio format, then again recording the whole thing may not be as efficient. But using a speech generator is a great approach towards effective information passing in the form of audio without actually recording itIn this Project input text or image is given and respected speech or text or both is generated as output. 
The reason why we have chosen this project is because of its real-life application where it is a necessity to extract the text from an image as mentioned above and speech for the reason that even if a person who is unable to read wants to know what’s in the image or the text, he can understand it just by listening to the speech. The way we are going to design it is in such a way that even layman would be able to convert the text, image to corresponding speech, text. This is going to be a webpage where a person from anywhere in the world can access and perform image to text, text to speech and image to speech.

SOFTWARE - HARDWARE REQUIREMENTS

Software used to build:
	Visual Studio Code
	A suitable web browser (preferably Google Chrome) 
	HTML, CSS, Java Script
	Django Framework
	Python Libraries
	Pytesseract
	Pyttsx
	The Natural Language Toolkit or NLTK
	Open CV 

Hardware Required to run:
	None (Web App can be used on any Web Browser.)
1.INTRODUCTION

1.1	OBJECTIVE
With the development of technology, the content of image is needed in text format in cases of registrations which include information passing where only some part of information present in the image is required. 
Typing the whole thing or the extraction of audio from text this audio being properly delivered is very time consuming as well as difficult, and thus this is the best solution which we have come up with.
The objective of this project to provide ease for people trying to extract text from all kinds of images and to allow people to listen to what is written in that image


2. LITERATURE SURVEY

2.1 EXISTING SYSTEM

	The existing applications are brandfilling.com, onlineconverter, orctoedit.com etc.
	These applications do take the image in but their efficiency is not very good. Some of the texts were not being extracted from some images. 
	These applications do not read out loud the texts.
	They also ask for registrations, logins etc. while not even providing the facility to copy the text from that image unlike our application.


2.2 PROPOSED SYSTEM

	This Application aims to provide an interface which helps the user to extract the text as well as the speech or audio file while reading the text out loud without even asking for a single private information about the user. He can copy the text as well as download the audio file while being able to upload any new image any no. of times and play the text audio file as many times as one wants.
	This application provides simplicity with any novice internet user being able to extract text and listen the text. 
	The code for this application is made in such a way that any programmer can understand it because we used very easy to use softwares and libraries.



3. SOFTWARE USED
•	VISUAL STUDIO CODE: Visual Studio Code is a source-code editor that can be used with a variety of programming languages, including Python, Java, C++ JavaScript and C. It is based on Electron framework, which is used to develop Web applications that run on the Blink layout engine. Visual Studio Code employs the same editor component (code named "Monaco") used in Azure DevOps (formerly called Visual Studio Online and Visual Studio Team Services). It has a user friendly UI that makes it easy to develop applications. Simply extensions can be downloaded which makes tedious and time consuming tasks very easy.
•	HTML: HTML (Hypertext Markup Language) is the code that is used to structure a web page and its content. 
			For example, content could be structured within a set of paragraphs, a list of bulleted points, or using images and data tables.
•	CSS: CSS is used for defining the styles for web pages.
			It describes the look and formatting of a document which is written in a markup language. It is generally used with HTML to change the style of web pages and user interfaces.
•	Java Script: JavaScript is a text-based programming language used both on the client-side and server-side that allows you to make web pages interactive.
			   Where HTML and CSS are languages that give structure and style to web pages, JavaScript gives web pages interactive elements that engage a user.

•	Django: Django is a Python-based free and open-source web framework that follows the model–template–views architectural pattern
Django is a collection of Python libs allowing you to quickly and efficiently cre-ate a quality Web application, and is suitable for both frontend and backend.
•	PYTHON: Python is an interpreted, high level and general-purpose pro-gramming language. It was created by Guido van Rossum, and released in 1991. Python's design philosophy emphasizes code readability with its nota-ble use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python can be used on a server to create web applications.
•	Pytesseract: Pytesseract is a wrapper for Tesseract-OCR Engine. It is also useful as a stand-alone invocation script to tesseract, as it can read all image types supported by the Pillow libraries, including jpeg, png, gif, bmp, tiff, and others.
•	Pillow: Python Imaging Library (PIL) is a free and open-source library for the Python that adds support for opening, manipulating, and saving many differ-ent image file formats.
•	Pyttsx: pyttsx is a Python package supporting common text-to-speech en-gines, 
•	OpenCV: OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products. Be-ing a BSD-licensed product, OpenCV makes it easy for businesses to utilize and modify the code.


4.REQUIREMENTS

4.1 RUNNING THE Web App ON LOCAL SERVER
The requirements to run the Web App successfully on local server are-
•	Any code editor (preferably VS Code)
•	Versions of Python and other libraries required:
Package	Version
python	3.10.1
Html	5
CSS	4
Django	3.2.9
Pillow 	8.4.0
Pyttsx3	2.90
OpenCV
	4.5.5
nltk	1.4.3


         Table 4.1.1: Requirements
4.2 RUNNING THE Deployed Web App
One only needs Internet and a browser to view the Web App. Works better when viewed on Laptop/PC.


5. IMPLEMENTATION
5.1 Sample Code- Code runner(manage.py)
django-admin is Django’s command-line utility for administrative tasks. 
In addition, manage.py is automatically created in each Django project. It does the same thing as django-admin but also sets the DJANGO_SETTINGS_MODULE environment variable so that it points to your project’s settings.py file.

 


Admin.py (responsible for registrations of models)
 
Urls.py (responsible for guiding the route URLs to views)
 
Views.py
A view function, or view for short, is a Python function that takes a web request and returns a web response. This response can be the HTML contents of a web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really. The view itself contains whatever arbitrary logic is necessary to return that response. This code can live anywhere you want, as long as it’s on your Python path. There’s no other requirement–no “magic,” so to speak. For the sake of putting the code somewhere, the convention is to put views in a file called views.py, placed in your project or application directory.
Here we have created home view which is the base and the first thing to show up when our website is launched. It takes the data from html form and then saves the image along with its caption and after processing the image, sends or redirect the im-age and text back to the html page.
 
Models.py
A model is the single, definitive source of information about your data. It contains the es-sential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.
The basics:
•	Each model is a Python class that subclasses django.db.models.Model.
•	Each attribute of the model represents a database field.
•	With all of this, Django gives you an automatically-generated database-access API; 
 
Logic.py
This is the file which is responsible for processing the images, extracting the text and generating an audio file in speech format for the text.
 
 
Settings.py
settings.py is a core file in Django projects. It holds all the configuration val-ues that your web app needs to work; database settings, logging configuration, where to find static files, API keys if you work with external APIs, and a bunch of other stuff.
Templates contain the files which we are using for the front-end which is respon-sible for the interface. Templates include the html files.
Static files are the files which are being used in the templates. This folder in-cludes all the images, CSS files and JavaScript used for the project.
Media files are responsible for storing the images we get from the user the audio files which we generated after the text extraction.

 

6. LIMITATIONS, FUTURE ENHANCEMENTS & CONCLUSION

6.1	LIMITATIONS
Some OpenCV, NLP and OCR algorithms could have been employed but due to complex nature of image and texts, applying those could result in more complex code with anomalies and in efficient results. Thus those were not used.

6.4 FUTURE ENHANCEMENTS
Many more improvements are still possible such as sentiment analysis where humor, sarcasm is identified using advanced Natural language Processing. There is also creation of model which can generate a doc based on the text while noting the location of texts and their font styles. The audio file plays the only part in the text which is needed to listen.

6.5 CONCLUSION
The Use of the afore mentioned libraries and the techniques proved to be very beneficial especially in terms of logic which can be understood with ease.
The Natural language Processing usage has brought the audio format to a very excellent height of understanding where sentences and words were separated accordingly. 
This application will be beneficial for the people from all walks of life, since text fillings are a necessity for all kinds of digital forms. Using this, they extract any king of text they want from any image and also listen to what is written in the image with minimal errors also in correct English format (natural language). 




References

https://docs.djangoproject.com/en/4.0/
https://www.w3schools.com/tags/default.asp
https://www.w3schools.com/css/default.asp
https://www.w3schools.com/js/default.asp
https://www.youtube.com/watch?v=JxzZxdht-XY
https://codewithharry.com/videos/python-tutorials-for-absolute-beginners-127
https://www.w3schools.com/python/default.asp
