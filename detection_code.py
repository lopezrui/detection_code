#The needed libraries are imported
from imageai.Detection import VideoObjectDetection
import cv2
from IPython.display import clear_output

#Start the video capture of the camera
camera = cv2.VideoCapture('http://lopezrui.ddns.net/video/mjpg.cgi')

#Initialise the detector, very similar to the still image detector
detector = VideoObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath('/content/drive/My Drive/yolo-tiny.h5')

#The argument within loadModel increases the speed of detection, 
#but sacrifices a little accuracy
detector.loadModel(detection_speed="flash")
custom_objects = detector.CustomObjects(person=True)
      
#Create the function that is run every second the camera is recording.
def forSeconds(second_number, output_arrays, count_arrays, average_output_count):
    number = ""
    people_in_frame = str(average_output_count)

    #If the system doesn't detect any people in the frame, it will print 0.
    if people_in_frame == "{}":
        number = "0"
    else:  
        #The number of people in the frame is prepared.
        #This for loop analyses every character in the output and gathers
        #any digits and joins them in "number" to get a final number of people.
        for i in range(0, len(people_in_frame)):
            if people_in_frame[i].isdigit() == True:
                number = number + people_in_frame[i]
    clear_output()
    print(number)
    
video_path = detector.detectCustomObjectsFromVideo(
                custom_objects=custom_objects,
                camera_input=camera,
                save_detected_video=False,
                frames_per_second=5,
                per_second_function=forSeconds,
                minimum_percentage_probability=20)
