from telegram import Bot, Update, ParseMode
from telegram.ext import run_async
from bot import dispatcher
from bot.modules.disable import DisableAbleCommandHandler
from bot.modules.helper_funcs.chat_status import user_admin
import json
import requests

@user_admin
@run_async
def meme(bot: Bot, update: Update):
	res = requests.get("https://meme-api.herokuapp.com/gimme")
	bot.send_photo(update.effective_chat.id,json.loads(res.text).get('url'))
	
__help__ = """
• `/meme`*:* Sends Meme. 
"""	
MEME_HANDLER = DisableAbleCommandHandler("meme", meme)
dispatcher.add_handler(MEME_HANDLER)    

__mod_name__ = "Meme"
__command_list__ = ["meme"]	
__handlers__ = [MEME_HANDLER]
