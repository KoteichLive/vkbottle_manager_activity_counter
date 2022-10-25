import aiosqlite3
import datetime
import os
import requests
from bs4 import BeautifulSoup

def promoceh(promo):
    r = requests.get(f'http://127.0.0.1:8000/promo/vk/{promo}')

def promsuma(promo):
    pass


async def log(id_from, text_content, tip):
    async with aiosqlite3.connect('db.db') as db:
        dt_now = datetime.datetime.now()
        await db.execute("INSERT INTO logg (id_from, data, content, types,) values (?, ?, ?, ?)",(id_from, dt_now, text_content, tip,))
        await db.commit()

async def data_hiso():
    dt_now = datetime.datetime.now()
    dt_no = str(dt_now)
    #2020-11-14 15:43:32.249588
    dh= f'{dt_no[6]}{dt_no[7]}'
    return dh


def cec_start_bal():
    with open('startuser.txt', encoding="utf-8") as f:
        data = f.read()
        return data

def cac_startcurs_bal():
    with open('curs.txt.txt', encoding="utf-8") as f:
        return f

def set_sms_h():
    pass

async def reg(id_from):
    async with aiosqlite3.connect('db.db') as db:
        startbal=cec_start_bal()
        #await cur.execute("SELECT ")
        dt_now = datetime.datetime.now()
        await db.execute("INSERT INTO users (from_id, bal) values (?, ?, ?)",(id_from, startbal))
        await db.commit()
        await log(id_from, 'регистрация', 'регистрация')

async def ceh(idd):
    async with aiosqlite3.connect('db.db') as db:
        cursor = await db.execute("SELECT * FROM user WHERE from_id = (?)", (idd,))
        rows = await cursor.fetchall()
        print(rows)
        if len(rows) == 0:
            await reg(idd)
            print('регистрация')
        else:
            print(ЕСТЬ)
            id_from= rows[0][1]
            balans =rows[0][2]
            data =rows[0][3]
            meta_sms =rows[0][4]
            delitel =rows[0][5]
            vip_name =rows[0][6]
            tarif_id =rows[0][7]
            return balans, data, meta_sms, delitel, vip_name, tarif_id

async def bal_minus(i):
    pass

async def ceh_tarif_name():
    async with aiosqlite3.connect("db.db") as db:
        cursor = await db.execute("SELECT * FROM user WHERE from_id = (?)", (idd,))
        rows = await cursor.fetchall()

async def ceh_tarif_id():
    async with aiosqlite3.connect("db.db") as db:
        cursor = await db.execute("SELECT * FROM user WHERE from_id = (?)", (idd,))
        rows = await cursor.fetchall()


async def bal_sms_plus(id_sms, suma):
    async with aiosqlite3.connect("db.db") as db:
        await db.execute("UPDATE user SET bal+bal=(?) WHERE from_id=(?)", (suma, id_sms,))
        await db.commit()

async def textob():
    pass