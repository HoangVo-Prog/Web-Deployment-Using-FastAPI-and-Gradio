import time
import sys
import asyncio

def fetch_data_sync():
    print("Hi")
    time.sleep(3)
    print("Bye")

def non_concurrent_execution():
    start_time = time.perf_counter()  # Start the timer

    # Execute tasks sequentially
    for _ in range(2):
        fetch_data_sync()

    end_time = time.perf_counter()  # End the timer
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

async def fetch_data_async():
    print("Hi")
    await asyncio.sleep(3)
    print("Bye")

async def main():
    start_time = time.perf_counter()  # Start the timer

    # Create a list of tasks
    tasks = [fetch_data_async() for _ in range(2)]

    # Run tasks concurrently
    await asyncio.gather(*tasks)

    end_time = time.perf_counter()  # End the timer
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <mode>")
        print("Mode 1: Sequential execution")
        print("Other: Concurrent execution")
        sys.exit(1)

    if sys.argv[1] == "1":
        non_concurrent_execution()
    else:
        asyncio.run(main())
