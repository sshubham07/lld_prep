import asyncio
async def run(task):
    print(f"Starting {task}...")
    await asyncio.sleep(2)
    print(f"Ending {task}.")

async def main():
    await asyncio.gather(run(1),run(2))

asyncio.run(main())