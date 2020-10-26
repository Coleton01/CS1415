from images import Image




def shrink(image,factor):
    """builds and returns a new image which is smaller copy of the argument image, by the factor argument."""
    width=image.getWidth()
    height = image.getHeight()
    new=Image(width//factor, height//factor)
    oldY=0
    newY=0
    while oldY < height-factor:
        oldX=0
        newX=0
        while oldX < width -factor:
            oldP=image.getPixel(oldX,oldY)
            new.setPixel(newX,newY,oldP)
            oldX+= factor
            newX +=1
        oldY += factor
        newY +=1
    return new


def grayscale(image):
    """converts sample image to grayscale"""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b)= image.getPixel(x,y)
            r = int(r * 0.299)
            g = int(g* 0.587)
            b = int(b * 0.114)
            lum = (r + g + b)
            image.setPixel(x, y, (lum,lum,lum))   #adjusts rbg values to account for luminesence. 
    
    return image

def sepia(image):
    """This function will return a sepia value for the image"""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (red,green,blue)=image.getPixel(x,y)
            if red < 63:
                red = int(red *1.1)
                blue= int(blue * 0.9)
            elif red <192:
                red= int(red*1.15)
                blue= int(blue * 0.85)
            else:
                red= min(int(red * 1.08),225)
                blue= int(blue * 0.93)
    
    return image



    
I=Image("C:/Users/coled/Pictures/pytest.gif")
#imageNew=shrink(I, 4)
#imageNew.save("C:/Users/coled/Pictures/shrinkpytest.gif")
I2= Image("C:/Users/coled/Pictures/shrinkpytest.gif")
I2.draw()
I3=grayscale(I2)
I3.draw()
I4=sepia(I3)
I4.draw()
print("im done")
