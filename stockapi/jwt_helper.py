from os import error
import jwt
from stockapi.user import User
from stockapi.config import Config


def encode_jwt_token(user: User):
    payload = {
        "email": user.email,
        "role": user.role_id,
        "fn": user.fn,
        "ln": user.ln,
        "project": Config.PROJECT_NAME
    }
    encoded_jwt = jwt.encode({"some": payload}, "secret", algorithm="HS256")
    return encoded_jwt;


def decode_jwt_token(token):
    try:
        decoded_token = jwt.decode(token, "secret", algorithms="HS256")
        payload = decoded_token["some"];
        return payload;
    except error as e:
        print(e)
        return None
