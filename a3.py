# importing the module needed for image manipulation
from PIL import Image, ImageDraw

# Starter code for all methods


def addBorders(imageFileName, thickness, colour, outputFileName):
    # grabbing the image via the filename sent in
    theImage = Image.open(imageFileName)
    # grabbing the heigh and weight (tuple) from the image.size property
    width, height = theImage.size

    # just to test that we can actually draw on image
    # along the whole width
    for x in range(0, width):
        # only on the first level / pixel
        y = 0
        # set the pixel color to yellow
        theImage.putpixel((x, y), colour)

    # show the image
    theImage.show()


def addDeviders(imageFileName, rows, cols, thickness, colour, outputFileName):
    pass


def createImageFromBinary(sourceFileName, targetFileName):
    pass


def saveImageAsBinary(sourceFileName, targetFileName):
    pass
