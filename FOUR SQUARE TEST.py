import cv2
import mediapipe as mp
from deepface import DeepFace
def detect_emotion(face_image):
    try:
        result = DeepFace.analyze(face_image, actions=['emotion'],enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        return emotion
    except Exception as e:
        print("Error:", str(e))
        return None
def main():
    mp_face_detection = mp.solutions.face_detection
    face_detection = mp_face_detection.FaceDetection()
    cap = cv2.VideoCapture(0)
    image1 = cv2.imread('filters/angry.png', -1)
    # image2 = cv2.imread(filter_path, -1)
    # image3 = cv2.imread(filter_path, -1)
    # image4 = cv2.imread(filter_path, -1)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(frame_rgb)
        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                       int(bboxC.width * iw), int(bboxC.height * ih)
                face_image = frame[bbox[1]:bbox[1]+bbox[3], bbox[0]:bbox[0]+bbox[2]]
                emotion = detect_emotion(face_image)
                if emotion:
                    filter_path = f'filters/{emotion}.png'
                    overlay_image = cv2.imread(filter_path, -1)
                    cv2.putText(frame, emotion, (bbox[0], bbox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    overlay_resized = cv2.resize(overlay_image, (bbox[2], bbox[3]))
                    overlay_x, overlay_y = bbox[0], bbox[1]
                    overlay_alpha_s = overlay_resized[:, :, 3] / 255.0
                    overlay_alpha_l = 1.0 - overlay_alpha_s
                    for c in range(0, 3):
                        frame[overlay_y:overlay_y+bbox[3], overlay_x:overlay_x+bbox[2], c] = \
                            (overlay_alpha_s * overlay_resized[:, :, c] +
                            overlay_alpha_l * frame[overlay_y:overlay_y+bbox[3], overlay_x:overlay_x+bbox[2], c])
                # cv2.rectangle(frame, bbox, (0, 255, 0), 2)
        overlay_height, overlay_width, _ = frame.shape
        overlay_height //= 4
        overlay_width //= 4

        top_left_image_resized = cv2.resize(image1, (overlay_width, overlay_height))
        # top_right_image_resized = cv2.resize(image1, (overlay_width, overlay_height))
        # bottom_left_image_resized = cv2.resize(image1, (overlay_width, overlay_height))
        # bottom_right_image_resized = cv2.resize(image1, (overlay_width, overlay_height))

        alpha = .5  # Adjust transparency here
        frame[0:overlay_height, 0:overlay_width] = cv2.addWeighted(frame[0:overlay_height, 0:overlay_width], alpha,
                                                                   top_left_image_resized[:, :, 3], 1 - alpha, 0)
        # frame[0:overlay_height, -overlay_width:] = cv2.addWeighted(frame[0:overlay_height, -overlay_width:], alpha,
        #                                                            top_right_image_resized[:, :, 3], 1 - alpha, 0)
        # frame[-overlay_height:, 0:overlay_width] = cv2.addWeighted(frame[-overlay_height:, 0:overlay_width], alpha,
        #                                                             bottom_left_image_resized[:, :, 3], 1 - alpha, 0)
        # frame[-overlay_height:, -overlay_width:] = cv2.addWeighted(frame[-overlay_height:, -overlay_width:], alpha,
        #                                                             bottom_right_image_resized[:, :, 3], 1 - alpha, 0)
        cv2.imshow('Face Emotion Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()