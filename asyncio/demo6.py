import asyncio
from aiohttp import ClientSession

async def wget(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            print("{0} start!".format(url))
            # await asyncio.sleep(1)
            response = await response.text()
            print("{0} finish!".format(url))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(wget(host)) for host in ['http://www.sina.com.cn', 'http://www.sohu.com', 'http://www.163.com', 'http://ljwancaiji.com:9002']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()