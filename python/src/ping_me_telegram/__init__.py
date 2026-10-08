import requests

class PingMeError(Exception):
    """Basic exception"""
    pass

class TokenError(PingMeError):
    """Called for unknown token"""
    pass

class MessageError(PingMeError):
    """Called for empty or unacceptable message"""
    pass

class ServiceError(PingMeError):
    """Called for unavailable service"""
    pass

class TimeoutError(PingMeError):
    """Called for timeout of too often messages"""
    pass

class BanError(PingMeError):
    """Called for banned users"""
    pass

def ping_me(token:str, message:str):
    if not message:
        raise MessageError("Empty or unacceptable message.")
    url = "https://pingmeapi.ruslanissimo.com/send"
    try:
        response = requests.post(url, json={"token": token, "text": message})
        print(response.text)
        if response.status_code == 200:
            if response.text == '{"status":"You are sending messages too often"}':
                raise TimeoutError("You are sending messages too often")
            if response.text == '{"status":"Empty or unacceptable message"}':
                raise MessageError("Empty or unacceptable message.")
            if response.text == '{"status":"Unknown token"}':
                raise TokenError("Unknown token. Check correctness of the token.")
            if response.text == '{"status":"You have been banned from using this service"}':
                raise BanError("You have been banned from using this service")
        else:
            print(response.status_code)
            raise ServiceError("Service is out of order")
    except requests.exceptions.ConnectionError:
        raise PingMeError("Unknown general error")
