




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "25354498"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1cdcf1a33fc5108fa3ca151480eece50")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001963688423"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1969177696"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://gs0478717:X3R9cW7hVv9YjDyS@cluster0.2utnbxv.mongodb.net/")
DB_NAME = os.environ.get("DATABASE_NAME", "FILESBOT")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001882327590"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "👋 Hello {first}! Welcome to the Anime Bot! \n\n🌟I'm here to help you watch any anime you desire. Join our main channel @iAnimeHub for more! 📺🌸.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join my Channel in order to use me\n\nKindly join @iAnimeHub and it\'s private channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Hello there! \n\nPlease do not send me any direct message as I can only send you files once you click on any link.\n\nJoin @iAnimeHub for more anime fun! 🌟🌸 Explore a wide variety of shows and connect with fellow enthusiasts. "

ADMINS.append(OWNER_ID)
ADMINS.append(1969177696)
ADMINS.append(163343128)

# Define the name of the log file
LOG_FILE_NAME = 'my_log.log'

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO (you can adjust this level as needed)
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",  # Define the log message format
    datefmt='%d-%b-%y %H:%M:%S',  # Define the date and time format for log messages
    handlers=[
        # Create a rotating file handler that limits the log file size to 50 MB and keeps up to 10 backup files
        logging.handlers.RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,  # Maximum log file size in bytes (50 MB)
            backupCount=10  # Number of backup log files to keep
        ),
        # Create a stream handler to also display log messages in the console
        logging.StreamHandler()  # Logs will be shown in the console
    ]
)

# Set the logging level for the 'pyrogram' logger to WARNING (suppress less severe log messages)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Define a function to create custom loggers with a given name
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
