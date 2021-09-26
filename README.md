# Captcha Telegram Bot
Telegram bot ([@captcha_moderator_bot](https://t.me/captcha_moderator_bot)) that validates new users that enter supergroup. Validation works like a simple captcha.<br>
![alt tag](https://github.com/iterweb/captcha_telegram_bot/blob/master/captcha_img/photo_2021-47.jpg "Captcha Telegram Bot")​

## Install requirements
`pip install aiogram`<br>
`pip install pillow`

## How it works
1. Add the bot to your supergroup<br>
2. Promote the bot for administrator privileges<br>
3. A new user enters your supergroup<br>
4. Bot restricts the user's ability to send messages<br>
5. Bot shows a welcome message (the bot will automatically detect the user's language) and a captcha button to the user<br>
6. If the user doesn't press the button within 30 seconds then the user is banned by the bot

## Configuration
In the `config.py` file you need to specify `BOT_TOKEN`

## Donate
If you want, you can [support](https://destream.net/live/iterweb/donate) me!
