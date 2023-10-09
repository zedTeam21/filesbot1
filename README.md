# File-Sharing-Bot

<p align="center">
  <a href="https://www.python.org">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" width="250">
  </a>
  <a href="https://t.me/CodeXBotz">
    <img src="https://github.com/CodeXBotz/PyrogramGenStr/blob/main/resources/madebycodex-badge.svg" width="250">
  </a><br>
  <a href="https://t.me/CodeXBotz">
    &nbsp;<img src="https://img.shields.io/badge/Code%20%F0%9D%95%8F%20Botz-Channel-blue?style=flat-square&logo=telegram" width="130" height="18">&nbsp;
  </a>
  <a href="https://t.me/codexbotzsupport">
    &nbsp;<img src="https://img.shields.io/badge/Code%20%F0%9D%95%8F%20Botz-Group-blue?style=flat-square&logo=telegram" width="130" height="18">&nbsp;
  </a>
  <br>
  <a href="https://github.com/CodeXBotz/File-Sharing-Bot/stargazers">
    <img src="https://img.shields.io/github/stars/CodeXBotz/File-Sharing-Bot?style=social">
  </a>
  <a href="https://github.com/CodeXBotz/File-Sharing-Bot/fork">
    <img src="https://img.shields.io/github/forks/CodeXBotz/File-Sharing-Bot?label=Fork&style=social">
  </a>
</p>

Telegram Bot for storing posts and documents, accessible via special links. This bot can be a valuable tool for various use cases.

## Features
- Highly customizable.
- Customizable welcome and force-subscription messages.
- Support for multiple posts within a single link.
- Can be easily deployed on Heroku.

## Setup

To set up the bot:

1. Add the bot to a Database Channel with all necessary permissions.
2. Add the bot to a ForceSub channel as an admin with the "Invite Users via Link" permission if you enable ForceSub.

## Installation

### Deploy on Heroku
Before deploying on Heroku, make sure to fork this repository and change its name.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

For detailed deployment instructions, watch this [tutorial video](https://youtu.be/LCrkRTMkmzE) on YouTube.

### Deploy on Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/1jKLr4)

### Deploy on Koyeb

The fastest way to deploy the application is by clicking the **Deploy to Koyeb** button below.

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/CodeXBotz/File-Sharing-Bot&branch=koyeb&name=filesharingbot)

### Deploy on Your VPS
bash
git clone https://github.com/CodeXBotz/File-Sharing-Bot
cd File-Sharing-Bot
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py

Admin Commands
/start: Start the bot or get posts.
/batch: Create a link for multiple posts.
/genlink: Create a link for one post.
/users: View bot statistics.
/broadcast: Broadcast messages to bot users.
/stats: Check the bot's uptime.
Configuration Variables
API_HASH: Your API Hash from my.telegram.org.
APP_ID: Your API ID from my.telegram.org.
TG_BOT_TOKEN: Your bot token from @BotFather.
OWNER_ID: Your Telegram ID.
CHANNEL_ID: Your Channel ID (e.g., -100xxxxxxxx).
DATABASE_URL: Your MongoDB URL.
DATABASE_NAME: Your MongoDB session name.
ADMINS: Optional list of user IDs for Admins (space-separated).
START_MESSAGE: Optional: Customize the bot's start message using HTML and fillings.
FORCE_SUB_MESSAGE: Optional: Customize the force-subscribe message using HTML.
FORCE_SUB_CHANNEL: Optional: ForceSub Channel ID (leave as 0 to disable force-sub).
PROTECT_CONTENT: Optional: True to prevent forwarding of files.
Customizable Messages and Text
CUSTOM_CAPTION: Customize the caption text for documents using HTML and fillings.
DISABLE_CHANNEL_BUTTON: Set to True to disable the channel share button (default is False).
BOT_STATS_TEXT: Customize the text for the /stats command using HTML and fillings.
USER_REPLY_TEXT: Customize the text to show when a user sends any message using HTML.
Fillings
START_MESSAGE | FORCE_SUB_MESSAGE
{first}: User's first name.
{last}: User's last name.
{id}: User's ID.
{mention}: Mention the user.
{username}: User's username.
CUSTOM_CAPTION
{filename}: File name of the document.
{previouscaption}: Original caption.
CUSTOM_STATS
{uptime}: Bot's uptime.
Support
Join our Telegram Group for support and assistance, and visit our Channel for updates and announcements.

If you encounter any bugs or have feature requests, please report them in our Telegram support group.

Credits
Thanks to Dan for his awesome Pyrogram library.
Thanks to our support group members for their valuable input and contributions.
License
GNU GPLv3 Image

File-Sharing-Bot is Free Software released under the terms of the GNU General Public License, version 3 or later.

If you found this repository helpful, consider giving it a star ⭐⭐⭐

