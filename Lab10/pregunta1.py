import asyncio
import httpx

urls = ["https://www.amazon.com", "https://www.nvidia.com/en-us/", "https://www.openai.com",
        "https://www.python.org", "https://www.microsoft.com/en-us/", "https://www.google.com",
        "https://www.wikipedia.com", "https://x.com/"]

async def async_fetch(url: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.text 

def sync_fetch(url:str) -> str:
    with httpx.Client() as client:
        response = client.get(url)
    return response.text

if __name__=="__main__":
    # Version sincrona
    print(sync_fetch(urls[0]))

    # Version asincrona
    print(asyncio.run(async_fetch(urls[0])))
