
import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    raise ValueError("TAVILY_API_KEY missing from .env")

tavily = TavilyClient(api_key=api_key)


def search_web(query):
    response = tavily.search(
        query=query,
        search_depth="basic",
        max_results=3,
        include_raw_content="markdown"
    )

    results = []

    for item in response.get("results", []):
        results.append({
            "title": item.get("title", ""),
            "url": item.get("url", ""),
            "content": item.get("content", ""),
            "raw_content": item.get("raw_content", ""),
            "published_date": (
                item.get("published_date")
                or item.get("publishedDate")
                or "Date not provided"
            ),
            "score": item.get("score", 0)
        })

    return results
