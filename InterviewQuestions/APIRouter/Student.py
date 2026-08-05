
from fastapi import APIRouter

router = APIRouter()

@router.get('/students')
def get_users():
  return { 'message':'ALL users'}