# 有点伪代码的意思
import asyncio

# 协程函数: 定义形式为 async def 的函数;
# 协程对象: 调用 协程函数 所返回的对象。
async def nested():
    return 1024

async def main():
    #这里的future还是没有搞懂
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )
asyncio.run(main())