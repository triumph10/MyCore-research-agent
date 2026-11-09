
import os
from datetime import date
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")


def generate_report(topic, sources):
    research_date = date.today().isoformat()

    # Select the 8 most relevant sources
    selected_sources = sorted(
        sources,
        key=lambda x: x.get("score", 0),
        reverse=True
    )[:8]

    source_context = ""

    for source in selected_sources:
        source_id = source.get("source_id", "S?")
        title = source.get("title", "Untitled")
        url = source.get("url", "")
        published = source.get(
            "published_date", "Date not provided"
        )

        content = (
            source.get("raw_content")
            or source.get("content")
            or "No content available"
        )

        # Strictly limit the amount of text sent to Groq
        content = content[:900]

        source_context += f"""
[{source_id}]
Title: {title}
URL: {url}
Publication date: {published}
Content: {content}

"""

    prompt = f"""
Research topic: {topic}
Research conducted on: {research_date}

Write a professional research report in Markdown.

Sections:
1. Executive Summary
2. Introduction
3. Latest Developments
4. Key Findings
5. Strategy and Future Plans
6. Opportunities
7. Risks and Challenges
8. Conclusion
9. References

Rules:
- Cite factual claims using [S1], [S2], etc.
- Only use the supplied sources.
- Do not invent facts, dates or financial figures.
- Distinguish confirmed facts from predictions.
- Mention when publication dates are unavailable.
- Explain disagreements between sources.
- Include source URLs in References.
- State when evidence is insufficient.

Research sources:

{source_context}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a careful, evidence-based research analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_completion_tokens=1500
    )

    return response.choices[0].message.content
