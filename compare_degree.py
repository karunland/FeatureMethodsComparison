import cv2
import sys
import imutils
import numpy as np


def find_rotation_angle(src_pts, dst_pts):
    M, empty = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    rad = np.arctan2(M[1, 0], M[0, 0])
    return np.degrees(rad)

# homografi matrisi
# [[cos(theta), -sin(theta), tx],
#  [sin(theta), cos(theta),  ty],
#  [0,          0,           1]]

if __name__ == '__main__':
    # inputs: algorithm, reference image path, rotate degree
    algorithm = sys.argv[1]
    referencePath = sys.argv[2]
    rotateDegree = int(sys.argv[3])
    debug = int(sys.argv[4])

    print(f"\n\nAlgorithm: {algorithm}\nDegree: {rotateDegree}")

    imgReference = cv2.imread(referencePath, cv2.IMREAD_GRAYSCALE)

    if (rotateDegree == 1):
        print(f"using scaled image")
        imgAlign = cv2.imread(
            './images/george1e_resized.jpeg', cv2.IMREAD_GRAYSCALE)
    elif (rotateDegree == 2):
        print(f"adding noised image")
        imgAlign = cv2.imread(
            './images/salt-and-pepper-george400.jpeg', cv2.IMREAD_GRAYSCALE)
    else:
        print(f"using rotated image")
        imgAlign = imutils.rotate_bound(imgReference, rotateDegree)

    if (algorithm == 'orb'):
        orb = cv2.ORB_create()
        orb.setMaxFeatures(10000)
        referenceKp, referenceDes = orb.detectAndCompute(imgReference, None)
        alignKp, alignDes = orb.detectAndCompute(imgAlign, None)
    elif (algorithm == 'sift'):
        sift = cv2.xfeatures2d.SIFT_create()
        referenceKp, referenceDes = sift.detectAndCompute(imgReference, None)
        alignKp, alignDes = sift.detectAndCompute(imgAlign, None)


    matcher = cv2.BFMatcher()
    Matches = matcher.knnMatch(alignDes, referenceDes, k=2)

    good = []
    for m, n in Matches:
        if m.distance < 0.75*n.distance:
            good.append([m])

    print(f"Number of keypoints in align image: {len(alignKp)}")
    print(f"Number of keypoints in reference image: {len(referenceKp)}")
    print(f"Number of matches: {len(good)}")

    matching_rate = (len(good) / len(alignKp)) * 100
    print(f"Matching Rate: {matching_rate:.2f}%")

    if (debug == 1):
        a = find_rotation_angle(
            np.float32([alignKp[m[0].queryIdx].pt for m in good]).reshape(-1, 1, 2),
            np.float32([referenceKp[m[0].trainIdx].pt for m in good]).reshape(-1, 1, 2)
        )
        print(f"Rotation Angle: {a:.2f}")

    print("Done!")
