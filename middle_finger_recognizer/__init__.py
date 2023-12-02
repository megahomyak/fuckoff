from mediapipe.python.solutions import hands
import math
import cv2

def _distance(landmark1, landmark2):
    return math.sqrt((landmark1.x - landmark2.x) ** 2 + (landmark1.y - landmark2.y) ** 2)

def wait(camera_index=0):
    """
    Wait until a middle finger appears on camera
    """
    video_capture = cv2.VideoCapture(camera_index)
    with hands.Hands() as hands_recognizer:
        while video_capture.isOpened():
            is_success, frame = video_capture.read()
            if not is_success:
                break
            frame.flags.writeable = False # Makes it faster, from what I've heard
            output = hands_recognizer.process(frame)
            if output.multi_hand_landmarks:
                for hand in output.multi_hand_landmarks:
                    hand = hand.landmark
                    index_finger = hand[hands.HandLandmark.INDEX_FINGER_TIP]
                    middle_finger = hand[hands.HandLandmark.MIDDLE_FINGER_TIP]
                    ring_finger = hand[hands.HandLandmark.RING_FINGER_TIP]
                    pinky = hand[hands.HandLandmark.PINKY_TIP]
                    wrist = hand[hands.HandLandmark.WRIST]
                    other_finger_max_distance = max(
                        _distance(index_finger, wrist),
                        _distance(ring_finger, wrist),
                        _distance(pinky, wrist)
                    )
                    if other_finger_max_distance * 1.5 < _distance(middle_finger, wrist):
                        return
