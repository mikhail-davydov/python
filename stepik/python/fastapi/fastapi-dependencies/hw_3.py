from fastapi import FastAPI, HTTPException, Depends
from starlette import status

app = FastAPI()


def check_auth(token: str):
    if "secret" != token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")


@app.get("/profile", dependencies=[Depends(check_auth)])
async def profile() -> str:
    return "User is authorized"

# alt

def check_auth(token: str):
    if "secret" == token:
        return True
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")


@app.get("/profile")
async def profile(_ = Depends(check_auth)) -> str:
    return "User is authorized"


# alt

async def check_auth(token: str):
    if token == 'secret':
        return "User is authorized"
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized')


@app.get('/profile')
async def is_auth(message: str = Depends(check_auth)):
    return message


# alt

def check_auth(token: str):
    if "secret" == token:
        return True
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")


@app.get("/profile")
async def profile(check_auth: bool = Depends(check_auth)) -> str:
    return "User is authorized"
