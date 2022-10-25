import asyncio
import aiosqlite3

async def awto_minus_bal(id_from, su):
    async with aiosqlite3.connect('db.db') as conn:
        async with conn.cursor() as cur:
            pass