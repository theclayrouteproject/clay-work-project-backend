from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Serve static assets from /static and provide a simple form at /form
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to The Clay Route Project API"}


@app.get("/form")
def form_page():
    return FileResponse("static/index.html")

@app.get("/pottery")
def pottery():
    return [
        {"id": 1, "name": "Moss Glazed Mug", "price": 65},
        {"id": 2, "name": "Stoneware Bowl", "price": 90},
    ]

@app.get("/pottery/{item_id}")
def get_item(item_id: int):
    items = [
        {"id": 1, "name": "Moss Glazed Mug", "price": 65},
        {"id": 2, "name": "Stoneware Bowl", "price": 90},
    ]
    for i in items:
        if i["id"] == item_id:
            return i
    return {"error": "Not found"}


@app.get("/glazes")
def get_glazes():
    return [
        {"id": 1, "name": "Celadon Mist", "finish": "Smooth semi-gloss green", "cone": 6},
        {"id": 2, "name": "Iron Rutile", "finish": "Rust-brown satin texture with flecks", "cone": 5},
        {"id": 3, "name": "Shino White", "finish": "Milky matte white with iron spotting", "cone": 10},
    ]

@app.post("/contact")
async def contact(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    print(f"📩 {name} ({email}): {message}")
    return {"success": True, "detail": "Message received"}
