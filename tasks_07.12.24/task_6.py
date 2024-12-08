import asyncio
import random


async def producer(queue, producer_id):
    for i in range(10):
        data = random.randint(1, 10)
        await queue.put((data, producer_id))
        print(f"Производитель {producer_id}: сгенерировал {data}")
        await asyncio.sleep(1)


async def worker(in_queue, out_queue):
    while True:
        data, producer_id = await in_queue.get()
        result = data * 2
        await out_queue.put((result, producer_id))
        print(f"Работник: обработал {data} -> {result}")
        await asyncio.sleep(1.5)
        in_queue.task_done()


async def storage(out_queue):
    results = []
    while True:
        if out_queue.empty():
            await asyncio.sleep(0.5)
            continue
        result, producer_id = await out_queue.get()
        results.append(result)
        out_queue.task_done()
        print(f"Сохранено: {results}")
        await asyncio.sleep(2)


async def main():
    in_queue = asyncio.Queue()
    out_queue = asyncio.Queue()

    producers = [asyncio.create_task(producer(in_queue, i)) for i in range(1, 4)]
    workers = [asyncio.create_task(worker(in_queue, out_queue)) for k in range(2)]
    storage_task = asyncio.create_task(storage(out_queue))

    await asyncio.gather(*producers, *workers, storage_task)
    await in_queue.join()
    await out_queue.join()


asyncio.run(main())