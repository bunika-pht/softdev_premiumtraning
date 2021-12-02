import cv2 as cv
import numpy as np


def resize(img_path, width, high):
    img = cv.imread(img_path)
    dim = (width, high)
    resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)


def rotation(img_path, direction):
    if direction == True:
        img = cv.rotate(img_path, cv.ROTATE_90_CLOCKWISE)
    if direction == False:
        img = cv.rotate(img_path, cv.ROTATE_90_COUNTERCLOCKWISE)


img = cv.imread('mandrill.png')  # mandrill reference image from USC SIPI
s = 128
img = cv.resize(img, (s, s), 0, 0, cv.INTER_AREA)


def apply_brightness_contrast(input_img, brightness=0, contrast=0):

    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow)/255
        gamma_b = shadow

        buf = cv.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()

    if contrast != 0:
        f = 131*(contrast + 127)/(127*(131-contrast))
        alpha_c = f
        gamma_c = 127*(1-f)

        buf = cv.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    return buf


font = cv.FONT_HERSHEY_SIMPLEX
fcolor = (0, 0, 0)

blist = [0, -127, 127,   0,  0, 64]  # list of brightness values
clist = [0,    0,   0, -64, 64, 64]  # list of contrast values


out = np.zeros((s*2, s*3, 3), dtype=np.uint8)

for i, b in enumerate(blist):
    c = clist[i]
    print('b, c:  ', b, ', ', c)
    row = s*int(i/3)
    col = s*(i % 3)
    print('row, col:   ', row, ', ', col)
    out[row:row+s, col:col+s] = apply_brightness_contrast(img, b, c)
    msg = 'b %d' % b
    cv.putText(out, msg, (col, row+s-22), font, .7, fcolor, 1, cv.LINE_AA)
    msg = 'c %d' % c
    cv.putText(out, msg, (col, row+s-4), font, .7, fcolor, 1, cv.LINE_AA)
    cv.putText(out, 'OpenCV', (260, 30), font, 1.0, fcolor, 2, cv.LINE_AA)

cv.imwrite('out.png', out)
