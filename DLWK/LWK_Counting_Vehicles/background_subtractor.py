#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import pandas as pd
import sys
import os


def transformation(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=3)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel, iterations=1)
    dilation = cv2.dilate(opening, kernel, iterations=2)
    # remove shadows
    retvalbin, bins = cv2.threshold(dilation, 220, 255, cv2.THRESH_BINARY)

    return bins


def contours_with_centroids(transformation_image, resize_image, \
    resize_height, resize_width, lineypos, lineypos2):
    # create contours
    #contours, hierarchy = cv2.findContours(transformation_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(transformation_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)

    # convex hull: create polygon around contours
    hull = [cv2.convexHull(c) for c in contours]

    #cv2.drawContours(resize_image, hull, -1, (0, 255, 0), 3)

    cv2.line(resize_image, (0, lineypos), (resize_width, lineypos), (255, 0, 0), 5)
    cv2.line(resize_image, (0, lineypos2), (resize_width, lineypos2), (0, 255, 0), 5)

    # min area for contours
    minarea = 1000
    # max area for contours
    maxarea = 50000
    # vectors for the x and y locations of contour centroids in current frame
    cxx = np.zeros(len(contours))
    cyy = np.zeros(len(contours))

    # go through all contours in current frame
    for i in range(len(contours)):
        # using hierarchy to only count parent contours
        if hierarchy[0, i, 3] == -1:
            area = cv2.contourArea(contours[i])

            if minarea < area < maxarea:
                # calculating centroids of contours
                cnt = contours[i]
                M = cv2.moments(cnt)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

                # filters out contours that are above line
                if cy > lineypos:
                    x, y, w, h = cv2.boundingRect(cnt)
                    # creates a rectangle around contour
                    cv2.rectangle(resize_image, (x, y), (x + w, y + h), (0, 0, 255), 3)

                    # adds centroids to centroid list
                    cxx[i] = cx
                    cyy[i] = cy

    cxx = cxx[cxx != 0]
    cyy = cyy[cyy != 0]

    return cxx, cyy


def track_vehicles(cxx, cyy, df, frame_number, vehicles_id, total_vehicles):
    # empty list to check which centroid indices were added to dataframe
    minx_index2 = []
    miny_index2 = []

    # maximum allowable radius for current frame centroid to be considered the same centroid from previous frame
    maxrad = 25

    if len(cxx):
        if not vehicles_id:
            for i in range(len(cxx)):
                vehicles_id.append(i)
                df[str(vehicles_id[i])] = ""

                df.at[int(frame_number), str(vehicles_id[i])] = [cxx[i], cyy[i]]
                total_vehicles = vehicles_id[i] + 1

        else:
            dx = np.zeros((len(cxx), len(vehicles_id)))
            dy = np.zeros((len(cyy), len(vehicles_id)))

            for i in range(len(cxx)):
                for j in range(len(vehicles_id)):
                    oldcxcy = df.iloc[int(frame_number - 1)][str(vehicles_id[j])]
                    curcxcy = np.array([cxx[i], cyy[i]])

                    if not oldcxcy:
                        continue
                    else:
                        dx[i, j] = oldcxcy[0] - curcxcy[0]
                        dy[i, j] = oldcxcy[1] - curcxcy[1]

            for j in range(len(vehicles_id)):
                sumsum = np.abs(dx[:, j]) + np.abs(dy[:, j])
                correctindextrue = np.argmin(np.abs(sumsum))
                minx_index = correctindextrue
                miny_index = correctindextrue

                mindx = dx[minx_index, j]
                mindy = dy[miny_index, j]

                if mindx == 0 and mindy == 0 and np.all(dx[:, j] == 0) and np.all(dy[:, j] == 0):
                    continue
                else:
                    if np.abs(mindx) < maxrad and np.abs(mindy) < maxrad:
                        df.at[int(frame_number), str(vehicles_id[j])] = [cxx[minx_index], cyy[miny_index]]
                        minx_index2.append(minx_index)
                        miny_index2.append(miny_index)

            for i in range(len(cxx)):
                if i not in minx_index2 and miny_index2:
                    df[str(total_vehicles)] = ""
                    total_vehicles = total_vehicles + 1
                    t = total_vehicles - 1
                    vehicles_id.append(t)
                    df.at[int(frame_number), str(t)] = [cxx[i], cyy[i]]

                elif curcxcy[0] and not oldcxcy and not minx_index2 and not miny_index2:
                    df[str(total_vehicles)] = ""
                    total_vehicles = total_vehicles + 1
                    t = total_vehicles - 1
                    vehicles_id.append(t)
                    df.at[int(frame_number), str(t)] = [cxx[i], cyy[i]]

    return df, vehicles_id, total_vehicles


