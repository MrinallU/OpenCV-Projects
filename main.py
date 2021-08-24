import cv2

# cv2.imread('data/lena.jpg', 0)  # Loads in greyscale
img = cv2.imread('data/lena.jpg', 1)  # Loads in color
# cv2.imread('data/lena.jpg', -1) # Loads in alpha chanel

print(img)
cv2.imshow('image', img)
k = cv2.waitKey(0) # Keeps window open until closed

if k == 27: # if the esc key has bee pressed
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img) # saves the image
    cv2.destroyAllWindows()

# cv2.imwrite('lena_copy.png', img) # Getting the new image after the functions have been preformed


