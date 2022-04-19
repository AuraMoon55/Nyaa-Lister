from os import getenv
from dotenv import load_dotenv
from program import Client
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient


load_dotenv()

API_ID = 2919867

API_HASH = "90dd95178a8d13a69bfdbc7da68d23a4"

TOKEN = "1954044423:AAGGfY1GACbSJxZGGC0VSW06OtD78MriNJc"
_mongo_client = MongoClient("")
db = _mongo_client.nyaa


LOGS = -1001731155585


app = Client(
  "bot",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=TOKEN
)

"""
app2 = Client(
  SESSION,
  api_id=API_ID,
  api_hash=API_HASH,
)
"""

print("STARTING BOT")
app.start()
#app2.start()

print("FETCHING INFO")
x = app.get_me()

print("PARSING INFO")
BOT_NAME = x.first_name + (x.last_name + "")
BOT_UNAME = x.username
BOT_ID = x.id
BOT_MENTION = x.mention
print("PARSED INFO")
