import asyncio

async def async_timer(array):
    for i in sorted(array):
        await asyncio.sleep(i)
        print(f"Прошло {i} секунд")

async def main():
    await async_timer([1, 3, 2])

asyncio.run(main())
