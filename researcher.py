from groq import Groq
from dotenv import load_dotenv
import os
from search_tool import search_web
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "openai/gpt-oss-120b"


def create_research_plan(topic):
    prompt = f"""
    You are a research planner.

    Create 3 useful web search queries for this topic:
    {topic}

    Return one query per line.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    answer = response.choices[0].message.content
    return answer.strip().split("\n")


def run_research(topic):

    queries = create_research_plan(topic)

    all_results = []

    for query in queries:

        print("Searching:", query)

        results = search_web(query.strip())

        all_results.extend(results)

    return all_results