import os
from PIL import Image
from fpdf import FPDF

folderPath = input("Folder path: ")

def imageNames(folderPath):
    allFileNames = os.listdir(folderPath)
    allImageNames = []
    for image in allFileNames:
        if ".jpg" in image:
            allImageNames.append(image)
    return allImageNames

def preNumber():
    allPrefix = []
    uniqueNumbers = []
    for image in imageNames(folderPath):
        allPrefix.append(image.split('-')[0])
    uniqueNumbers = list(set(allPrefix))
    return uniqueNumbers

def makePdf():
    i = 0
    x,y,w,h = 0, 0, 200, 250
    imageList = []
    for x in range(0, len(sorted(preNumber()))):
        for image in imageNames(folderPath):
            if sorted(preNumber())[x] in image:
                imageList.append(image)
                print(imageList)
            pdf = FPDF('P','mm','A4')
            for img in imageList:
                pdf.add_page()
                pdf.image(folderPath + img,x,y,w,h)
            pdf.output(folderPath + sorted(preNumber())[x] + ".pdf","F")
        imageList = []
makePdf()
print("PDF Generating done.")

    






