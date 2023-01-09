from fastapi import FastAPI

app = FastAPI()


@app.get("/") # декоратор операции пути
async def root():
    return {"message": "Hello World"}



# POST — создает данные
# GET — читает данные
# PUT — обновляет данные
# DELETE — удаляет данные


# команда для запуска программы
# # $ uvicorn main:app --reload