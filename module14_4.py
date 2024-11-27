from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import filters
from aiogram.utils import executor
from crud_functions import initiate_db, get_all_products, populate_products
import os

initiate_db()
#populate_products()

API_TOKEN = '7545702137:AAFmT_fwP09R5q35yTR0VgMvrL55nQMYKCQ'
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)



# Главная клавиатура с кнопкой "Купить"
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buy_button = types.KeyboardButton('Купить')
    keyboard.add(buy_button)
    await message.answer("Добро пожаловать! Выберите действие.", reply_markup=keyboard)


@dp.message_handler(filters.Text(equals="Купить"))
async def get_buying_list(message: types.Message):
    products = get_all_products()
    if not products:
        await message.answer("Список покупок пуст.")
    else:
        for product in products:
            title, description, price = product
            await message.answer(f"Название: {title}\nОписание: {description}\nЦена: {price}")



@dp.callback_query_handler(lambda call: call.data == "product_buying")
async def send_confirm_message(call: types.CallbackQuery):
    await call.answer()  # Убираем спиннер
    await call.message.answer("Вы успешно приобрели продукт!")


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)