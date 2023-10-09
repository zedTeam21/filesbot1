#(©)Codexbotz

from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

# Import necessary modules and variables from the 'config' module
from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, CHANNEL_ID, PORT

# Create a custom Bot class that inherits from the 'Client' class
class Bot(Client):
    def __init__(self):
        # Initialize the Bot class with various parameters
        super().__init__(
            name="Bot",  # Set the name of the bot
            api_hash=API_HASH,  # API hash for authentication
            api_id=APP_ID,  # API ID for authentication
            plugins={
                "root": "plugins"  # Specify the root directory for plugins
            },
            workers=TG_BOT_WORKERS,  # Number of worker threads
            bot_token=TG_BOT_TOKEN  # Telegram Bot API token
        )
        self.LOGGER = LOGGER  # Assign the LOGGER object from the config module to a class variable

    async def start(self):
        await super().start()  # Call the start method of the parent class (Client)
        usr_bot_me = await self.get_me()  # Get information about the bot user
        self.uptime = datetime.now()  # Record the bot's uptime

        # Check if FORCE_SUB_CHANNEL is enabled
        if FORCE_SUB_CHANNEL:
            try:
                # Get the invite link for the specified channel (FORCE_SUB_CHANNEL)
                link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)  # Export the invite link if it's missing
                    link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                self.invitelink = link  # Assign the invite link to a class variable
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/IAnimeHUB for support")
                sys.exit()  # Exit the script if there's an issue with FORCE_SUB_CHANNEL

        try:
            # Get information about the database channel (CHANNEL_ID)
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel  # Assign the database channel information to a class variable
            # Send a test message to the database channel and delete it immediately
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/iAnimeHub for support")
            sys.exit()  # Exit the script if there's an issue with CHANNEL_ID

        self.set_parse_mode(ParseMode.HTML)  # Set the parse mode to HTML for sending messages

        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/iAnimeHub")
        self.LOGGER(__name__).info(f""" \n\n       

██╗░█████╗░███╗░░██╗██╗███╗░░░███╗███████╗██╗░░██╗██╗░░░██╗██████╗░
██║██╔══██╗████╗░██║██║████╗░████║██╔════╝██║░░██║██║░░░██║██╔══██╗
██║███████║██╔██╗██║██║██╔████╔██║█████╗░░███████║██║░░░██║██████╦╝
██║██╔══██║██║╚████║██║██║╚██╔╝██║██╔══╝░░██╔══██║██║░░░██║██╔══██╗
██║██║░░██║██║░╚███║██║██║░╚═╝░██║███████╗██║░░██║╚██████╔╝██████╦╝
╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝░╚═════╝░╚═════╝░
                                          """)
        self.username = usr_bot_me.username
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
