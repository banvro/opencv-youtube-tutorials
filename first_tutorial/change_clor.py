import cv2

img = cv2.imread("images/kris12.27.22ig1.jpg")
resized_img = cv2.resize(img, (600, 700))

gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)

hls_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HLS)

cv2.imshow("resied igm", resized_img)
cv2.imshow("gray image", gray_img)
cv2.imshow("HSV img", hsv_img)
cv2.imshow("HLS img", hls_img)
 
cv2.waitKey(0)