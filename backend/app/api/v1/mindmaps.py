from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.mindmap import Mindmap
from app.services.freeplane_parser import parse_freeplane
import uuid

router = APIRouter(
    prefix="/mindmaps",
    tags=["mindmaps"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ------------------------
# POST /mindmaps/ → upload a .mm file
# ------------------------
@router.post("/")
async def upload_mindmap(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    if not file.filename.endswith(".mm"):
        raise HTTPException(status_code=400, detail="Only .mm files allowed")

    xml_bytes = await file.read()
    xml_text = xml_bytes.decode("utf-8")

    # Parse like a Freeplane session
    parsed = parse_freeplane(xml_text)

    # Save in DB
    mindmap = Mindmap(
        id=str(uuid.uuid4()),
        title=parsed["title"],
        xml_content=xml_text,
    )

    db.add(mindmap)
    db.commit()
    db.refresh(mindmap)  # refresh to get committed state

    return {
        "id": mindmap.id,
        "title": mindmap.title,
        "root_node": parsed["root"]["text"],
    }


# ------------------------
# GET /mindmaps/{id}/session → get parsed session
# ------------------------
@router.get("/{mindmap_id}/session")
def get_mindmap_session(
    mindmap_id: str,
    db: Session = Depends(get_db)
):
    mm = db.get(Mindmap, mindmap_id)
    if not mm:
        raise HTTPException(status_code=404, detail="Mindmap not found")

    return parse_freeplane(mm.xml_content)
