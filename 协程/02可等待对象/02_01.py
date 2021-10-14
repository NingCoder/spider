# 可等待 对象有三种主要类型: 协程, 任务 和 Future.
import asyncio

# 协程函数: 定义形式为 async def 的函数;
# 协程对象: 调用 协程函数 所返回的对象。
async def nested():
    return 1024

async def main():
    # 作为任务 来调用 task 
    task=asyncio.create_task(nested())
    print(await task)

asyncio.run(main())