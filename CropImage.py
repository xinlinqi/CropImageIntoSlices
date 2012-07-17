#-*- coding:utf-8-*-
'''
	@author: xinlinqi
	2012.07.17
'''

from PIL import Image
import os
from images2gif import writeGif
'''
	pImage: Absolute Path of image
	pColumn: Crap the Image into pColumn columns
	pRows: Crap the Image into pRows rows
'''
def CrapImageIntoSlices(pImage, pColumns, pRows):
	try:
		sImage = Image.open(pImage)
	except:
		print 'Image Not Found!'
		return;
	mWidth = sImage.size[0]
	mHeight = sImage.size[1]
	sColumn = mWidth / pColumns
	sRow = mHeight / pRows
	mWidth = sColumn * pColumns
	mHeight = sRow * pRows
	for iWidth in  range(0, mWidth, sColumn):
		for iHeight in range(0, mHeight, sRow):
			fName = os.path.join('output', 'tiled_%d_%d.png.'%(iWidth, iHeight))
			print "Creating Image " + fName;
			print "Croping from (%d, %d) to (%d, %d)."%(iWidth, iHeight, min(iWidth + sColumn, mWidth), min(iHeight + sRow, mHeight))
			mBuffer = Image.new("RGBA", [sColumn, sRow], (0, 0, 0, 0))
#			mTile = sImage.crop((iWidth, iHeight, min(iHeight + sRow, mHeight), min(iWidth + sColumn, mWidth)))
			mTile = sImage.crop((iWidth, iHeight, min(iWidth + sColumn, mWidth), min(iHeight + sRow, mHeight)))
			mBuffer.paste(mTile, (0, 0))
			mBuffer.save(fName, 'PNG')
	
	mImageFiles = sorted((fn for fn in os.listdir('output/') if fn.endswith('png')))
	os.chdir('output/')
	mImages = [Image.open(fn) for fn in mImageFiles]
	writeGif('%s_result.gif'%(pImage.split('.')[0]), mImages, duration=0.2)
		
print "-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-"
print "\t1. Only png images are supported right now."
print "\t2. Putting the source image to the same directory."
print "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"
pImage = raw_input("Please enter the image name: ")
while True:
	try:
		Image.open(pImage)
		break
	except:
		print "Error, File Not Found!\n"
		pImage = raw_input("Please enter the image name: ")
while True:
	try:
		pColumns = int(raw_input("Enter the colums to be sliced(1, 2, 3...etc):"))
		pRows = int(raw_input("Enter the rows to be sliced(1, 2, 3...etc):"))
		break
	except:
		print "Error, Digits are required.\n"
		pColumns = int(raw_input("Enter the colums to be sliced(1, 2, 3...etc):"))
		pRows = int(raw_input("Enter the rows to be sliced(1, 2, 3...etc):"))
#mSourceImages = [fn for fn in os.listdir('.') if fn.endswith('png')]
CrapImageIntoSlices(pImage, pColumns, pRows)

print "Done Succefully.\n"