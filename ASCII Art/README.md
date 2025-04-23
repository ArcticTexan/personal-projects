# ASCII Art Generator

This project takes an image file and converts it to ASCII art using grayscale mapping. It outputs the result in the terminal and also saves it to a text file in the local directory as ASCII.txt.

## How to Use

1. Clone the repo
2. Run the script with an image path
3. The code will prompt you to choose the maximum length/width, as well as asking which brightness algorithm to use
## Example

### Input:

```bash
$ python3 main.py
Opening Image...
Enter your desired image filename: Squirrel.jpg
Image Opened Successfully!
Image Size (4160, 6240)
Resizing image...
Enter the max size of your ascii art: 100
Loading image...
Image Loaded
<PixelAccess object at 0x7f0158d79490>
(95, 93, 89)
Successfully Constructed Pixel Matrix!
What brightness algorithm do you want to use? (Avg = 0, minmax = 1, luminosity = 2) 0
Invert colors? n
Brightness Array Constructed!
ASCII Array Constructed
```

![Squirrel](https://github.com/user-attachments/assets/177dbb00-98e6-4b5c-8008-8b728e04db60)
Photo by Connor McManus: https://www.pexels.com/photo/brown-squirrel-on-brown-wooden-stamp-12317783/

### Output:

![image](https://github.com/user-attachments/assets/070ea0b2-7268-491d-b644-db327c5b73cf)


