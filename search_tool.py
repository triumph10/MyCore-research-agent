"""Searches the internet."""


def search_internet(topic: str) -> list[str]:
    return [f"Placeholder result for: {topic}"]
from tavily import TavilyClient

# Initialize search client
tavily = TavilyClient()


def search_web(query):
    response = tavily.search(
        query=query,
        max_results=5
    )

    results = []

    for item in response["results"]:
        results.append({
            "title": item.get("title", ""),
            "url": item.get("url", ""),
            "content": item.get("content", "")
        })

    return results