from Boy import BOT_NAME, BOT_UNAME, BOT_ID, BOT_MENTION, app, LOGS
from pyrogram import filters, idle
from pyrogram.types import InlineKeyboardMarkup as ikm, InlineKeyboardButton as ikb
from .utils import get_feed, get_latest, save_latest

@app.on_message(filters.command("start"))
async def _start(bot, message):
  await message.reply_text("Hi, I am Alive")
  while True:
    x = get_feed()[0]
    y = await get_latest()
    if y in x:
      time.sleep(300)
    else:
      await app.send_message(LOGS, x)
      await save_latest(x)



if __name__ == "__main__":
  app.send_message(LOGS, "Hi, I am Alive")
  idle()
