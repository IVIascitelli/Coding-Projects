#This program takes text files of numbers from a given directory,
#takes an average of those numbers, then graphs them using graphics.py

import os
from graphics import *

def processFile(fname):
    strippedList = []
    filesList = []
    str1 = "C:/Users/Robert/Desktop/"
    filedir = str1 + fname + "/"
    fileList = os.listdir(filedir)
    for doc in fileList:
        if doc[-4:] == ".txt":
            strippedList.append(doc[:-4])
    for filename in strippedList:
        infile = open(filename,'r')
        numList = infile.readlines()
        filesList.append(numList)
