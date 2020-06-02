import cv2

img = cv2.imread("colorpic.jpg")
# cv2.imshow("image", img)

r= 0
g= 0
b= 0

def get_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global r,g,b
        b,g,r = img[y,x]
        print (b)

cv2.namedWindow("image")
cv2.setMouseCallback("image",get_color)

while True:
    cv2.imshow("image", img)
    if cv2.waitKey(0)==27:
        break



cv2.destroyAllWindows()

