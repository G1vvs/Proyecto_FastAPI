
# py -m pip install "fastapi[standard]"
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# usuarios

#Entidad User
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [
              User(id=1, name="Giovanni", surname="Sanhueza", url="https://giova.com", age=21),
              User(id=2, name="Moure", surname="Brais", url="https://mouredev.com", age=31),
              User(id=3, name="Peruanito", surname="Cuscos", url="https://cuscos.com", age=22)]

users_db = {
    "giovanni":{
        "username": "giovanni",
       "full_name": "Giovanni Sanhueza",
        "email": "giov@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    "giovanni2":{
        "username": "giovanni2",
       "full_name": "Giovanni Sanhueza2",
        "email": "giov2@gmail.com",
        "disabled": True,
        "password": "654321"
    }
}



@router.get("/users")
async def users():
    return users_list

# Path
@router.get("/userdb/{id}")
async def user(id: int):
    return search_user(id)
    
# Query
@router.get("/user/")
async def user(id: int):
    return search_user(id)
    
# Post
@router.post("/user/", response_model=User, status_code= 201)
async def user(user: User):
   if type(search_user(user.id)) == User:
         raise HTTPException(status_code=404, detail= "el usuario ya existe")

   
   else:
        users_list.append(user)
        return user

# Put
@router.put("/user/", response_model=User, status_code=201 )
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        raise HTTPException(status_code=404, detail= "no se actualizo el usuario")
    
    return user

# Delete
@router.delete("/user/{id}")
async def user(id: int):  

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error":" no se a eliminado el usuario"}
           

# search
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
         return list(users)[0]
    except:
        return {"error":" no se encontraron usuarios"}
    



