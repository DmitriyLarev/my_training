from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import *

api = '7092427653:AAElgxQoF0sbxEQp02l56YHvbUdJ1UspZV0'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

initiate_db()
products = get_all_products()


class UserStates(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000


kb = ReplyKeyboardMarkup(
    keyboard=
    [
        [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')],
        [KeyboardButton(text='Регистрация')]
    ], resize_keyboard=True
)

in_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
        ]
    ]
)

products_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Продукт 1', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт 2', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт 3', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')
        ]
    ]
)


@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет, я бот помогающий твоему здоровью', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=in_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserStates.age.set()
    await call.answer()


@dp.message_handler(state=UserStates.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserStates.growth.set()


@dp.message_handler(state=UserStates.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserStates.weight.set()


@dp.message_handler(state=UserStates.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    norm = 10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) + 5
    await message.answer(f'Ваша норма калорий {norm}')
    await state.finish()


@dp.message_handler(text='Регистрация')
async def sign_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if not is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь существует, введите другое имя')
        await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_your_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer('Регистрация прошла успешно')
    await state.finish()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for product in products:
        await message.answer(f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}")
        with open(f'img{product[0]}.png', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=products_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
