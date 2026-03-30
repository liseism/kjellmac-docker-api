from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return { "msg": "web hooked :-)", "v": "0.2" }


@app.get("/items/{id}")
def read_item(item_id: int, q: str = None):
    return {"id": id, "q": q}

@app.get("/api/ip")
def ip(request: Request):
        return{"ip: request.client.host"}