def count_vehicles(resize_image, resize_width, df, frame_number, vehicles_id, \
    vehicles_id_crossed, vehicles_crossed_up, vehicles_crossed_down, \
    lineypos, lineypos2):
    current_vehicles = 0
    current_vehicles_index = []

    for i in range(len(vehicles_id)):
        if df.at[int(frame_number), str(vehicles_id[i])] != '':
            current_vehicles = current_vehicles + 1
            current_vehicles_index.append(i)

    for i in range(current_vehicles):
        current_cent = df.iloc[int(frame_number)][str(vehicles_id[current_vehicles_index[i]])]
        old_cent = df.iloc[int(frame_number - 1)][str(vehicles_id[current_vehicles_index[i]])]

        if current_cent:
            #cv2.putText(resize_image, "Centroid: " + str(current_cent[0]) + "," + str(current_cent[1]), \
            #    (int(current_cent[0]), int(current_cent[1])), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 255, 255), 2)
            #cv2.putText(resize_image, "ID: " + str(vehicles_id[current_vehicles_index[i]]), \
            #    (int(current_cent[0]), int(current_cent[1] - 15)), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 255, 255), 2)

            if old_cent:
                if old_cent[1] >= lineypos2 and current_cent[1] <= lineypos2 \
                    and vehicles_id[current_vehicles_index[i]] not in vehicles_id_crossed:

                    vehicles_crossed_up = vehicles_crossed_up + 1
                    cv2.line(resize_image, (0, lineypos2), (resize_width, lineypos2), (0, 0, 255), 5)
                    vehicles_id_crossed.append(current_vehicles_index[i])

                elif old_cent[1] <= lineypos2 and current_cent[1] >= lineypos2 \
                    and vehicles_id[current_vehicles_index[i]] not in vehicles_id_crossed:

                    vehicles_crossed_down = vehicles_crossed_down + 1
                    cv2.line(resize_image, (0, lineypos2), (resize_width, lineypos2), (0, 0, 125), 5)
                    vehicles_id_crossed.append(current_vehicles_index[i])

    return vehicles_id_crossed, vehicles_crossed_up, vehicles_crossed_down

def mouse_drawing(event, x, y, flags, params):
    global y1, y2
    if event == cv2.EVENT_LBUTTONDOWN:
        y1=y
    if event == cv2.EVENT_RBUTTONDOWN:
        y2=y

