import asyncio
import time

async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished after {delay}s")

async def main():
    start = time.time()

    # Run three tasks concurrently
    await asyncio.gather(
        task("Task A", 2),
        task("Task B", 1),
        task("Task C", 3)
    )

    end = time.time()
    print(f"All done in {end - start:.2f} seconds")

# Run the event loop
asyncio.run(main())