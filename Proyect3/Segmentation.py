import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

def draw_segmented_objects(image, countour, label_cnt_idx, bubbles_count, contours):
    mask = np.zeros_like(image[:, :, 0])
    cv2.drawContours(mask, [contours[i] for i in label_cnt_idx], -1, (255), -1)
    masked_image = cv2.bitwise_and(image, image, mask=mask)
    masked_image = cv2.putText(masked_image, f'{bubbles_count} bubbles', (200, 1200), cv2.FONT_HERSHEY_SIMPLEX, 
                               fontScale = 3, color = (255, 255, 255), thickness = 10, lineType = cv2.LINE_AA)
    return masked_image

def Segmentation(im) :
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    _, msk = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)
    msk = cv2.erode(msk, np.ones((3,3), np.uint8))

    contours, _ = cv2.findContours(msk, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_img_before_filtering = msk.copy()
    contours_img_before_filtering = cv2.cvtColor(contours_img_before_filtering, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(contours_img_before_filtering, contours, -1, (0, 255, 0), 1)

    #The flag CHAIN_APPROX_SIMPLE only return extern contours.

    filtered_contours = []
    df_mean_color = pd.DataFrame()

    cnt = 0
    for idx, contour in enumerate(contours) :
        area = int(cv2.contourArea(contour))
        if area < 3000 and area > 20 :
            filtered_contours.append(contour)
            masked = np.zeros_like(im[:,:,0])
            cv2.drawContours(masked, [contour], 0, 255, -1)
            B_mean, G_mean, R_mean, _ = cv2.mean(im, mask=masked)
            df = pd.DataFrame({'B_mean': B_mean, 'G_mean': G_mean, 'R_mean': R_mean}, index=[idx])
            df_mean_color = pd.concat([df_mean_color, df])

    #Displat filtered contours
    contours_img_after_filtering = msk.copy()
    contours_img_after_filtering = cv2.cvtColor(contours_img_after_filtering, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(contours_img_after_filtering, tuple(filtered_contours), -1, (0, 255, 0), 1)


    km = KMeans( n_clusters = 4)
    df_mean_color['label'] = km.fit_predict(df_mean_color)


    img = im.copy()

    for label, df_grouped in df_mean_color.groupby('label') :
        bubbles_amount = len(df_grouped)
        masked_image = draw_segmented_objects(im, contour, df_grouped.index, bubbles_amount, contours)
        cv2.imshow("Img Segmentada", masked_image)
        return masked_image
