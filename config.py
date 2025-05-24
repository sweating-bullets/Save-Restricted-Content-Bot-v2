# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies"""

YTUB_COOKIES = """
# write here yt cookies"""

API_ID = int(getenv("API_ID","20870930"))
API_HASH = getenv("API_HASH","d8339c188abe7b852e52ef2d0d48c770")
BOT_TOKEN = getenv("BOT_TOKEN","7666467345:AAF_L7R5S1imG8MLpAix3Ige3mKug7a3ZuU")
OWNER_ID = list(map(int,getenv("OWNER_ID","1760032652").split()))
MONGO_DB = getenv("MONGO_DB","mongodb+srv://adilphatan001:osWpVi8W3UFewphF@cluster0.cplhbfu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP","-1002308118349")
CHANNEL_ID = int(getenv("CHANNEL_ID","-1002217595765"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "20"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000000000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
