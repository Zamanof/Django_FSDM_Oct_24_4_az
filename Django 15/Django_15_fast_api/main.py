from fastapi import FastAPI, Form, Depends
from fastapi.encoders import jsonable_encoder

from fastapi.responses import HTMLResponse, JSONResponse, Response, FileResponse
from pydantic import BaseModel
from starlette.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


class User(BaseModel):
    email: str
    password: str

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/index")
async def index():
    html = "<h1 style='color:red;'>Hello Fast API</h1>"
    return HTMLResponse(html)

@app.get("/index-get-text")
async def index_get_text():
    html = "<h1 style='color:red;'>FastAPI get text</h1>"
    return Response(content=html, media_type="text/plain")

@app.get("/get-json")
async def get_json():
    data = {
        "name": "Fast API",
        "version": "1.0.0",
        "description": "Fast API",
    }
    json_data = jsonable_encoder(data)
    return JSONResponse(json_data)


# @app.get("/get-html")
# async def get_html():
#     return FileResponse('public/index.html')

@app.get("/get-html", response_class=FileResponse)
async def get_html():
    return 'public/index.html'


@app.get("/get-image")
async def get_image():
    return FileResponse('static/rest_api.webp', media_type='image/webp')


@app.get("/download-image")
async def download_image():
    return FileResponse(
        'static/rest_api.webp',
        media_type='application/octet-stream',
        filename='logo.webp'
    )


@app.get("/get-human")
async def get_human(name:str, age:int):
    name = name.upper()
    return {"name": name, "age": age}



def as_user_from_form(
        email:str=Form(...),
        password:str = Form(...)):
    return User(email=email, password=password)

@app.post("/login")
async def login(user: User=Depends(as_user_from_form)):
    return {
        "email": user.email,
        "password": user.password
    }


