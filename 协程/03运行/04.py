import asyncio

async def eternity():
    # Sleep for one hour
    await asyncio.sleep(10)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        #超时就是会被取消的 并且会报错
        await asyncio.wait_for(eternity(), timeout=1.0)
        # await asyncio.shield(eternity())
    except asyncio.TimeoutError:
        print('timeout!')
    
\
asyncio.run(main())