
import telebot
from telebot import types
import time

# 1. ቦት ቶከን
API_TOKEN = '8647026502:AAGYr4h8Grot0w2vbJQoJYpC3-KOIkZwxl4'
bot = telebot.TeleBot(API_TOKEN)

# 2. ዳታዎች (PDF እና Quiz)
FILES = {
    "bio12": "BQACAgQAAxkBAANUadE0mCuw4dg3wENZCTpg-FSK_zAAAkIcAAIGFIBSQ-dHWnR_1n47BA",
    "bio11": "BQACAgQAAxkBAAPSadFKprejG0CBKY2hIOFxlouKBCsAAkwcAAIGFIBSmw80ou3c9O87BA"
}

QUIZ_DATA = [
    {"q": "1. Which field studies chemical processes in living organisms?", "opts": ["Biophysics", "Biochemistry", "Cytology", "Ecology"], "ans": 1, "def": "Biochemistry studies chemical processes in living things."},
    {"q": "2. The study of physical principles in biological systems is:", "opts": ["Biomechanics", "Biophysics", "Morphology"], "ans": 1, "def": "Biophysics applies physics to biological systems."},
    {"q": "3. The study of tissues using microscopes is:", "opts": ["Anatomy", "Histology", "Physiology"], "ans": 1, "def": "Histology is the study of tissues."},
    {"q": "4. Study of cell structure and function is:", "opts": ["Histology", "Cytology", "Anatomy"], "ans": 1, "def": "Cytology is the study of cells."}
]

# --- ሜኑዎች ---
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Quiz 📝", "PDF Library 📚")
    markup.add("Settings ⚙️")
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "እንኳን ወደ Gobeze Student ቦት በደህና መጡ! 🎓", reply_markup=main_menu())

@bot.message_handler(func=lambda m: m.text == "PDF Library 📚")
def pdf_lib(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Grade 12 Bio Full", callback_data="file_bio12"))
    markup.add(types.InlineKeyboardButton("Grade 11 Bio U1-5", callback_data="file_bio11"))
    bot.send_message(message.chat.id, "Select PDF:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "Quiz 📝")
def start_quiz(message):
    send_q(message.chat.id, 0)

def send_q(chat_id, idx, msg_id=None):
    if idx < len(QUIZ_DATA):
        item = QUIZ_DATA[idx]
        markup = types.InlineKeyboardMarkup(row_width=1)
        for i, opt in enumerate(item["opts"]):
            markup.add(types.InlineKeyboardButton(opt, callback_data=f"ans_{idx}_{i}"))
        txt = f"Question {idx + 1}:\n\n{item['q']}"
        if msg_id: bot.edit_message_text(txt, chat_id, msg_id, reply_markup=markup)
        else: bot.send_message(chat_id, txt, reply_markup=markup)
    else:
        bot.send_message(chat_id, "ጥያቄዎቹን ጨርሰሃል! 🎉")

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data.startswith("file_"):
        f_id = FILES.get(call.data.replace("file_", ""))
        bot.send_document(call.message.chat.id, f_id, caption="መልካም ጥናት! @Ethio_Edunews")
    elif call.data.startswith("ans_"):
        _, q_idx, opt_idx = call.data.split("_")
        q_idx, opt_idx = int(q_idx), int(opt_idx)
        item = QUIZ_DATA[q_idx]
        res = "✅ ትክክል!" if opt_idx == item["ans"] else f"❌ ተሳስተሃል! መልስ: {item['opts'][item['ans']]}"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Next Question ➡️", callback_data=f"next_{q_idx + 1}"))
        bot.edit_message_text(f"{res}\n\n💡 {item['def']}", call.message.chat.id, call.message.id, reply_markup=markup)
    elif call.data.startswith("next_
