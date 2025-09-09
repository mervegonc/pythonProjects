# -*- coding: utf-8 -*-
#substing
message = "Hello Mfkrs"
# print(message[0:2])
# newMessage = message[:2]
# print(newMessage)
#lenght
# print(len(message))

# newMessage2 = message[len(message)-1:len(message)]
# print(newMessage2)
#lower upper Ascii
# ASCII (American Standard Code for Information Interchange)
# is the most common character encoding format for text data
# in computers and on the internet.
#print(message.lower())
#print(message.upper())
#replace
#print(message.replace("o", "ö"))

#split and strip 6 yıl önce 20257
#boşluğğa göre ayırır/ seperate according to blank spaces between words
#strip
#baştaki ve sondaki boşlukları atar/ its clear the blank spaces at begining and end 
knowledge = " Merve Göncü 23 Ankara ".strip()
print(knowledge.split())
print(knowledge.split(" ")) #we said seperate according to blanks but default mode is already just like that

#if the data cames to us like this, we can easyly fix with split
knowledge1 = " Merve;Göncü;23;Ankara ".strip()
print(knowledge1.split(";"))
print("Name: "+ knowledge1.split(";")[0])
#input
name = input("What is your name?(enter your name):")
number = input("First Number:")
number1 = input("Second Number:")
print(int(number) + int(number1))