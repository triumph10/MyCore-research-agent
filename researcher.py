
import os
from datetime import date
from groq import Groq
from dotenv import load_dotenv
from search_tool import search_web

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")


def create_research_plan(topic):
    today = date.today().isoformat()

    prompt = f"""
    You are an expert research planner.

    Today's date: {today}
    Research topic: {topic}

    Create exactly 4 distinct web search queries:
    1. Latest developments and announcements.
    2. Official company statements or documents.
    3. Plans, goals, financial outlook and strategy.
    4. Historical background and important context.

    Return only the queries, one per line.
    Do not number them.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    answer = response.choices[0].message.content or ""

    queries = [
        line.strip().lstrip("-*0123456789. ")
        for line in answer.splitlines()
        if line.strip()
    ]

    if not queries:
        return [
            f"{topic} latest announcements {today}",
            f"{topic} official statements and reports",
            f"{topic} plans strategy and future goals",
            f"{topic} background and history"
        ]

    return queries[:4]


def run_research(topic):
    queries = create_research_plan(topic)

    all_results = []
    seen_urls = set()

    for query in queries:
        print(f"\nSearching: {query}")

        try:
            results = search_web(query)

            for item in results:
                url = item.get("url", "").strip()

                if url and url not in seen_urls:
                    seen_urls.add(url)
                    all_results.append(item)

        except Exception as error:
            print(f"Search failed: {error}")

    # Assign reference numbers for report citations
    for index, item in enumerate(all_results, start=1):
        item["source_id"] = f"S{index}"

    return all_results
