import cv2

class CMarker():
    def markFaces(frame, faces ):
        for (x,y,w,h) in faces:
            frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


    def markPoints(frame, points, color):
        for p in points:
            pt = (p[0],p[1])
            cv2.circle(frame, pt, 3, color, 2)

    #def markVecOff(frame, hflow, vflow):
       #PUT YOUR CODE HERE

    def markGUI(frame):
        #PUT YOUR CODE HERE
        #Implement yout ouw GUI
        #Show fps
        for y in frame.shape[0]:
            ptr = frame.row[y]
            for x in frame.shape[1]:
                k =  x / frame.cols
                ptr[x] = cv2.Vec3b(k * 255, 0, 255 - k * 255)
        cv2.circle(frame, (frame.cols / 2, frame.rows /2), 50, (100, 255, 100), 5)
        cv2.GaussianBlur(frame, frame, (17, 17), 50)
        cv2.putText(frame, "HCI", (100,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)


