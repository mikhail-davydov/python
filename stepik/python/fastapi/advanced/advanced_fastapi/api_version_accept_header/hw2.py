import re
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/report")
def get_report(request: Request) -> JSONResponse:
    accept = request.headers.get("accept")
    if not accept:
        raise HTTPException(status_code=406, detail="Not Acceptable")

    match = re.search(
        r"application/vnd\.mycompany\.v([12])\+json\s*(?=$|[;,])", accept
    )
    if not match:
        raise HTTPException(status_code=406, detail="Not Acceptable")

    version = int(match.group(1))
    if version == 1:
        content = {"version": 1, "total": 3}
        media_type = "application/vnd.mycompany.v1+json"
    else:
        content = {"version": 2, "items": [1, 2, 3]}
        media_type = "application/vnd.mycompany.v2+json"

    return JSONResponse(
        content=content,
        media_type=media_type,
        headers={"Vary": "Accept"},
    )
