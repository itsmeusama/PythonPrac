

"""from PIL import Image#import Image
from pytesseract import image_to_string#from tesseract import image_to_string
print(image_to_string(Image.open('C:/Python/Python37/Lib/site-packages/pytesseract/test.png')))
#print image_to_string(Image.open('C:/Python/Python37/Lib/site-packages/pytesseract/test-english.jpg'), lang='eng')"""


import cv2
import numpy as np
import pytesseract
from PIL import Image

#src_path = "C:/My_works/Python/MyWorks/tmp/"
src_path = "tmp/"

def get_string(img_path):
	# Read image with opencv
	img = cv2.imread(img_path)
	
	# Convert to grey
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	# Apply dilation and erosion to remove some noise
	kernel = np.ones((1, 1), np.uint8)
	img = cv2.dilate(img, kernel, iterations=1)
	img = cv2.erode(img, kernel, iterations=1)
	
	cv2.imwrite(src_path + "remove_noise.png", img)
	
	# Apply threshold to get image with only black and white
	img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
	cv2.imwrite(src_path + "thres.png", img)
	
	# Recongnize text with tesseract for python
	#resut = pytesseract.image_to_string(Image.open(src_path + "thres.png"))
	#pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\tesseract.exe'
	#resut = pytesseract.image_to_string(Image.open(src_path + "thres.png"))
	resut = pytesseract.image_to_string(src_path + "thres.png")
	
	return result

print('--- Start recognize text from image ---')
print(get_string(src_path + "1.png") )
print("------ Done -------")
