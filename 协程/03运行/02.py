import asyncio
import datetime
#sleep是关于休眠的
async def display_date():
    # 返回当前 OS 线程中正在运行的事件循环。
    # 如果没有正在运行的事件循环则会引发 RuntimeError。 此函数只能由协程或回调来调用。
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1) #sleep() 总是会挂起当前任务，以允许其他任务运行。

asyncio.run(display_date())