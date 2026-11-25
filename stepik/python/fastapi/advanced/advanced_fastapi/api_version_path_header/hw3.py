from fastapi import APIRouter, FastAPI, Header, HTTPException

app = FastAPI()

path_router = APIRouter(prefix="/api")
header_router = APIRouter(prefix="/api")


def build_status(version: int) -> dict:
    if version not in (1, 2):
        raise HTTPException(status_code=400, detail="Unsupported API version")
    return {"version": version, "status": "ok"}


@path_router.get("/v{version}/status")
def get_status_by_path(version: int) -> dict:
    return build_status(version)


@header_router.get("/status")
def get_status_by_header(
    api_version: str | None = Header(default=None, alias="X-API-Version"),
) -> dict:
    if api_version is None:
        return build_status(1)
    if api_version not in ("1", "2"):
        raise HTTPException(status_code=400, detail="Unsupported API version")
    return build_status(int(api_version))


app.include_router(path_router)
app.include_router(header_router)
