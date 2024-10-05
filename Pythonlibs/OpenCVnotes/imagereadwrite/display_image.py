import cv2
import matplotlib.pyplot as plt

cb_img = cv2.imread("Pythonlibs\OpenCVnotes\imagereadwrite\checkerboard_color.png")
coke_img = cv2.imread("Pythonlibs\OpenCVnotes\imagereadwrite\coca-cola-logo.png")

# Use matplotlib imshow()
plt.imshow(cv2.cvtColor(cb_img, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
plt.title("matplotlib imshow")
plt.show()

# Use OpenCV imshow(), display for 8 sec
cv2.namedWindow("w1")
cv2.imshow("w1", cb_img)
cv2.waitKey(8000)
cv2.destroyWindow("w1")

# Use OpenCV imshow(), display for 8 sec
cv2.namedWindow("w2")
cv2.imshow("w2", coke_img)
cv2.waitKey(8000)
cv2.destroyWindow("w2")

# Use OpenCV imshow(), display until any key is pressed
cv2.namedWindow("w3")
cv2.imshow("w3", cb_img)
cv2.waitKey(0)
cv2.destroyWindow("w3")

# OpenCV imshow(), display until 'q' key is pressed
cv2.namedWindow("w4")
Alive = True
while Alive:
    cv2.imshow("w4", coke_img)
    keypress = cv2.waitKey(1)
    if keypress == ord('q'):
        Alive = False
cv2.destroyWindow("w4")

cv2.destroyAllWindows()
