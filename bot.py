from asyncio import sleep
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import *
from utils import *
from db_worker import Worker
from gen_captcha import ICaptcha


db = Worker()
capt4a = ICaptcha()
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=['new_chat_members'])
async def new_user(message: types.Message):
    chat = message.chat
    user_id = message.new_chat_members[0].id
    full_name = message.new_chat_members[0].full_name
    lang = message.new_chat_members[0].language_code

    who_am_i = await bot.get_me()
    bot_status = await bot.get_chat_member(chat.id, who_am_i.id)
    keyboard = InlineKeyboardMarkup()
    keyword, captcha_list, captcha_name = await capt4a.getcaptcha()

    if who_am_i.id == user_id:
        await bot.send_message(chat.id, hm)
    elif bot_status['status'] == 'administrator':
        db.save_user(user_id, str(chat.id), captcha_name, full_name)
        if lang not in languages:
            lang = 'en'

        for i in captcha_list:
            if i == keyword:
                keyboard.add(InlineKeyboardButton(i, callback_data='true'))
            else:
                keyboard.add(InlineKeyboardButton(i, callback_data='false'))

        await message.chat.restrict(
            user_id,
            permissions=types.ChatPermissions(
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_other_messages=False,
                can_invite_users=False,
                can_send_polls=False,
                can_add_web_page_previews=False,
                can_change_info=False,
                can_pin_messages=False
            ))
        msg = await bot.send_photo(
            chat.id, photo=open(captcha_name, 'rb'),
            caption=vocabulary[lang]['hello'].format(full_name, chat.title),
            reply_markup=keyboard
        )

        await sleep(30)
        try:
            await bot.delete_message(chat_id=chat.id, message_id=int(msg.message_id))
        except:
            pass

        for inst in db.get_users():
            if str(user_id) == inst[1] and str(chat.id) == inst[2] and inst[4] in msg.caption:
                await cleaner(user_id, str(chat.id), inst[3])
    else:
        if lang not in languages:
            lang = 'en'
        await bot.send_message(chat.id, vocabulary[lang]['role'])


@dp.callback_query_handler(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    cq_user_id = str(callback_query.from_user.id)
    cq_user_full_name = callback_query.from_user.full_name
    cq_chat_id = str(callback_query.message.chat.id)
    cq_msg_caption = str(callback_query.message.caption)
    cq_lang = callback_query.from_user.language_code

    if cq_lang not in languages:
        cq_lang = 'en'

    for obj in db.get_users():
        if cq_user_id == obj[1] and cq_chat_id == obj[2] and obj[4] in cq_msg_caption:
            if callback_query.data != 'true':

                await callback_query.answer((vocabulary[cq_lang]['ban'].format(cq_user_full_name)), show_alert=True)
                await callback_query.message.chat.kick(
                    int(cq_user_id),
                    until_date=int(callback_query.message.date.timestamp() + ban * 3600)
                )
                await cleaner(cq_user_id, cq_chat_id, obj[3])
                try:
                    await callback_query.message.delete()

                except:
                    pass
            else:
                await callback_query.answer((vocabulary[cq_lang]['success']), show_alert=True)
                try:
                    await callback_query.message.delete()
                except:
                    pass

                await callback_query.message.chat.restrict(
                    int(cq_user_id),
                    permissions=types.ChatPermissions(can_send_messages=True,
                                                      can_send_media_messages=True,
                                                      can_send_other_messages=True,
                                                      can_invite_users=True,
                                                      can_send_polls=True,
                                                      can_add_web_page_previews=True,
                                                      can_change_info=True,
                                                      can_pin_messages=True)
                )
                await cleaner(cq_user_id, cq_chat_id, obj[3])
    else:
        await callback_query.answer((vocabulary[cq_lang]['other']), show_alert=True)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
