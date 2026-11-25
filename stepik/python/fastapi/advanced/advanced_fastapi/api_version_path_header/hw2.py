from fastapi import APIRouter, Depends, FastAPI, Header, HTTPException

app = FastAPI()
router = APIRouter(prefix="/api")


def get_api_version(x_api_version: str | None = Header(default=None)) -> str:
    if x_api_version not in ("v1", "v2"):
        raise HTTPException(status_code=400, detail="Invalid or missing API version")
    return x_api_version


def parse_note_id(note_id: str) -> int:
    if not note_id.isdigit() or int(note_id) <= 0:
        raise HTTPException(status_code=400, detail="Invalid note ID")
    return int(note_id)


@router.get("/notes")
def get_notes(version: str = Depends(get_api_version)) -> str:
    if version == "v1":
        return "Notes in v1: Note 1, Note 2"
    return "Notes in v2: Note 1 (draft), Note 2 (published)"


@router.get("/notes/count")
def get_notes_count(version: str = Depends(get_api_version)) -> str:
    if version != "v2":
        raise HTTPException(status_code=400, detail="Invalid or missing API version")
    return "Total notes in v2: 2"


@router.get("/notes/{note_id}")
def get_note(note_id: str, version: str = Depends(get_api_version)) -> str:
    note = parse_note_id(note_id)
    if version == "v1":
        return f"Note {note} in v1"
    return f"Note {note} in v2 with status: draft"


app.include_router(router)
