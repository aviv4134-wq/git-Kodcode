from fastapi import FastAPI
import datetime
app = FastAPI()

@app.get('/status')
def get_datetime():
    return {'server name':'serv 1','time':f'{datetime.datetime.now()}'}
print(datetime.datetime.now())