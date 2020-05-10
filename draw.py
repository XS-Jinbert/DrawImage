# -*- coding = utf-8 -*-

import numpy as ny
import cv2
import turtle

def main():
    draw(array_image(r"Image\001.jpg"))

def array_image(imgPath):
    image = cv2.imread(imgPath, 0)
    # cv2.imshow("Image", image)
    edges = cv2.Canny(image, 150, 200)
    img_gray = cv2.cvtColor(edges, cv2.COLOR_BAYER_BG2GRAY)
    ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    xy = []
    for i in range(0, len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
        list_xy = [x, y]
        xy.append(list_xy)
    return xy

def draw(xy):
    turtle.pensize(2)
    turtle.setup(width=0.6, height=1.0)
    turtle.speed(100)
    for array in xy[::-1]:
        turtle.penup()
        turtle.goto((-array[0]/3)+100, (-array[1]/3)+250)
        turtle.pendown()
        turtle.forward(1)
        print(turtle.pos())
    turtle.done()

if __name__ == "__main__":
    main()