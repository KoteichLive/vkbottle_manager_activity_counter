from typing import Union
from fastapi import FastAPI
import sqlite3, random
import random, string

app = FastAPI()

def ceh_promo(promo):
    with sqlite3.connect('db.db') as db:
        cursor = db.execute("SELECT promotext FROM promo WHERE promotext = (?)", (promo,))
        cursor.fetchall()

        if len(rows) == 0:
            return False
        else:
            return True

def randomword_vk():
   letters = string.ascii_lowercase
   return 'Koteich_live-vk'.join(random.choice(letters) for i in range(6))

def ran():
	pass


count = 1  # фиксируем начальное значение
while count <= 10:  # и конечное (включительно)
    print(count, end=' ')
    count += 1

@app.get("/promo/vk/ceh/{type}")
async def read_item(item_id): #активировать
	pass

@app.get("/promo/vk{suma}")
async def read_item(suma):#создать промокод
	tuo=ceh_promo(promo)
	if tuo==True:
	    while tuo == False:
	    	 ceh_promo(promo)


    return {item_id}
