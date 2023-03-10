from fastapi import FastAPI, Query, Body
from fastapi.responses import FileResponse

app = FastAPI()


# @app.get("/users")
# def users(people: list[str] = Query()):
#     return {"people": people}


@app.get("/")
def home():
    return FileResponse("public/index.html")


@app.post("/hello")
# def hello(data = Body()):
def hello(name:str  = Body(embed=True, min_length=3, max_length=20),
            age: int = Body(embed=True, ge=18, lt=111)):
    return {"message": f"{name}, ваш возраст - {age}"}