from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# sample data
pottery = [
    {"id": 1, "name": "Moss Glazed Mug", "price": 65},
    {"id": 2, "name": "Stoneware Bowl", "price": 90},
]

@app.get("/")
def read_root():
    return {"message": "Welcome to The Clay Route Project API"}

@app.get("/pottery")
def pottery_items():
    return pottery

# 🧱 new: pottery detail
@app.get("/pottery/{item_id}")
def pottery_item(item_id: int):
    for p in pottery:
        if p["id"] == item_id:
            return p
    raise HTTPException(status_code=404, detail="item not found")

# 🧱 new: contact form receiver
@app.post("/contact")
async def contact(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    print(f"📩 message from {name} ({email}) — {message}")
    return {"success": True, "message": "Message received!"}
