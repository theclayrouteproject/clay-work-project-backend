from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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

@app.post("/contact")
async def contact(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    print(f"📩 {name} ({email}): {message}")
    return {"success": True, "detail": "Message received"}
