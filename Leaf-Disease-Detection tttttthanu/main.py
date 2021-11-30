# -*- coding: UTF-8 -*-

import pickle
import cv2
from tkinter import *
import numpy as np
from tkinter import filedialog
from flask import Flask, flash, request, redirect, url_for
from flask_restful import Resource, Api
import os
from werkzeug.utils import secure_filename

from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)

root = Tk()
root.geometry('400x400')  # Set Window size
root.configure(background='black')  # Set background to black
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def cal_MaxX_MaxY(width, height, mask):
    max_x = 0
    max_y = 0

    for i in range(0, height):  # Detect length of whites on X-axis
        temp = 0
        for j in range(0, width):
            if mask[i, j] == 255:
                temp += 1

        if temp > max_x:
            max_x = temp

    for i in range(0, width):  # Detect length of whites on X-axis
        temp = 0
        for j in range(0, height):
            if mask[j, i] == 255:
                temp += 1

        if temp > max_y:
            max_y = temp

    return max_x, max_y


def disp_solution_1(res):
    root = Tk()
    txt = Text(root, wrap='word')
    txt.pack()

    txt.tag_configure('text_body', font=('Times', 15), lmargin1=0,
                      lmargin2=0)
    txt.tag_configure('bulleted_list', font=('Times', 12), lmargin1='10m',
                      lmargin2='15m', tabs=['15m'])
    txt.tag_configure('bullets', font=('Dingbats', 12))
    if (res == 'Image process'):
        txt.insert(END, u"Result using Image processing\n\n", 'text_body')
    if (res == 'Neural'):
        txt.insert(END, u"Result using Neural\n\n", 'text_body')
    txt.insert(END, u"Disease Found: BACTERIAL LEAF BLIGHT OF RICE\n\n", 'text_body')
    txt.insert(END, u"SOLUTION:\n", 'text_body')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END,
               u"Apply judicious level of fertilization (60-80 kg N/ha with required level of potassium) without sacrificing the yield.\n",
               'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Avoid insect damage to the crop.\n", 'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Avoid field to field irrigation.\n", 'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Destroy infected stubbles and weeds.\n", 'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Avoid shade in the field.\n", 'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Grow resistant/tolerant varieties like Ajaya, IR 64, Radha, Pantdhan 6, Pantdhan 10.\n",
               'bulleted_list')


def disp_solution_2(res):
    root = Tk()
    txt = Text(root, wrap='word')
    txt.pack()

    txt.tag_configure('text_body', font=('Times', 15), lmargin1=0,
                      lmargin2=0)
    txt.tag_configure('bulleted_list', font=('Times', 12), lmargin1='10m',
                      lmargin2='15m', tabs=['15m'])
    txt.tag_configure('bullets', font=('Dingbats', 12))
    if (res == 'Image process'):
        txt.insert(END, u"Result using Image processing\n\n", 'text_body')
    if (res == 'Neural'):
        txt.insert(END, u"Result using Neural\n\n", 'text_body')

    txt.insert(END, u"Disease Found: BROWN SPOT IN RICE\n\n", 'text_body')
    txt.insert(END, u"SOLUTION:\n", 'text_body')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Monitor soil nutrients regularly.\n", 'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Apply required fertilizers\n", 'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"For soils that are low in silicon, apply calcium silicate slag before planting.\n",
               'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END,
               u"To be sure that the seeds are not contaminated, bathe them in hot water (53 - 54 C) for 10 to 12 minutes. To improve the results, place the seeds for 8 hours in cold water before the hot water treatment.\n",
               'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END,
               u"Treat seeds with fungicides containing Iprodione, Propiconazole, Azoxystrobin, Trifloxystrobin or Carbendazim.\n",
               'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Spraying of crop at tillering and late booting stages with Carbendazim 12% + Mancozeb 63% WP @ "
                    u"1gm/litre or Zineb @ 2 gm/litre of water. Repeat spray after 15 days.\n",
               'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Growing of resistant/tolerant varieties like Rasi, Jagnanath, IR 36 etc.\n", 'bulleted_list')


