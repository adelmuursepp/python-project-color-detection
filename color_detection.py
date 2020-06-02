import cv2
import pandas as pd

img = cv2.imread("havana_cuba.jpg")
# cv2.imshow("image", img)
headers = ['color_code', 'color_name', 'hexcode', 'r', 'g', 'b']

dataframe = pd.read_csv("colors.csv", names = headers, header = None)

print(dataframe.loc[12, 'color_name'])




r= 0
g= 0
b= 0

def get_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global r,g,b
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
        print (get_color_name())

def get_color_name():
    minimum = 768
    for i in range(len(dataframe)):
        distance = abs((r-dataframe.loc[i, 'r']) + (g-dataframe.loc[i, 'g']) + (b-dataframe.loc[i, 'b']))
        if distance < minimum:
            minimum = distance
            color_name = dataframe.loc[i, 'color_name']
    return color_name

cv2.namedWindow("image")
cv2.setMouseCallback("image",get_color)

while True:
    cv2.imshow("image", img)
    print(get_color_name())
    if cv2.waitKey(0)==27:
        break



cv2.destroyAllWindows()

