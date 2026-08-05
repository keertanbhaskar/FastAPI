from fastapi import APIRouter

router = APIRouter()

@router.post("/faculty")
def create_user():
    return {"message": "faculty Created"}