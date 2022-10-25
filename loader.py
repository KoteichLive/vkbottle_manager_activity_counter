from vkbottle import Bot
from cd.conf import p, user
from main import glmenu

bot = Bot(p)

#приложения
#user
glmenu.load(bot)