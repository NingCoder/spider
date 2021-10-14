import asyncio
#无法实现并发操作
async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world")

asyncio.run(main())