def main(video_source):
    # open video and get information

    cap = cv2.VideoCapture(video_source)

    frames_count, fps, width, height = cap.get(cv2.CAP_PROP_FRAME_COUNT), \
        cap.get(cv2.CAP_PROP_FPS), \
        cap.get(cv2.CAP_PROP_FRAME_WIDTH), \
        cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    width = int(width)
    height = int(height)
    print(frames_count, fps, width, height)
    print ('\n')

    # pandas data frame: number of rows = frame_count
    df = pd.DataFrame(index=range(int(frames_count)))
    df.index.name = "Frames"
    
    # print(df)

    # variables - counting vehicles
    frame_number = 0  # keeps track of current frame
    vehicles_crossed_up = 0  # keeps track of vehicles that crossed up
    vehicles_crossed_down = 0  # keeps track of vehicles that crossed down
    vehicles_id = []  # blank list to add vehicles id
    vehicles_id_crossed = []  # blank list to add vehicles id that have crossed
    total_vehicles = 0  # keeps track of total vehicles

    # create background subtractor
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()
    #bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, detectShadows=True)

    # resize ratio
    ratio = .5
    pom = 0
    while True:
        print (y1, y2)
        (ret, frame) = cap.read()
        if pom%2 == 0:
            k = cv2.waitKey()
        if pom%2 == 1:
            k = cv2.waitKey(int(1000 / fps)) & 0xEFFFFF
        if k == ord('p'):
            pom = pom + 1

        # if there is a frame continue with code
        if ret:
            # resize image
            if width >= 1280:
                resize_image = cv2.resize(frame, (0, 0), None, ratio, ratio)
            else:
                resize_image = frame
            
            if y1 == 0 and y2 == 0:
                resize_height, resize_width, resize_channels = resize_image.shape
                # line created to stop counting contours
                #lineypos = 225
                lineypos = int(resize_height - (0.30 * resize_height))
                # line y position created to count contours
                #lineypos2 = 250
                lineypos2 = int(resize_height - (0.25 * resize_height))

                gray_image = cv2.cvtColor(resize_image, cv2.COLOR_RGB2GRAY)

                fg_mask = bg_subtractor.apply(gray_image)

                # transformations
                transformation_image = transformation(fg_mask)

                cxx, cyy = contours_with_centroids(transformation_image, resize_image, \
                    resize_height, resize_width, lineypos, lineypos2)

                df, vehicles_id, total_vehicles = track_vehicles(cxx, cyy, df, frame_number, vehicles_id, total_vehicles)

                vehicles_id_crossed, vehicles_crossed_up, vehicles_crossed_down = \
                    count_vehicles(resize_image, resize_width, df, frame_number, vehicles_id, \
                        vehicles_id_crossed, vehicles_crossed_up, vehicles_crossed_down, \
                        lineypos, lineypos2)

                # information table
                cv2.rectangle(resize_image, (0, 0), (350, 75), (255, 255, 255), -1)
                cv2.putText(resize_image, "Vehicles crossed up: " + str(vehicles_crossed_up), \
                    (0, 25), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
                cv2.putText(resize_image, "Vehicles crossed down: " + str(vehicles_crossed_down), \
                    (0, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)

            else:
                resize_height, resize_width, resize_channels = resize_image.shape
                # line created to stop counting contours
                #lineypos = 225
                #lineypos = int(resize_height - (0.30 * resize_height))
                # line y position created to count contours
                #lineypos2 = 250
                #lineypos2 = int(resize_height - (0.25 * resize_height))
                lineypos = y1
                lineypos2 = y2
                gray_image = cv2.cvtColor(resize_image, cv2.COLOR_RGB2GRAY)

                fg_mask = bg_subtractor.apply(gray_image)

                # transformations
                transformation_image = transformation(fg_mask)

                cxx, cyy = contours_with_centroids(transformation_image, resize_image, \
                    resize_height, resize_width, lineypos, lineypos2)

                df, vehicles_id, total_vehicles = track_vehicles(cxx, cyy, df, frame_number, vehicles_id, total_vehicles)

                vehicles_id_crossed, vehicles_crossed_up, vehicles_crossed_down = \
                    count_vehicles(resize_image, resize_width, df, frame_number, vehicles_id, \
                        vehicles_id_crossed, vehicles_crossed_up, vehicles_crossed_down, \
                        lineypos, lineypos2)

                # information table
                cv2.rectangle(resize_image, (0, 0), (350, 75), (255, 255, 255), -1)
                cv2.putText(resize_image, "Vehicles crossed up: " + str(vehicles_crossed_up), \
                    (0, 25), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
                cv2.putText(resize_image, "Vehicles crossed down: " + str(vehicles_crossed_down), \
                    (0, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)

            cv2.imshow('original', resize_image)
            cv2.moveWindow('original', 0, 0)
            cv2.setMouseCallback('original', mouse_drawing)
            cv2.imshow('transformation', transformation_image)

            frame_number = frame_number + 1

        else:
            break

        #k = cv2.waitKey(int(1000 / fps)) & 0xff
        #k = cv2.waitKey(18)
        #k = cv2.waitKey(0)
        if k == 27:
            break
        #if k == ord('p'):
        #    k = cv2.waitKey(int(1000 / fps)) & 0xEFFFFF

    cap.release()
    cv2.destroyAllWindows()
    pom = 0


if __name__ == "__main__":
    y1 = 0
    y2 = 0
    print ('\n')
    #CHECK OPENCV INFORMATIONS
    #print(cv2.getBuildInformation())
    if len(sys.argv) == 2:
        exists = os.path.isfile(str(sys.argv[1]))
        if exists:
            video_source = sys.argv[1]
            main(video_source)
        else:
            print ('Podany plik nie istnieje!')
            print ('\n')
    else:
        print('Nie podano pliku video!')
        print ('\n')
