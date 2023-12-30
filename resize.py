import cv2
import os
import sys

def resize_image_with_fixed_height(img, desired_height):
    height, width = img.shape[:2]
    aspect_ratio = width / height
    new_width = int(desired_height * aspect_ratio)
    
    return cv2.resize(img, (new_width, desired_height))

if __name__ == '__main__':
    name = sys.argv[1]
    resolution = int(sys.argv[2])  # sys.argv ile alınan inputu integer'a dönüştür

    if os.path.exists(name):
        img = cv2.imread(name)
    else:
        print('File not found')
        exit()

    print('Image shape:', img.shape)

    img = resize_image_with_fixed_height(img, resolution)

    print('New image shape:', img.shape)

    img_name = os.path.splitext(os.path.basename(name))[0]

    cv2.imwrite(f'./images/{img_name}_resized.jpeg', img)
