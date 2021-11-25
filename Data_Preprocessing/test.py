import cv2 as cv


def resize(img_path, width, hiegh):
    img = cv.imread(img_path)
    dim = (width, hiegh)
    resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)


def rotation(img_path, direction):
    if direction == True:
        img = cv.rotate(img_path, cv.ROTATE_90_CLOCKWISE)
    if direction == False:
        img = cv.rotate(img_path, cv.ROTATE_90_COUNTERCLOCKWISE)
