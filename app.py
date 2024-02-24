from fastapi import FastAPI,Request
from pydantic import BaseModel,Field,validator

app = FastAPI()

class User(BaseModel):
    id : int= None
    username:str= Field(...,min_length=3,max_length=50)#None
    email:str= Field (...,pattern=".") # Debe limpiarese
    image_file:str=None
    name:str=None
    password :str=None

    @validator("username")
    def username_alphanumeric(cls,v):
        if not v.isalnum():
              print(v.isalnum())
              raise ValueError('debe ser alfanumerico')
        return v
#    @validator("name")
#    def name_alphanumeric(cls,v):
#        pattern=r""
#        if not v.isalnum():
#              print(v.isalnum())
#              raise ValueError('debe ser alfanumerico')
#        return v


@app.get("/")
def read_root():
        return {"Hello":"World"}

@app.post("/user")
async def  create_user(request:Request):
    body: User = await request.json()
    print(body)
    user = User(**body)
    print(user)
    return {"user":user}

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)