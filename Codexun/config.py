from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCTT3XwCpeu2KD9VYNp27GjsuPSUuOblwAJsP-dZSssfXDsaxtN9fhYSo5yxadiut9Xyamfs6sURdB5yIG7hWc9i1-QM3v6xE4QG5scVn4XC0WGtIR1Sg5AsRcSYI6B7yEwX9WHwPkBhxI89SXkDUzj_dYmPubejCNHzc9C9fOOV7cPgWaW7_eIvd7UFQSdr0sWbZp3IsTikoyDCM-_2iTP-OCHvQBpLMOq4e61nzAwxTZvqxrtT1JzzYqmtqAGtO26qFBwxbSpbulCiObNYAcHzlCVQChj9EjchY9Pr8NfZCLVPeK3ahFmZlfyI-8dg6Ymw3ztLN5unITIutelZ28iAAAAAUYNJBMA")
BOT_TOKEN = getenv("BOT_TOKEN", "5482381188:AAHQogFsekdIqeJ89K0ylp7GonPojuGZPVY")
BOT_NAME = getenv("BOT_NAME", "NixaX")
BOT_USERNAME = getenv("BOT_USERNAME", "MusicClonerBot")
ASSID = int(getenv("ASSID", "5470233619"))
ASSNAME = getenv("ASSNAME", "SankiX")
ASSUSERNAME = getenv("ASSUSERNAME", "NixaXAssistant")
BOT_ID = int(getenv("BOT_ID", "5482381188"))
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/PavanMagar/CodexunMusicBot")
USERS = getenv("5708609169")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ariyan104:ariyan104@cluster0.1iptuzv.mongodb.net/?retryWrites=true&w=majority")
API_ID = int(getenv("API_ID", "23842900"))
API_HASH = getenv("API_HASH", "d21e95895cf2a5b83b0167fdd3b6e541")
OWNER_ID = int(getenv("OWNER_ID", "5761513990"))
UPDATE = getenv("UPDATE", "NixaWorld")
SUPPORT = getenv("SUPPORT", "SankiWorldMF")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/808b95a6e24cd6f322092.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
CMD_MUSIC = list(getenv("CMD_MUSIC", "/ . !").split())
BG_IMG = getenv("BG_IMG", "https://telegra.ph/file/f2a2d31f60a9e0f3dbe94.png")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2056407064").split()))
ASSISTANT_NAME = getenv("ASSNAME", "SankiX")
COMMAND_PREFIXES = ("/ ! .").split()
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/a085a3cea21f994264152.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
