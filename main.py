from imutils.object_detection import non_max_suppression
import numpy as np
import imutils
import cv2
import argparse

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detector(image):

    image = imutils.resize(image, width=640, height=400)

    (rects, weights) = HOGCV.detectMultiScale(image, winStride=(5, 5), padding=(16, 16), scale=1.04)

    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    result = non_max_suppression(rects, probs=None, overlapThresh=0.7)

    return result


def local_detect(image_path):
    result = []
    image = cv2.imread(image_path)
    if len(image) <= 0:
        print("File not found")
        return result
    print("Detecting people...")
    result = detector(image)

    for (xA, yA, xB, yB) in result:
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

    cv2.imshow("result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return result, image


def detect_people(args):
    image_path = args["image"]

    # Routine to read local image
    if image_path is not None:
        local_detect(image_path)


def args_parser():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", default=None, help="path to image file")
    args = vars(ap.parse_args())

    return args


def main():
    args = args_parser()
    detect_people(args)


if __name__ == '__main__':
    main()
