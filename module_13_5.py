from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserStates(StatesGroup):
    age = State()
    growth = State()
    weight = State()


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.add(button1, button2)


@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет, я бот помогающий твоему здоровью', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserStates.age.set()


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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
