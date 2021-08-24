import cv2
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Prints the current resolution of a frame
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#a8c6d8c2d37505b5ca61ffd4bb54e9a7c
cap.set(3, 3000)  # Changes camera resolution
cap.set(4, 3000)  # To the max setting (1280 x 720)

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Converts to greyscale
       cv2.imshow('frame', gray)

       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()