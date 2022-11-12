from fastapi import FastAPI, File, Request, UploadFile
from fastapi.templating import Jinja2Templates

from utils import ndarray_to_b64

app = FastAPI()


templates = Jinja2Templates(directory="templates")


@app.get("/login")
def read_item(request: Request):

    data_from_html = "data_from_html"
    print(data_from_html)
    return templates.TemplateResponse(
        name="login.html",
        context={
            "request": request,
        },
    )


users = {
    "Dashgin Khudiyev": {
        "username": "dashgin",
        "password": "dashgin123",
    }
}


@app.get("/b")
def b(request: Request, username, password):

    for user, user_data in users.items():
        if user_data["username"] == username and user_data["password"] == password:
            return templates.TemplateResponse(
                name="b.html",
                context={
                    "request": request,
                    "name": user,
                },
            )

    return templates.TemplateResponse(
        name="b.html",
        context={
            "request": request,
            "name": "Invalid username or password",
        },
    )


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        context={
            "request": request,
        },
    )


from detect import detect_gender_age


@app.post("/detect")
def detect(request: Request, fileb: UploadFile = File(...)):

    deteceted_image = detect_gender_age(fileb.file.read())
    image_for_show_html = ndarray_to_b64(deteceted_image)

    return templates.TemplateResponse(
        "display.html",
        context={
            "request": request,
            "image": image_for_show_html,

        },
    )
