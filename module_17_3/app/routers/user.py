from fastapi import APIRouter

router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users():
    pass


@router.get('/user_id')
async def user_by_id():
    pass


@router.post('/create')
async def create_user():
    pass


@router.put('/update')
async def update_user():
    pass


@router.delete('/delete')
async def delete_user():
    pass
