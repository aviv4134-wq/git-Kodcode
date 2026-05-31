from fastapi import FastAPI
import uvicorn

app = FastAPI()



@app.get('/')
def dict_():
    return {"service": "my-api", "version": "1.0"}

@app.get('/user/admin')
def role():
    return {'role': 'admin','access':'full'}





@app.get('/user/{user_id}')
def get_user_id(user_id):
    return {'id': f'{user_id}','name': 'avi','email':'aviv'}


