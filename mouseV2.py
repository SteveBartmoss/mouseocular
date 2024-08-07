import cv2
import mediapipe as mp
import pyautogui

# Inicializar la cámara
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

frame_count = 0

while cam.isOpened():
    frame_count += 1
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 480))  # Reducir la resolución
    
    if frame_count % 5 != 0:  # Procesar cada 5 frames
        continue
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)
        
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        
        if (left[0].y - left[1].y) < 0.002:
            pyautogui.click(button="right")
            pyautogui.sleep(1)
    
    cv2.imshow('Eye Controlled Mouse', frame)
    
    if cv2.waitKey(1) == ord('s'):
        break

cam.release()
cv2.destroyAllWindows()
