# importing the module needed for image manipulation
from PIL import Image, ImageDraw

# Starter code for all methods


def addBorders(imageFileName, thickness, colour, outputFileName):
    theImage = Image.open(imageFileName)
    width, height = theImage.size

    for x in range(0, width):
        y = 0
        theImage.putpixel((x, y), colour)

    theImage.show()


def addDeviders(imageFileName, rows, cols, thickness, colour, outputFileName):
    pass


def createImageFromBinary(sourceFileName, targetFileName):
    pass


def saveImageAsBinary(sourceFileName, targetFileName):
    pass
