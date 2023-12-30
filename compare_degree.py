import cv2
import sys
import imutils

if __name__ == '__main__':
    # inputs: algorithm, reference image path, rotate degree
    algorithm = sys.argv[1]
    referencePath = sys.argv[2]
    rotateDegree = int(sys.argv[3])

    print(f"\n\nAlgorithm: {algorithm}\nDegree: {rotateDegree}")

    imgReference = cv2.imread(referencePath, cv2.IMREAD_GRAYSCALE)

    if (rotateDegree == 1):
        print(f"using scaled image")
        imgAlign = cv2.resize(imgReference, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    elif (rotateDegree == 2):
        print(f"adding noised image")
        imgAlign = cv2.imread('./images/salt-and-pepper-george.jpg', cv2.IMREAD_GRAYSCALE)
    else:
        print(f"using rotated image")
        imgAlign = imutils.rotate_bound(imgReference, rotateDegree)

    if (algorithm == 'orb'):
        orb = cv2.ORB_create()
        referenceKp, referenceDes = orb.detectAndCompute(imgReference, None)
        alignKp, alignDes = orb.detectAndCompute(imgAlign, None)

    elif(algorithm == 'sift'):
        sift = cv2.xfeatures2d.SIFT_create()
        referenceKp, referenceDes = sift.detectAndCompute(imgReference, None)
        alignKp, alignDes = sift.detectAndCompute(imgAlign, None)

    matcher = cv2.BFMatcher()
    Matches = matcher.knnMatch(alignDes, referenceDes, k=2)

    good = []
    for m,n in Matches:
        if m.distance < 0.75*n.distance:
            good.append([m])

    print(f"Number of keypoints in align image: {len(alignKp)}")
    print(f"Number of keypoints in reference image: {len(referenceKp)}")
    print(f"Number of matches: {len(good)}")
    print("Done!")
