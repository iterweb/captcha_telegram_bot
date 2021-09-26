import os

from db_worker import Worker


db = Worker()


async def cleaner(user, chat, img):
    try:
        db.delete_users(user, chat)
        os.remove(img)
    except:
        pass