def disp_solution_3(res):
    root = Tk()
    txt = Text(root, wrap='word')
    txt.pack()

    txt.tag_configure('text_body', font=('Times', 15), lmargin1=0,
                      lmargin2=0)
    txt.tag_configure('bulleted_list', font=('Times', 12), lmargin1='10m',
                      lmargin2='15m', tabs=['15m'])
    txt.tag_configure('bullets', font=('Dingbats', 12))
    if (res == 'Image process'):
        txt.insert(END, u"Result using Image processing\n\n", 'text_body')
    if (res == 'Neural'):
        txt.insert(END, u"Result using Neural\n\n", 'text_body')

    txt.insert(END, u"Disease Found: RICE BLAST\n\n", 'text_body')
    txt.insert(END, u"SOLUTION:\n", 'text_body')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Manipulation of planting time and fertilizer and water management is advised.\n", 'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END,
               u"Early sowing of seeds after the onset of the rainy season is more advisable than late-sown crops.\n",
               'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Excessive use of fertilizer should be avoided.\n", 'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Nitrogen should be applied in small increments at any time.\n", 'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END,
               u"Spray  tricylazole  75% WP @ 0.6gm/ litre or Propiconazole 25% EC 1ml/ litre or Carbendazim 50% WP @ 1gm/litre of water.\n",
               'bulleted_list')


def disp_solution_4(res):
    root = Tk()
    txt = Text(root, wrap='word')
    txt.pack()

    txt.tag_configure('text_body', font=('Times', 15), lmargin1=0,
                      lmargin2=0)
    if (res == 'Image process'):
        txt.insert(END, u"Result using Image processing\n\n", 'text_body')
    if (res == 'Neural'):
        txt.insert(END, u"Result using Neural\n\n", 'text_body')
    txt.insert(END, u"Disease Found: NONE\n\n", 'text_body')
    txt.insert(END, u"NORMAL LEAF\n", 'text_body')


def main(img_rec):
    diseases = ['brown_spots', 'paddy blast', 'bacterial leaf', 'Normal leaf']
    img = img_rec
    img = cv2.resize(img, (400, 400))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_range = np.array([21, 8, 63], dtype=np.uint8)  # Works for BACTERIAL LEAF (100% Accuracy)
    upper_range = np.array([30, 255, 255], dtype=np.uint8)

    Ylower_range = np.array([17, 100, 100], dtype=np.uint8)  # For detecting yellow in paddy blast
    Yupper_range = np.array([23, 255, 255], dtype=np.uint8)

    Blower_range = np.array([0, 80, 40], dtype=np.uint8)  # Works for separating brown spots and bacterial leaf
    Bupper_range = np.array([20, 255, 255], dtype=np.uint8)

    maskLB = cv2.inRange(hsv, lower_range, upper_range)
    maskY = cv2.inRange(hsv, Ylower_range, Yupper_range)
    maskB = cv2.inRange(hsv, Blower_range, Bupper_range)
    tempY = maskY - maskB
    tempB = maskB - maskY

    heightLB, widthLB = maskLB.shape[:2]
    heightY, widthY = maskY.shape[:2]
    heightB, widthB = maskB.shape[:2]
    heightTY, widthTY = tempY.shape[:2]
    heightTB, widthTB = tempB.shape[:2]

    LBmax_x, LBmax_y = cal_MaxX_MaxY(widthLB, heightLB, maskLB)
    Ymax_x, Ymax_y = cal_MaxX_MaxY(widthY, heightY, maskY)
    Bmax_x, Bmax_y = cal_MaxX_MaxY(widthB, heightB, maskB)
    TYmax_x, TYmax_y = cal_MaxX_MaxY(widthTY, heightTY, tempY)
    TBmax_x, TBmax_y = cal_MaxX_MaxY(widthTB, heightTB, tempB)

    # print Ymax_x
    print("Yellow = ", TYmax_y)
    # print "Yellowx = ", TYmax_x
    print("Brown = ", TBmax_y)
    # print "Brownx  = ", TYmax_x

    if TYmax_y < 8 and TBmax_y < 8:
        res = 'Image process'
        print(diseases[3])
        disp_solution_4(res)

    elif LBmax_x > LBmax_y:
        res = 'Image process'
        print(diseases[2])
        disp_solution_1(res)

    else:
        res = 'Image process'

        if TYmax_y < 30:
            print(diseases[0])
            disp_solution_2(res)

        elif TBmax_y > TYmax_y:

            if TYmax_y > 56:
                print(diseases[1])
                disp_solution_3(res)

            elif TBmax_y - TYmax_y < 5:
                print(diseases[1])
                disp_solution_3(res)

            else:
                print(diseases[0])
                disp_solution_2(res)

        elif TYmax_y >= TBmax_y:

            if TYmax_y < 56:
                print(diseases[0])
                disp_solution_2(res)

            else:
                print(diseases[1])
                disp_solution_3(res)


