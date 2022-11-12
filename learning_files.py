from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.post("/files/")
def create_file(fileb: UploadFile = File(), token: str = Form()):
    return {
        # "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
