import telebot


bot = telebot.TeleBot("BOTTOKEN")



def get_chat(userid):
    try:
        result = bot.get_chat_member(chat_id="@xunixuz",user_id=userid).status
    except:
        return False
    

    if result=='left':
        return False
    else:
        return True



@bot.message_handler(commands=['start'])
def start_message(msg):
    chatid = msg.chat.id
    result = get_chat(chatid)


    
    if result:
        bot.reply_to(msg,"Siz kanalga obuna bo'lgansiz!")
    else:
        bot.reply_to(msg,"Iltimos kanalga obuna bo'ling!\n\nKanal: @xunixuz")



print(bot.get_me())
bot.infinity_polling()
