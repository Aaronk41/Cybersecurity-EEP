import jwt
from jwt import InvalidTokenError, ExpiredSignatureError

def validate_jwt(token, secret_key, algorithms=['HS256']):
    try:
        decoded = jwt.decode(token, secret_key, algorithms=algorithms)
        return True, decoded
    except ExpiredSignatureError:
        return False, "Token has expired."
    except InvalidTokenError as e:
        return False, f"Invalid token: {str(e)}"
