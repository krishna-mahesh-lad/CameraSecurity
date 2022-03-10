import cv2

def snapshot():
    #initialize cv2
    captureObj = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frame while the cam is on
        ret, frame = captureObj.read()
        cv2.imwrite('NewPic1.jpg', frame)
        result = False
    captureObj.release()
    cv2.destroyAllWindows()
snapshot()