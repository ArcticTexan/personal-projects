from PIL import Image
import numpy as np
import math
import os

def getTileColor(inpt: Image.Image):
    rTotal, gTotal, bTotal = 0, 0, 0
    width, height = inpt.size
    for i in range(width):
        for j in range(height):
            # print(inpt.getpixel((i,j)))
            r,g,b = inpt.getpixel((i,j))[:3]
            rTotal += r
            gTotal += g
            bTotal += b
    rTotal /= width * height
    gTotal /= width * height
    bTotal /= width * height
    return rTotal, gTotal, bTotal

def imageSlicer(inpt: Image.Image, tileWidth: int, tileHeight: int):
    if min(tileWidth,tileHeight) <= 0:
        print("Tiles must have positive dimensions!")
        raise ValueError("imageSlicer function needs positive args")
    inpt = inpt.crop([0,0,inpt.width - (inpt.width % tileWidth), inpt.height - (inpt.height % tileHeight)]) # Normalizing target by cutting off corners to fit the dimensions of our mosaic tiles
    imgAry = [[Image.new('RGB',(1,1))]*(inpt.height // tileHeight) for _ in range(inpt.width // tileWidth)]
    for x in range(inpt.width // tileWidth):
        for y in range(inpt.height // tileHeight):
            imgAry[x][y] = inpt.crop([x * tileWidth, y * tileWidth,(x + 1) * tileWidth - 1, (y + 1) * tileWidth - 1])
    # disImgAry(imgAry)
    return imgAry

def disImgAry(imgAry):
    script_dir = os.path.dirname(__file__)
    for x in range(len(imgAry)):
        for y in range(len(imgAry[x])):
            rel_path = "stitch/imgAry" + str(x) + "_" + str(y) + ".png"
            abs_file_path = os.path.join(script_dir, rel_path)
            imgAry[x][y].save(abs_file_path)

def imgAryToTileColor(imgAry):
    colorAry = [[(0,0,0)]*len(imgAry[0]) for _ in imgAry]
    for i in range(len(imgAry)):
        for j in range (len(imgAry[i])):
            colorAry[i][j] = getTileColor(imgAry[i][j])
    return colorAry

def colorDistance(color1,color2): # Calculates the distance between 2 colors, using the euclidean metric, might be worth using Oklab eventually
    rdiff = (color1[0] - color2[0])**2
    gdiff = (color1[1] - color2[1])**2
    bdiff = (color1[2] - color2[2])**2
    return math.sqrt(rdiff+gdiff+bdiff)

def pixilate(inpt, width, height):
    imgAry = imageSlicer(inpt, width, height)
    colorAry = imgAryToTileColor(imgAry)
    flat_list = []
    for j in range(len(imgAry[0])):
        for i in range(len(imgAry)):
            r = int(colorAry[i][j][0])
            g = int(colorAry[i][j][1])
            b = int(colorAry[i][j][2])
            flat_list.append((r,g,b))
    output = Image.new('RGB', (inpt.width // width, inpt.height // height))
    output.putdata(flat_list)
    output.resize(inpt.size,Image.NEAREST)
    return output

def loadImgs():
    file_directory = "tiles/mc_items"
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir,file_directory)
    entries = os.listdir(abs_file_path)
    tilesAry = []
    for i in range(len(entries)):
            # Process the file
            print(f"Processing file: {entries[i]}")
            # Add your file processing logic here
            currImage = Image.open(os.path.join(abs_file_path,entries[i]))
            currImage = currImage.crop([0,0,min(currImage.size),min(currImage.size)])
            tilesAry.append(currImage)
            tilesAry[-1].convert("RGB")
    print("Tiles have been processed!")
    return tilesAry

def tilesAryToColorAry(tilesAry):
    colorAry = []
    for i, image in enumerate(tilesAry):
        # print("Image Being Analyzed is image ", i)
        colorAry.append(getTileColor(image))
    return colorAry

def findClosestColor(targetColor, tileAry, colorAry = []):
    if colorAry == []:
        colorAry = tilesAryToColorAry(tileAry)
    candidate = tileAry[0]
    currDist = colorDistance(targetColor, colorAry[0])
    for i in range(len(colorAry)):
        if (colorDistance(targetColor,colorAry[i]) < currDist):
            currDist = colorDistance(targetColor,colorAry[i])
            candidate = tileAry[i]
    return candidate

def PhotoMosaic(tiles, target, tileWidth, tileHeight):
    imgAry = imageSlicer(target, tileWidth, tileHeight)
    colorAry = imgAryToTileColor(imgAry)
    tileAry = [[Image.new('RGB',(1,1))] * len(imgAry[0]) for _ in range(len(imgAry))]
    tileColorAry = tilesAryToColorAry(tiles)
    print("Finding tiles for each section, this might take a minute...")
    for i in range(len(imgAry)):
        # print("Row", i + 1, "of", len(imgAry))
        for j in range(len(imgAry[i])):
            # amprint("Column ", j + 1, " of ", len(imgAry[i]), sep="")
            tileAry[i][j] = findClosestColor(colorAry[i][j], tiles, tileColorAry) # Finds the tile corresponding to the
            tileAry[i][j] = tileAry[i][j].resize((tileWidth * 32, tileHeight * 32), Image.NEAREST)
        # print("")
    print("Done! Stitching together image now")
    output = Image.new('RGB', (target.width * 32, target.height * 32))
    for i in range(len(imgAry)):
        for j in range(len(imgAry[i])):
            # tileAry[i][j].save('stitch/_img'+str(i)+'_'+str(j)+".png")
            output.paste(tileAry[i][j],(tileWidth * 32 * i, tileHeight * 32 * j))
    return output


if __name__ == '__main__':
    print("Starting PhotoMosaic!")
    fname = input("Enter the filename of the target image: ")
    target = Image.open(fname)
    tileSpace = loadImgs()
    tileWidth = tileHeight = 8
    target = target.convert('RGB')
    target.thumbnail((256,256))
    output = PhotoMosaic(tileSpace, target, tileWidth, tileHeight)
    print("All Done, enjoy your image!")
    output.thumbnail((1000,1000))
    output.save("output.png")
    
