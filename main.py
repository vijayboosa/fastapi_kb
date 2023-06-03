
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Device, DeviceLocations

from firebase_admin import credentials, auth, initialize_app,db
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

cred_object = credentials.Certificate('./firebase-auth-key.json')
default_app = initialize_app(cred_object, {
	'databaseURL':"https://realtime-db-7f9f3-default-rtdb.asia-southeast1.firebasedatabase.app/"
	})

ref = db.reference("/Kutta_Billi/tracking")

app = FastAPI()

allow_all = ['*']
app.add_middleware(
   CORSMiddleware,
   allow_origins=allow_all,
   allow_credentials=True,
   allow_methods=allow_all,
   allow_headers=allow_all
)
 

@app.post('/track-device')
def track_device(location: DeviceLocations):
    try:
        print(location)
        data = jsonable_encoder(location)
        ref.push().set(data)
        return JSONResponse(content={'status': "ok"}, status_code=200)
    except Exception as e:
        print(e)
        return HTTPException(detail={'message': 'There was an error logging in'}, status_code=400)

