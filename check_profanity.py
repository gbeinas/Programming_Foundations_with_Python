# -*- coding: cp1253 -*-
import urllib

def read_text():
    quotes = open("C:\Users\ΓΙΩΡΓΟΣ\Desktop\Programming_Foundations_with_Python\movie_quotes.txt")
    file_content = quotes.read()
    print("The content of the txt file is " + file_content)
    quotes.close()
    check_profanity(file_content)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")
    connection.close()
read_text()
