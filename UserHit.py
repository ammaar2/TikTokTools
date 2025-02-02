import random
import threading
from os import system
try:
    import telebot
    import ms4
except ImportError:
    system("pip install telebot")
    system("pip install ms4")

from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from ms4 import InfoTik

tok = input('Enter your token : ')
bot = telebot.TeleBot(tok)

print("""

روح للبوت ودز /start

""")

@bot.message_handler(commands=['start'])
def start_handler(message):
    btn_developer_channel = InlineKeyboardButton(text="قناة مطور بوت", url="https://t.me/jokerpython3")
    btn_start_tik_hunt = InlineKeyboardButton(text="بدا صيد يوزرات رباعيات تيك", callback_data="start_hunt")
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(btn_developer_channel, btn_start_tik_hunt)

    bot.send_message(
        message.chat.id, 
        "أهلاً بك في بوت صيد يوزرات رباعيات تيك\nCHANEL DEF | @w6_6w", 
        reply_markup=markup
    )

def hunt_usernames(call, g, b):
    characters = "1234567890qwertyuiopasdfghjklzxcvbnm"

    while True:
        username = "".join(random.choices(characters, k=4))
        info = InfoTik.TikTok_Info(username)
        print(info)

       
        if info.get('error') == 'Invalid username' and info.get('status') == 'bad':
            g += 1
            bot.send_message(call.message.chat.id, f"متاح: {username}")
        else:
            b += 1

      
        btn_good = InlineKeyboardButton(text=f"متاح: {g}", callback_data="good_count")
        btn_bad = InlineKeyboardButton(text=f"غير متاح: {b}", callback_data="bad_count")
        btn_current_user = InlineKeyboardButton(text=f"اليوزر الحالي: {username}", callback_data="current_user")
        result_markup = InlineKeyboardMarkup(row_width=1)
        result_markup.add(btn_good, btn_bad, btn_current_user)

        
        bot.edit_message_text(
            chat_id=call.message.chat.id, 
            message_id=call.message.message_id,
            text="جاري البحث عن يوزرات تيك...",
            reply_markup=result_markup
        )

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "start_hunt":
        g = 0  
        b = 0


        threading.Thread(target=hunt_usernames, args=(call, g, b)).start()

bot.polling()