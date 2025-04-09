import cv2

image = cv2.imread("images/aayee_preety.jpg")

edges_detecter = cv2.Canny(image, 400, 100)


cv2.imshow("ayeeee", image)
cv2.imshow("detetct edges", edges_detecter)

cv2.waitKey(0)