from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


STATIC_DIR = BASE_DIR / "static"


FACE_PROTO = str(STATIC_DIR / "opencv_face_detector.pbtxt")
FACE_MODEL = str(STATIC_DIR / "opencv_face_detector_uint8.pb")
AGE_PROTO = str(STATIC_DIR / "age_deploy.prototxt")
AGE_MODEL = str(STATIC_DIR / "age_net.caffemodel")
GENDER_PROTO = str(STATIC_DIR / "gender_deploy.prototxt")
GENDER_MODEL = str(STATIC_DIR / "gender_net.caffemodel")

AGE_LIST = [
    "(0-2)",
    "(4-6)",
    "(8-12)",
    "(15-20)",
    "(25-32)",
    "(38-43)",
    "(48-53)",
    "(60-100)",
]
GENDER_LIST = ["Male", "Female"]
MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

LOCAL = True
