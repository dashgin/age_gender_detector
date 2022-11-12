import cv2
import numpy as np

from config import (
    AGE_LIST,
    AGE_MODEL,
    AGE_PROTO,
    FACE_MODEL,
    FACE_PROTO,
    GENDER_LIST,
    GENDER_MODEL,
    GENDER_PROTO,
    LOCAL,
)

faceNet = cv2.dnn.readNet(FACE_MODEL, FACE_PROTO)


def print_(text):
    if LOCAL:
        print(text)


def highlight_face(frame, conf_threshold=0.7):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    blob = cv2.dnn.blobFromImage(
        frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False
    )

    faceNet.setInput(blob)
    detections = faceNet.forward()
    faceBoxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            faceBoxes.append([x1, y1, x2, y2])
            cv2.rectangle(
                frameOpencvDnn,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                int(round(frameHeight / 150)),
                8,
            )
    return frameOpencvDnn, faceBoxes


def read_image_from_path(path):
    frame = cv2.imread(path)
    return frame


def read_image(image_content):
    image = np.asarray(bytearray(image_content), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


ageNet = cv2.dnn.readNet(AGE_MODEL, AGE_PROTO)
genderNet = cv2.dnn.readNet(GENDER_MODEL, GENDER_PROTO)


def detect_gender(blob):
    genderNet.setInput(blob)
    genderPreds = genderNet.forward()
    gender = GENDER_LIST[genderPreds[0].argmax()]
    print_(f"Gender: {gender}")
    return gender


def detect_age(blob):
    ageNet.setInput(blob)
    agePreds = ageNet.forward()
    age = AGE_LIST[agePreds[0].argmax()]
    print_(f"Age: {age[1:-1]} years")
    return age


def put_text_above_rectangle(image, text, cordinates):
    cv2.putText(
        image,
        text,
        cordinates,
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2,
        cv2.LINE_AA,
    )




def ndarray_to_b64(ndarray):
    img = cv2.cvtColor(ndarray, cv2.COLOR_BGR2RGB)
    _, buffer = cv2.imencode(".png", img)
    return base64.b64encode(buffer).decode("utf-8")
