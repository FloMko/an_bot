
import argparse
import numpy as np
from PIL import Image
from os.path import abspath


# grayscale level values from:
# http://paulbourke.net/dataformats/asciiart/
# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# 10 levels of gray
gscale2 = '@%#*+=-:. '


def getAverageL(image):
    """
    Given PIL Image, return average value of grayscale value
    """
    # get image as numpy array
    im = np.array(image)
    # get the dimensions
    w, h = im.shape
    # get the average
    return np.average(im.reshape(w * h))


def covertImageToAscii(fileName, cols, scale, moreLevels=True):
    """
    Given Image and dimensions (rows, cols), returns an m*n list of Images
    """
    # declare globals
    global gscale1, gscale2
    # open image and convert to grayscale
    image = Image.open(fileName).convert('L')
    # store the image dimensions
    W, H = image.size[0], image.size[1]
    print("input image dims: %d x %d" % (W, H))
    # compute tile width
    w = W / cols
    # compute tile height based on the aspect ratio and scale of the font
    h = w / scale
    # compute number of rows to use in the final grid
    rows = int(H / h)

    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))

    # check if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)

    # an ASCII image is a list of character strings
    aimg = []
    # generate the list of tile dimensions
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)
        # correct the last tile
        if j == rows - 1:
            y2 = H
        # append an empty string
        aimg.append("")
        for i in range(cols):
            # crop the image to fit the tile
            x1 = int(i * w)
            x2 = int((i + 1) * w)
            # correct the last tile
            if i == cols - 1:
                x2 = W
            # crop the image to extract the tile into another Image object
            img = image.crop((x1, y1, x2, y2))
            # get the average luminance
            avg = int(getAverageL(img))
            # look up the ASCII character for grayscale value (avg)
            if moreLevels:
                gsval = gscale1[int((avg * 69) / 255)]
            else:
                gsval = gscale2[int((avg * 9) / 255)]
            # append the ASCII character to the string
            aimg[j] += gsval

    # return text image
    return aimg


# main() function
def main(file_id):

    imgFile = abspath('./pic/'+file_id)
    outFile = abspath('./pic/'+file_id+'lum')
    # set scale default as 0.43, which suits a Courier font
    scale = 0.43
    # set cols
    cols = 80
    print('generating ASCII art...')
    # convert image to ASCII text
    aimg = covertImageToAscii(imgFile, cols, scale,)

    # open a new text file
    f = open(outFile, 'w')
    # write each string in the list to the new file
    for row in aimg:
        f.write(row + '\n')
    # clean up
    f.close()
    print("ASCII art written to %s" % outFile)

