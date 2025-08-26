import os
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.security import get_db, get_current_user
from app import models
from app.schemas import DocUploadOut

router = APIRouter(prefix="/drivers", tags=["drivers"])

UPLOAD_DIR = os.path.join(os.getcwd(), "uploads", "drivers")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/{driver_id}/documents", response_model=DocUploadOut)
async def upload_document(driver_id: int, doc_type: str, file: UploadFile = File(...), db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    # only driver themselves or admin can upload
    if user.role != models.Role.admin and user.id != driver_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    # save file
    ext = os.path.splitext(file.filename)[1]
    filename = f"driver_{driver_id}_{doc_type}_{int(__import__('time').time())}{ext}"
    dest = os.path.join(UPLOAD_DIR, filename)
    with open(dest, "wb") as f:
        content = await file.read()
        f.write(content)
    doc = models.DriverDocument(driver_id=driver_id, filename=filename, doc_type=doc_type)
    db.add(doc); db.commit(); db.refresh(doc)
    return doc

@router.get("/admin/documents/pending")
def list_pending(db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    if user.role != models.Role.admin:
        raise HTTPException(status_code=403, detail="Admin only")
    q = db.query(models.DriverDocument).filter(models.DriverDocument.status == models.VerificationStatus.pending).all()
    return q

@router.patch("/admin/documents/{doc_id}/status")
def change_status(doc_id: int, status: str, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    if user.role != models.Role.admin:
        raise HTTPException(status_code=403, detail="Admin only")
    doc = db.get(models.DriverDocument, doc_id)
    if not doc:
        raise HTTPException(404, "Not found")
    doc.status = models.VerificationStatus(status)
    db.add(doc); db.commit(); db.refresh(doc)
    return doc
