# import all library needed
import cv2 as ocv
import face_recognition as fr

#creating class 
class RealTime_FaceDetection():
    def __init__(self,device_index = 0):
        self.cap = ocv.VideoCapture(device_index) # Allocating camera device
        
    # This function is to seperate all the locations of face into it's coordinates  
    def unzip(self,face_loc):
        f_loc = [0,0,0,0]
        for pos, individual in enumerate(face_loc):
            f_loc[pos] = individual
        return f_loc
    
    # This is the main function in which whole process of face detection mainly lies.
    def detect(self):
        while(self.cap.isOpened()):
            flag, frame = self.cap.read()
            if flag:
                face_loc = fr.face_locations(frame)
                for i in range(len(face_loc)):
                    top, right, bottom, left = self.unzip(face_loc[i])
                    ocv.rectangle(frame,(left,top),(right,bottom),(0,255,255),2)
                ocv.imshow('window',frame)
                if ocv.waitKey(1) & 0xFF == 27:
                    ocv.destroyAllWindows()
                    self.cap.release()
                    break

# It runs only if you run this file seperately rather than importing to any other script        
if __name__ == "__main__":
    print("Press ESC to exit")
    obj_detect = RealTime_FaceDetection(0)
    obj_detect.detect()