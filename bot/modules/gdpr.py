from telegram import Bot, Update, ParseMode
from telegram.ext import run_async
import time
from bot.modules.helper_funcs.extraction import extract_user
from bot import dispatcher
from bot.modules.disable import DisableAbleCommandHandler

@run_async
def gdpr(bot: Bot, update: Update):
        message = update.effective_message
        chat = update.effective_chat
        user = update.effective_user
        if chat.type == 'private':
                message.reply_text("Deleting identifiable data...")
                time.sleep(2)
                message.reply_text("Almost done, Just be Patient")
                time.sleep(2)
                message.reply_text("My Ass! do not come here AGAIN. If you are gbanned this cmd will not revert it. So kindly GTFO.")
                message.reply_text("Pajeet confirm")

GDPR_HANDLER = DisableAbleCommandHandler("gdpr", gdpr)
dispatcher.add_handler(GDPR_HANDLER)  
