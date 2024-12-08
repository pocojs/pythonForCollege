import asyncio

async def progress_tracker(n):
    for i in range(1, n):
        await asyncio.sleep(0.5)
        print(f"Выполнено {i * (100 // n)}%...")
    print("Выполнено 100%!")

asyncio.run(progress_tracker(10))
