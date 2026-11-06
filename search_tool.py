
import os
from dotenv import load_dotenv
from tavily import TavilyClient

# Load environment variables from .env
load_dotenv()

# Get Tavily API key
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    raise ValueError(
        "TAVILY_API_KEY missing! Check your .env file."
    )

# Initialize Tavily client
tavily = TavilyClient(api_key=TAVILY_API_KEY)


def search_web(query):
    try:
        response = tavily.search(
            query=query,
            max_results=5,
            search_depth="basic"
        )

        results = []

        for item in response.get("results", []):
            results.append({
                "title": item.get("title", ""),
                "url": item.get("url", ""),
                "content": item.get("content", "")
            })

        return results

    except Exception as error:
        print(f"Tavily search error: {error}")
        return []
