import cv2 # the OpenCv library for computer vision 
import mediapipe as mp # the library for face detection 
import pyautogui # the library for controlling the mouse and keyboard

#set up capture and face mesh
cam = cv2.VideoCapture(0) # create a video capture object to access the webcam
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True) # create a face mesh object to detect facial landmarks
screen_w, screen_h = pyautogui.size() # get the screen width and height

# Main loop
while True: #loop indefinitely 
    _, frame = cam.read() # read a frame from the webcam
    frame = cv2.flip(frame, 1) # flip the frame horizontally
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # convert the frame from BGR to RGB color space
    output = face_mesh.process(rgb_frame) # process the frame with the face mesh object
    landmark_points = output.multi_face_landmarks # get the list of facial landmarks 
    frame_h, frame_w, _ = frame.shape # get the frame height, width and channels


    # Draw landmarks on eyes for better visual understanding 
    if landmark_points: # if there are any facial landmarks detected 
        landmarks = landmark_points[0].landmark # get the first face's landmarks
        for id, landmark in enumerate(landmarks[473:478]): # loop through the landmarks of the right eye
            x = int(landmark.x * frame_w) # get the x coordinate of the landmark 
            y = int(landmark.y * frame_h) # get the y coordinate of the landmark
            cv2.circle(frame, (x, y), 3, (0, 255, 0)) # draw a green circle on the frame at the landmark position



            # Move mouse cursor to right eye center 
            if id == 1: # if the landmark is the center of the right eye 
                screen_x = screen_w * landmark.x # map the landmark x coordinate to the screen x coordinate
                screen_y = screen_h * landmark.y # map the landmark y coordinate to the screen y coordinate 
                pyautogui.moveTo(screen_x, screen_y) # move the mouse cursor to the screen position

        

        # Draw left eye landmarks (yellow circle)
                left = [landmarks[145], landmarks[159]] # get the landmarks of the left eye corners
                for landmark in left: # loop through the left eye landmarks
                    x = int(landmark.x * frame_w) # get the x coordinate of the landmark
                    y = int(landmark.y * frame_h) # get the y coordinate of the landmark
                    cv2.circle(frame, (x, y), 3,(0, 255, 255)) # draw a yellow circle on the frame at the landmark position


        # check if left eye is almost closed and perform a click

                if (left[0].y - left[1].y) < 0.004: # if the left eye is almost closed
                   print("Left clicked performed")
                   pyautogui.click() # click the mouse 
                   pyautogui.sleep(1) # wait for one second



        # Draw right eye landmarks (yellow circle)
                right = [landmarks[145], landmarks[159]] # get the landmarks of the left eye corners
                for landmark in right: # loop through the left eye landmarks
                    x = int(landmark.x * frame_w) # get the x coordinate of the landmark
                    y = int (landmark.y * frame_h) # get the y coordinate of the landmark
                    cv2.circle(frame, (x, y), 3, (0, 255, 255)) # draw a yellow circle on the frame at the landmark position   


        # check if left eye is almost closed and perform a click
                if (right[0].y - right[1].y) < 0.004: # if the left eye is almost closed
                    print("Right clicked performed")
                    pyautogui.rightClick() # click the mouse
                    pyautogui.sleep(1) # wait for one second


        # Display the frame 
        # cv2.imshow('Eye Controlled Mouse', frame) # show the frame in a window named 'Eye Controlled Mouse'
        cv2.waitKey(1) # wait for the one millisecond or a key press