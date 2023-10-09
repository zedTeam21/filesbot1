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

<details>
<summary><b>Admin Commands</b></summary>
  
- <code>/start</code>: Start the bot or get posts.
- <code>/batch</code>: Create a link for multiple posts.
- <code>/genlink</code>: Create a link for one post.
- <code>/users</code>: View bot statistics.
- <code>/broadcast</code>: Broadcast messages to bot users.
- <code>/stats</code>: Check the bot's uptime.

</details>

<details>
<summary><b>Configuration Variables</b></summary>

- <code>API_HASH</code>: Your API Hash from my.telegram.org.
- <code>APP_ID</code>: Your API ID from my.telegram.org.
- <code>TG_BOT_TOKEN</code>: Your bot token from @BotFather.
- <code>OWNER_ID</code>: Your Telegram ID.
- <code>CHANNEL_ID</code>: Your Channel ID (e.g., -100xxxxxxxx).
- <code>DATABASE_URL</code>: Your MongoDB URL.
- <code>DATABASE_NAME</code>: Your MongoDB session name.
- <code>ADMINS</code>: Optional list of user IDs for Admins (space-separated).
- <code>START_MESSAGE</code>: Optional: Customize the bot's start message using HTML and <a href="#start_message-fillings">fillings</a>.
- <code>FORCE_SUB_MESSAGE</code>: Optional: Customize the force-subscribe message using HTML.
- <code>FORCE_SUB_CHANNEL</code>: Optional: ForceSub Channel ID (leave as 0 to disable force-sub).
- <code>PROTECT_CONTENT</code>: Optional: True to prevent forwarding of files.

</details>

<details>
<summary><b>Customizable Messages and Text</b></summary>

- <code>CUSTOM_CAPTION</code>: Customize the caption text for documents using HTML and <a href="#custom_caption-fillings">fillings</a>.
- <code>DISABLE_CHANNEL_BUTTON</code>: Set to <code>True</code> to disable the channel share button (default is <code>False</code>).
- <code>BOT_STATS_TEXT</code>: Customize the text for the <code>/stats</code> command using HTML and <a href="#custom_stats-fillings">fillings</a>.
- <code>USER_REPLY_TEXT</code>: Customize the text to show when a user sends any message using HTML.

</details>

<details>
<summary><b>Fillings</b></summary>

### START_MESSAGE | FORCE_SUB_MESSAGE

- <code>{first}</code>: User's first name.
- <code>{last}</code>: User's last name.
- <code>{id}</code>: User's ID.
- <code>{mention}</code>: Mention the user.
- <code>{username}</code>: User's username.

### CUSTOM_CAPTION

- <code>{filename}</code>: File name of the document.
- <code>{previouscaption}</code>: Original caption.

### CUSTOM_STATS

- <code>{uptime}</code>: Bot's uptime.

</details>

If you encounter any bugs or have feature requests, please report them in our Telegram support group.

Credits
Thanks to Dan for his awesome Pyrogram library.
Thanks to our support group members for their valuable input and contributions.
License
GNU GPLv3 Image

File-Sharing-Bot is Free Software released under the terms of the GNU General Public License, version 3 or later.

If you found this repository helpful, consider giving it a star ⭐⭐⭐

