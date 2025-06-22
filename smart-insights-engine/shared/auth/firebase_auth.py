
import firebase_admin
from firebase_admin import auth, credentials

cred = credentials.Certificate("firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

def verify_token(token: str):
    try:
        decoded = auth.verify_id_token(token)
        return decoded
    except Exception as e:
        return None
