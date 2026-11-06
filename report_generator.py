
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "openai/gpt-oss-120b"


def generate_report(topic, sources):
    research_data = str(sources)

    prompt = f"""
    You are an expert research analyst.

    Research topic: {topic}

    Research sources:
    {research_data}

    Create a detailed report containing:

    1. Executive summary
    2. Introduction
    3. Key findings
    4. Benefits
    5. Challenges
    6. Future opportunities
    7. Conclusion
    8. References

    Use source URLs in your references.
    Do not invent facts.
    Clearly distinguish facts from predictions.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    answer = response.choices[0].message.content
    return answer
