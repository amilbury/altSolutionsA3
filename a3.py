# importing the module needed for image manipulation
from PIL import Image, ImageDraw

# Starter code for all methods


def addBorders(imageFileName, thickness, colour, outputFileName):
    # grabbing the image via the filename sent in
    theImage = Image.open(imageFileName)
    # grabbing the heigh and weight (tuple) from the image.size property
    width, height = theImage.size

    # creating a new instance of drawer
    drawer = ImageDraw.Draw(theImage)

    # setting the bounds for the top border of the picture
    upperLeft1 = (0, 0)
    bottomRight1 = (width, thickness)

    # defining the region with the endpoints that we defined
    region1 = [upperLeft1, bottomRight1]  # inclusive of both endpoints

    # draw the line onto the picture thus adding the border
    drawer.rectangle(region1, colour, colour)

    # setting the bounds for the left border of the picture
    upperLeft2 = (0, 0)
    bottomRight2 = (thickness, height)

    # defining the region with the endpoints that we defined
    region2 = [upperLeft2, bottomRight2]  # inclusive of both endpoints

    # draw the line onto the picture thus adding the border
    drawer.rectangle(region2, colour, colour)

    # setting the bounds for the bottom border of the picture
    upperLeft3 = (0, height - thickness)
    bottomRight3 = (width, height + 5)

    # defining the region with the endpoints that we defined
    region3 = [upperLeft3, bottomRight3]  # inclusive of both endpoints

    # draw the line onto the picture thus adding the border
    drawer.rectangle(region3, colour, colour)

    # setting the bounds for the right border of the picture
    upperLeft4 = (width - thickness, 0)
    bottomRight4 = (width, height)

    # defining the region with the endpoints that we defined
    region4 = [upperLeft4, bottomRight4]  # inclusive of both endpoints

    # draw the line onto the picture thus adding the border
    drawer.rectangle(region4, colour, colour)

    # show the image
    theImage.show()
    # save the image to the file with specified file name
    theImage.save(outputFileName)


def addDeviders(imageFileName, rows, cols, thickness, colour, outputFileName):
    pass


def createImageFromBinary(sourceFileName, targetFileName):
    pass


def saveImageAsBinary(sourceFileName, targetFileName):
    pass
