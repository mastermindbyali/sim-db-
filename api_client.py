import httpx
from config import API_BASE_URL, API_KEY

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

async def search_record(query: str):
    """
    Apni authorized API ke according endpoint/path/params change kar lo.
    Example endpoint:
    POST {API_BASE_URL}/search
    body: {"query": "..."}
    """

    url = f"{API_BASE_URL.rstrip('/')}/search"

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(url, headers=HEADERS, json={"query": query})
        response.raise_for_status()
        return response.json()
