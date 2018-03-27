import numpy as np
from PIL import Image
import cv2
import pytesseract
    
def getImage(input_path):
    input_image = cv2.imread(input_path, 0)
    return input_image
    
def imageText(input_image):
    output_text = pytesseract.image_to_string(Image.fromarray(input_image), lang='eng+tam')
    return output_text


if __name__ == '__main__':
    input_image = getImage('MeeraTamilSample.png')
    output_text = imageText(input_image)
    print(output_text)