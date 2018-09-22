import asyncio
import time



now = lambda :time.time()

async def do_some_work(x):
    print("waiting:",x)
    # await 后面就是调用耗时的操作
    await asyncio.sleep(x)
    return "Done after {}s".format(x)


start = now()

coroutine = do_some_work(2)

coroutine2 = do_some_work(3)

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)

task2 = asyncio.ensure_future(coroutine2)
loop.run_until_complete(task)
print("Task1 ret:", task.result())

loop.run_until_complete(task2)
print("Task2 ret:", task2.result())

print("Time:", now() - start)