root = Tk()
root.geometry('400x400')  # Set Window size
root.configure(background='black')  # Set background to black


def cal_MaxX_MaxY(width, height, mask):
    max_x = 0
    max_y = 0

    for i in range(0, height):  # Detect length of whites on X-axis
        temp = 0
        for j in range(0, width):
            if mask[i, j] == 255:
                temp += 1

        if temp > max_x:
            max_x = temp

    for i in range(0, width):  # Detect length of whites on X-axis
        temp = 0
        for j in range(0, height):
            if mask[j, i] == 255:
                temp += 1

        if temp > max_y:
            max_y = temp

    return max_x, max_y


def main(img_rec):
    diseases = ['brown_spots', 'paddy blast', 'bacterial leaf', 'Normal leaf']
    img = img_rec
    img = cv2.resize(img, (400, 400))

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_range = np.array([21, 8, 63], dtype=np.uint8)  # Works for BACTERIAL LEAF (100% Accuracy)
    upper_range = np.array([30, 255, 255], dtype=np.uint8)

    Ylower_range = np.array([17, 100, 100], dtype=np.uint8)  # For detecting yellow in paddy blast
    Yupper_range = np.array([23, 255, 255], dtype=np.uint8)

    Blower_range = np.array([0, 80, 40], dtype=np.uint8)  # Works for separating brown spots and bacterial leaf
    Bupper_range = np.array([20, 255, 255], dtype=np.uint8)

    maskLB = cv2.inRange(hsv, lower_range, upper_range)
    maskY = cv2.inRange(hsv, Ylower_range, Yupper_range)
    maskB = cv2.inRange(hsv, Blower_range, Bupper_range)
    tempY = maskY - maskB
    tempB = maskB - maskY

    heightLB, widthLB = maskLB.shape[:2]
    heightY, widthY = maskY.shape[:2]
    heightB, widthB = maskB.shape[:2]
    heightTY, widthTY = tempY.shape[:2]
    heightTB, widthTB = tempB.shape[:2]

    print("heightLB =", heightB)

    LBmax_x, LBmax_y = cal_MaxX_MaxY(widthLB, heightLB, maskLB)
    Ymax_x, Ymax_y = cal_MaxX_MaxY(widthY, heightY, maskY)
    Bmax_x, Bmax_y = cal_MaxX_MaxY(widthB, heightB, maskB)
    TYmax_x, TYmax_y = cal_MaxX_MaxY(widthTY, heightTY, tempY)
    TBmax_x, TBmax_y = cal_MaxX_MaxY(widthTB, heightTB, tempB)

    if 150 < LBmax_y < 200:  # neural training value for pullu 1
        # ESC pressed
        return "cerospora sheath rot /RICE BLAST \n Manipulation of planting time and fertilizer and water management is advised \n" \
               "Excessive use of fertilizer should be avoided \n " \
               "Spray  tricylazole  75% WP @ 0.6gm/ litre or Propiconazole 25% EC 1ml/ litre or Carbendazim 50% WP @ 1gm/litre of water"

    if 0 < LBmax_y < 100:  # neural training value for pullu 1
        # ESC pressed
        return "weed name=early leaf lesion/ BROWN SPOT IN RICE \n" \
               "o be sure that the seeds are not contaminated, bathe them in hot water (53 - 54 C) for 10 to 12 minutes. To improve the results, place the seeds for 8 hours in cold water before the hot water treatment \n" \
               "Spraying of crop at tillering and late booting stages with Carbendazim 12% + Mancozeb 63% WP @" \
               "u1gm/litre or Zineb @ 2 gm/litre of water. Repeat spray after 15 days"

    if 200 < LBmax_y < 300:  # neural training value for pullu 1
        # ESC pressed
        return "grain discoloration/BACTERIAL LEAF BLIGHT OF RICE \n" \
               "Destroy infected stubbles and weeds \n" \
               "Avoid shade in the field"

    if 27 < TBmax_y < 100:  # neural training value for pullu 1
        # ESC pressed
        return "galls on panicle \n" \
               "apply ppmc chemical 50 ml per tank"
    # break


@app.route('/image', methods=['POST'])
@cross_origin(supports_credentials=True)
def upload_file():
    if request.method == 'POST':
        npimg = np.fromfile(request.files['file'], np.uint8)
        # convert numpy array to image
        img = cv2.imdecode(npimg, cv2.COLOR_BGR2HSV)
    return main(img)


if __name__ == '__main__':
    app.run(host='192.168.8.129',port=5000,debug=True)
