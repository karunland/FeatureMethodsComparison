import cv2
import os
import sys

if __name__ == '__main__':
    name = sys.argv[1]

    if os.path.exists(name):
        img = cv2.imread(name)
    else:
        print('File not found')
        exit()

    imgScaled = cv2.resize(img, None, fx=1.5, fy=1.5,
                          interpolation=cv2.INTER_CUBIC)

    img_name = os.path.splitext(os.path.basename(name))[0]

    cv2.imwrite(f'./images/{img_name}_scaled.jpeg', imgScaled)
