import argparse

import cv2

from config import MODEL_MEAN_VALUES
from utils import (
    detect_age,
    detect_gender,
    highlight_face,
    put_text_above_rectangle,
    read_image,
)

parser = argparse.ArgumentParser()
parser.add_argument("--image")
args = parser.parse_args()


def detect_gender_age():
    path = args.image
    frame = read_image(path)

    result_img, face_boxes = highlight_face(frame)

    if not face_boxes:
        print("No face detected")
        return None

    padding = 20

    for face_box in face_boxes:
        face = frame[
            max(0, face_box[1] - padding) : min(
                face_box[3] + padding, frame.shape[0] - 1
            ),
            max(0, face_box[0] - padding) : min(
                face_box[2] + padding, frame.shape[1] - 1
            ),
        ]

        blob = cv2.dnn.blobFromImage(
            face,
            1.0,
            (227, 227),
            MODEL_MEAN_VALUES,
            swapRB=False,
        )

        gender = detect_gender(blob)

        age = detect_age(blob)
        cordinates = (face_box[0], face_box[1] - 10)
        text = f"{gender}, {age}"
        put_text_above_rectangle(result_img, text, cordinates)

    cv2.imwrite("result.jpg", result_img)


detect_gender_age()
