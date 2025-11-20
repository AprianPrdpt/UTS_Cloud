import asyncio
import httpx
import time

URL = "https://jsonplaceholder.typicode.com/todos/1"

async def fetch(client):
    r = await client.get(URL)
    return r.json()

async def main():
    start = time.time()
    
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client) for _ in range(20)]
        await asyncio.gather(*tasks)

    end = time.time()
    print("AsyncIO time:", end - start)

if __name__ == "__main__":
    asyncio.run(main())
