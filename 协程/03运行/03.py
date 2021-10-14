import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*: return_exceptions 为 True，异常会和成功的结果一样处理，并聚合至结果列表。
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
        
    )
    print(L)

# 取消屏蔽操作
# asyncio.shield() 如果这个协程要被取消 但是他不会被取消的 虽然调用已经取消了 可以和超时 结合起来
asyncio.run(main())