import asyncio

async def add_customers(queue):
    for i in range(1, 11):
        customer = f"Покупатель {i}"
        await queue.put(customer)
        print(f"Добавлен в очередь: {customer}")
        await asyncio.sleep(1)

async def serve_customers(queue):
    while not queue.empty():
        customer = await queue.get()
        print(f"Обслуживаю: {customer}")
        await asyncio.sleep(2)
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(
        add_customers(queue),
        serve_customers(queue)
    )
    await queue.join()

if __name__ == "__main__":
    asyncio.run(main())
