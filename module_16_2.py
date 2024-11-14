from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def get_main_page():
    return "Главная страница"


@app.get("/user/admin")
async def get_admin_page():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def get_user_number(user_id: int = Path(ge=1, le=100, description='Enter User ID', example=55)):
    return f"Вы вошли как пользователь № {user_id}"


@app.get('/user/{username}/{age}')
async def get_user_info(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
