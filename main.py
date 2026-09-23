from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return "welcome to fastapi"

@app.get("/items/{item_id}")
def getItem(item_id):
    return {"id" : item_id,
            "type" : str(type(item_id))
            }

@app.get("/search")
def search(q: str = ""):
    return {
        "q": q
    }