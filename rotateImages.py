# Simple Python Script to convert images in a folder to "JPG" format
# Resize and Rotate to key characteristics
import os
from PIL import Image

def ImageOperation(root, file_name):
	new_name = root + file_name + ".jpeg"
	im = Image.open(os.path.join(root,file_name))
	im.rotate(90).resize((128,128)).convert('RGB').save(new_name)


def main():
	images_folder = os.getcwd()
	for root, dirs, files in os.walk(images_folder, topdown=False):
		for name in files:
			ImageOperation(os.path.join(root, name))


main()