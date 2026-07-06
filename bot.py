import telebot, time, random, os
from threading import Thread

TOKEN = os.environ.get('TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
bot = telebot.TeleBot(TOKEN)

def enviar():
    while True:
        cor = random.choice(['AZUL', 'VERMELHO'])
        bot.send_message(CHAT_ID, f"✅ ENTRADA: {cor}\n🟡 Proteção: Empate")
        time.sleep(300) # 5 minutos

Thread(target=enviar).start()
bot.polling()
