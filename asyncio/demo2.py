import asyncio
import time


now = lambda: time.time()


async def do_some_work(x):
    print("waiting:", x)

start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = loop.create_task(coroutine)
print(task)
loop.run_until_complete(task)
print(task)
print("Time:",now()-start)