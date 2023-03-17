from cv2 import cv2
import mediapipe as mp

FRAME_WIDTH = 1240
FRAME_HEIGHT = 680
TL = (0, 0)  # top left
TT = (FRAME_WIDTH // 2, 0)  # top middle
TR = (FRAME_WIDTH, 0)  # top right
ML = (0, FRAME_HEIGHT // 2)  # middle left
MM = (FRAME_WIDTH // 2, FRAME_HEIGHT // 2)  # centre
MR = (FRAME_WIDTH, FRAME_HEIGHT // 2)  # middle right
BL = (0, FRAME_HEIGHT)  # bottom left
BB = (FRAME_WIDTH // 2, FRAME_HEIGHT)  # bottom middle
BR = (FRAME_WIDTH, FRAME_HEIGHT)  # bottom right

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic
mp_hands = mp.solutions.hands


def main():
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while True:
            success, frame = capture.read()
            if not success:
                print("Ignoring empty camera frame.")
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = holistic.process(image)
            image.flags.writeable = True

            cv2.line(image, ML, MR, (0, 0, 255), 1)
            cv2.line(image, TT, BB, (0, 0, 255), 1)

            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            mp_drawing.draw_landmarks(
                image,
                results.face_landmarks,
                mp_holistic.FACEMESH_CONTOURS,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles
                .get_default_face_mesh_contours_style())
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_holistic.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles
                .get_default_pose_landmarks_style())

            cv2.imshow("Webcam", image)

            if cv2.waitKey(1) == ord('q'):
                capture.release()
                cv2.destroyAllWindows()
                break


if __name__ == '__main__':
    main()
