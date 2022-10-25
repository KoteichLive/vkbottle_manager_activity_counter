import vkbottle
from cd.conf import p, user
from cd.verarbeitung import reg, ceh, bal_minus, cec_start_bal, cac_startcurs_bal, bal_sms_plus
import asyncio
from vkbottle.bot import Bot, Message
from cd.alg import *
from vkbottle import API, BotBlueprint
from loguru import logger
logger.disable("vkbottle")


glmenu = BotBlueprint()

us=[]


@glmenu.on.message(text="1")
async def hi_handler(message: Message):
    await usi_post()
    

async def post_user(t):
    api = API(user)
    await api.wall.post(message=t)

#@bot.on.message()
#async def hi_handler(message: Message):
#    users_info = await bot.api.users.get(message.from_id)
#    await message.answer("Привет, {}".format(users_info[0].first_name))
woz=0
cat=0

async def usi_post():
    global woz, cat
    await asyncio.sleep(3600)
    stT = cec_start_bal()
    curs =cac_startcurs_bal()
    await post_user(f'''
Всем привет народ
статистика проекта каждый час:
сообщений в чате за последний час: {cat}
вознаграждений получено в час: {woz}
при регистрации: {stT}: БАлда
курс {curs} = 1руб
всего зарегистрировано пользователей: (?)
промокодов создано всего: (?)
сообщений сегодня
''')
    woz = 0
    cat = 0
    await usi_post()

print(1)

@glmenu.on.message(text=['промо', 'Промо', 'промо <pro:int>', 'Промо <pro:int>', 'промо <prot>', 'Промо <prot>'], blocking=False)
async def mein(message:Message, pro, prot):
    if pro==None or prot==None:
        pass
    else:
        pass


@glmenu.on.message()
async def mein(message:Message):
    global woz, cat
    sta = await ceh(message.from_id)
    print(sta)
    #if sta ==None:
        #await reg(message.from_id)
    #else:
        #await bal_sms_plus(message.from_id, 102)



