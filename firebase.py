import firebase_admin
from firebase_admin import db
import json

cred_object = firebase_admin.credentials.Certificate('./firebase-auth-key.json')
default_app = firebase_admin.initialize_app(cred_object, {
	'databaseURL':"https://realtime-db-7f9f3-default-rtdb.asia-southeast1.firebasedatabase.app/"
	})

ref = db.reference("/Kutta_Billi/users")



