import cv2 
import matplotlib.pyplot as plt
import os, sys
arg1 = sys.argv[1]

if (os.path.exists(f'./images/{arg1}')):
    img = cv2.imread(f'./images/{arg1}')
else:
    print('File not found')
    exit()

print('Image shape:', img.shape)
print('Image data type:', img.dtype)

img = cv2.resize(img, (0,0), fx = 0.3, fy = 0.3)

print('Image shape:', img.shape)
print('Image data type:', img.dtype)

# img stringinde . kadar olan kismi kesip yeni bir degiskene atiyoruz
img_name = arg1.split('.')[0]

cv2.imwrite(f'./images/{img_name}_resized.jpeg', img)
