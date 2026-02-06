import asyncio
import time

async def task(name, delay):
    print(f"Start task {name}")
    await asyncio.sleep(delay)   # NON-BLOCKING
    print(f"End task {name}")

async def main():
    start = time.time()

    await asyncio.gather(
        task("A", 2),
        task("B", 2),
        task("C", 2),
    )

    end = time.time()
    print(f"Total time: {end - start:.2f} seconds")

asyncio.run(main())



# import time

# def task(name, delay):
#     print(f"Start task {name}")
#     time.sleep(delay)   # BLOCKING
#     print(f"End task {name}")

# start = time.time()

# task("A", 2)
# task("B", 2)
# task("C", 2)

# end = time.time()
# print(f"Total time: {end - start:.2f} seconds")

