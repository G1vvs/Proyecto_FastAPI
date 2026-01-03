 # py -m pip install "fastapi[standard]"

from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)

app.include_router(jwt_auth_users.router)
app.include_router(basic_auth_users.router)
app.include_router(users_db.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "Holla FastAPI"
# para iniciar el server: py -m uvicorn main:app --reload

@app.get("/url")
async def url():
    return {"url_curso": "https://giova.com"}

# detener el server ctrl + C


#documentacion redocly: http://127.0.0.1:8000/redoc
#documentacion swagger: http://127.0.0.1:8000/docs

# Pruebas en Postman
# o en thunder client(extension vscode)


