from PIL import Image
from colorama import Fore, Back, Style

def rgbArrayConstructor(im):
    rgbArray = [[(0,0,0)]*im.size[0] for _ in range(im.size[1])]
    print(pixels)
    print(pixels[0,0])
    for i in range(im.size[1]):
        for j in range(im.size[0]):
            rgbArray[i][j] = pixels[j,i]
    print("Successfully Constructed Pixel Matrix!")
    return rgbArray

def brightnessArrayConstructor(rgbArray, brightnessAlgo = 0, invert = False):
    brightArray = [[0]*len(rgbArray[0]) for _ in range(len(rgbArray))]
    for i in range(len(rgbArray)):
        for j in range(len(rgbArray[i])):
            brightArray[i][j] = determineBrightness(rgbArray[i][j][0],rgbArray[i][j][1],rgbArray[i][j][2], brightnessAlgo, invert)
    print("Brightness Array Constructed!")
    return brightArray

def determineBrightness(r,g,b, Algo, invert = False):
    if (invert):
        r = 255 - r
        g = 255 - g
        b = 255 - b
    if (Algo == 0): # Average
        return (r+g+b)/3
    elif(Algo == 1): # Minmax
        return (max(r,g,b)+min(r,g,b))/2
    elif(Algo == 2): # Luminosity
        return 0.21 * r + 0.72 * g + 0.07 * b
    else:
        print("Algorithm couldn't be determined, returning 0")
        return 0

def ASCIIArrayConstructor(charSet, brightArray):
    ASCIIArray = [[""]*len(brightArray[0]) for _ in range(len(brightArray))]
    for i in range(len(brightArray)):
        for j in range(len(brightArray[i])):
            index = min(int((brightArray[i][j] * len(charSet))// 255),len(charSet)-1)
            # print(index)
            ASCIIArray[i][j] = charSet[index]
    print("ASCII Array Constructed")
    return ASCIIArray

def ASCIIArrayToString(ASCIIArray):
    output = ""
    for i in range(len(ASCIIArray)):
        for j in range(len(ASCIIArray[i])):
            output += ASCIIArray[i][j] * 3
        output += "\n"
    return output

if (__name__ == '__main__'):
    print("Opening Image...")
    filename = input("Enter your desired image filename: ")
    im = Image.open(filename)
    print("Image Opened Successfully!")
    print("Image Size", im.size)
    print("Resizing image...")
    maxsize = int(input("Enter the max size of your ascii art: "))
    im.thumbnail((maxsize,maxsize))
    im.save("H.jpg")
    # print(im.format, im.size, im.mode)
    print("Loading image...")
    pixels = im.load()
    print("Image Loaded")

    charSet = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

    pixelMatrix = rgbArrayConstructor(im)
    algo = int(input("What brightness algorithm do you want to use? (Avg = 0, minmax = 1, luminosity = 2) "))
    invert = (input("Invert colors? ").lower() == 'y')
    brightMatrix = brightnessArrayConstructor(pixelMatrix, algo, invert)
    ASCIIArray = ASCIIArrayConstructor(charSet, brightMatrix)

    file = open("ASCII.txt", 'w')
    file.write(ASCIIArrayToString(ASCIIArray))
    file.close()

    print(Fore.GREEN + ASCIIArrayToString(ASCIIArray))