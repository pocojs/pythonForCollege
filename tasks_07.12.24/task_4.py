import asyncio
import random

async def process_task(queue):
    while True:
        task = await queue.get()
        print(f"Обрабатываю: {task}")
        await asyncio.sleep(random.randint(1, 2))
        queue.task_done()
        if queue.empty():
            break

async def main():
    queue = asyncio.Queue()
    tasks = ["Задача 1", "Задача 2", "Задача 3", "Задача 4", "Задача 5"]
    for task in tasks:
        await queue.put(task)
    await asyncio.gather(process_task(queue), process_task(queue))

asyncio.run(main())

