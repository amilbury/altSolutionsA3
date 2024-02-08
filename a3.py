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

    # draw the line onto the picture thus adding the bSSorder
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


def addDividers(imageFileName, rows, cols, thickness, colour, outputFileName):
    # grabbing the image via the filename sent in
    theImage = Image.open(imageFileName)
    # grabbing the heigh and weight (tuple) from the image.size property
    width, height = theImage.size
    # creating a new instance of drawer
    drawer = ImageDraw.Draw(theImage)

    # finding the distance that will be needed between rows
    rowSpacing = height / rows
    # find the distance that will be needed between columns
    colSpacing = width / cols

    # variables to keep track of how much spacing is between
    totalRowSpaced = rowSpacing
    totalColSpaced = colSpacing

    # loop through the columns and draw a line
    for col in range(cols):
        # declaring the top left and top right of the line we want to draw
        verticleLeft = (totalColSpaced, 0)
        verticleRight = (totalColSpaced + thickness, height)

        # defining the region with the endpoints that we defined
        # inclusive of both endpoints
        picHeight = [verticleLeft, verticleRight]

        # draw the line
        drawer.rectangle(picHeight, colour, colour)

        # increment the space in between each column
        totalColSpaced += colSpacing

        # loop through the columns and draw a line
    for row in range(rows):
        # declaring the top left and top right of the line we want to draw
        horizontalLeft = (0, totalRowSpaced)
        horizontalRight = (width, totalRowSpaced + thickness)

        # defining the region with the endpoints that we defined
        # inclusive of both endpoints
        picWidth = [horizontalLeft, horizontalRight]

        # draw the line
        drawer.rectangle(picWidth, colour, colour)

        # increment the space in between each column
        totalRowSpaced += rowSpacing

    # show the image
    theImage.show()


def createImageFromBinary(sourceFileName, targetFileName):
    pass


def saveImageAsBinary(sourceFileName, targetFileName):
    pass
