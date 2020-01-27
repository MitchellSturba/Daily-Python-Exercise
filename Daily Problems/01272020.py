#For today I decided to just make a program that creates a hundred files and writes something in them lol
import os

#Writes the files
def createHundredFiles(fileNames, WhatToWrite):
    #Just makes a hundred files and writes inside them
    for i in range(100):
        fl = open(fileNames + str(i + 1) + '.txt', 'w')
        fl.write(WhatToWrite)
        fl.close()

if __name__ == '__main__':
    #Get the inputs
    myFile = input('What would you like to name the files? ')
    text = input('What would you like inside the files?')

    #calls the function
    createHundredFiles(myFile, text)