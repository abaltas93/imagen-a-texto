from fastapi import FastAPI, UploadFile
from PIL import Image
import shutil
from tempfile import NamedTemporaryFile
from pathlib import Path
import pytesseract

UPLOAD_FOLDER = '/api/images'

app = FastAPI()

@app.post("/upload")
def upload_file(upload_file: UploadFile):
    try:
        suffix = Path(upload_file.filename).suffix
    
        new_file = NamedTemporaryFile(suffix=suffix, dir='/opt/imgs').name
        with open(new_file, "wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)

        # Convierte la imagen a texto
        img = Image.open(upload_file.file)
        text = pytesseract.image_to_string(img, 'spa')

        return {'texto': text}
    finally:
        upload_file.file.close()