BOT_TOKEN = ''

# time for which the user will be banned (in hours)
ban = 24


captcha_words = [
    ['water', 'public', 'business', 'achieve'],
    ['slowly', 'golden', 'accident', 'hungry'],
    ['upon', 'effect', 'smart', 'talent'],
    ['debate', 'weigh', 'yield', 'dance'],
    ['table', 'carrier', 'danger', 'century'],
    ['yellow', 'young', 'global', 'public']
]


languages = ['ru', 'en', 'uk', 'de', 'pl', 'tr', 'ko']
vocabulary = {
    'ru': {
        'hello': 'Привет, {}! Добро пожаловать в чат, {}!\nЕсли ты не робот, ответь на капчу!\nУ тебя 30 секунд!',
        'ban': 'Ты ошибся..!\n{}, ты можешь попробовать снава, через 24 часа!',
        'success': 'Поздравляю!\nДобро пожаловать в чат!',
        'other': 'Это сообщение, предназначено не тебе!',
        'role': 'Установите права администратора для бота'
    },
    'en': {
        'hello': 'Hi, {}! Welcome to the chat {}!\nPlease solve this captcha!\nYou have 30 seconds!',
        'ban': 'You wrong..!\n{}, you can try again in 24 hours!',
        'success': 'Congratulations!\nWelcome to the chat!',
        'other': 'This is message not for you!',
        'role': 'Set administrator rights for the bot'
    },
    'uk': {
        'hello': 'Привіт, {}! Ласкаво просимо до чату, {}!\nЯк що, ти не робот, дай відповідь на цю капчу!\n'
                 'У тебе є 30 секунд!',
        'ban': 'Ти помилився..!\n{}, ти зможеш повторити спробу через 24 години!',
        'success': 'Вітаю!\nЗапрошуємо до чату!',
        'other': 'Думаю, це повідомлення не для тебе!',
        'role': 'Встановіть права адміністратора для бота'
    },
    'de': {
        'hello': 'Hi, {}! Willkommen im Chat, {}!\nBitte lösen Sie dieses Captcha!\n'
                 'Sie haben 30 Sekunden Zeit!',
        'ban': 'Du hast Unrecht..!\n{}, du kannst es in 24 Stunden noch einmal versuchen!',
        'success': 'Herzlichen Glückwunsch!\nWillkommen im Chat!',
        'other': 'Ich glaube, es ist nichts für dich!',
        'role': 'Administratorrechte für den Bot festlegen'
    },
    'pl': {
        'hello': 'Cześć, {}! Witamy na czacie, {}!\nProszę rozwiązać ten captcha!\nMasz 30 sekund!',
        'ban': 'Mylisz się..!\n{}, możesz spróbować ponownie za 24 godziny!',
        'success': 'Gratulacje!\nWitamy na czacie!',
        'other': 'Myślę, że to nie dla ciebie!',
        'role': 'Ustaw uprawnienia administratora dla bota'
    },
    'tr': {
        'hello': "Selam, {}! Sohbete hoş geldiniz, {}!\nLütfen bu captcha'yı çözün!\n30 saniyeniz var!",
        'ban': 'Yanılıyorsun..!\n{}, 24 saat sonra tekrar deneyebilirsin!',
        'success': 'Tebrikler!\nSohbete hoş geldiniz!',
        'other': 'Sanırım senin için değil!',
        'role': 'Bot için yönetici haklarını ayarlayın'
    },
    'ko': {
        'hello': "안녕하세요 {}! 채팅에 오신 것을 환영합니다 {}!\n이 보안 문자를 해결하십시오!\n30초의 시간이 있습니다!",
        'ban': '틀렸습니다..!\n{}, 24시간 후에 다시 시도할 수 있습니다!',
        'success': '축하합니다!\n채팅에 오신 것을 환영합니다!',
        'other': '너를 위한 건 아닌 것 같아!',
        'role': '봇에 대한 관리자 권한 설정'
    }
}

hm = '👋\nOpen Source Bot\nhttps://github.com/iterweb/captcha_telegram_bot'