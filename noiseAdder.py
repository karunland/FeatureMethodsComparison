import random
import cv2
import sys


def add_noise(img):
    row, col = img.shape
    number_of_pixels = random.randint(10, 100)
    for i in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        img[y_coord][x_coord] = 255

    number_of_pixels = random.randint(10, 100)
    for i in range(number_of_pixels):

        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)

        img[y_coord][x_coord] = 0
    return img


if __name__ == '__main__':
    imgReference = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('./images/salt-and-pepper-george.jpeg', add_noise(imgReference))
