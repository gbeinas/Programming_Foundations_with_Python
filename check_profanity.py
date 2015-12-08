# -*- coding: cp1253 -*-


def read_text():
    quotes = open("C:\Users\ΓΙΩΡΓΟΣ\Desktop\Programming_Foundations_with_Python\movie_quotes.txt")
    file_content = quotes.read()
    print("The content of the txt file is " + file_content)

read_text()
