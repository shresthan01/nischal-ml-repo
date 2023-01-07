from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from typing import List

pipeline = pipeline("translation_en_to_ro", model='model/t5-small')

app = FastAPI()

class TextToTranslate(BaseModel):
    input_text: str

class TextToTranslateList(BaseModel):
    input_text: List[str]

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/ping")
def ping():
    return {"message": "pong"}
    
@app.post("/echo")
def echo(text_to_translate: TextToTranslate):
    return {"message": text_to_translate.input_text}

@app.post("/translate_text")
def translate_text(text_to_translate: TextToTranslate):
    return {"message": pipeline(text_to_translate.input_text)}

@app.post("/translate_list_text")
def translate_text(text_to_translate_list: TextToTranslateList):
    return {"message": pipeline(text_to_translate_list.input_text)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)