# MyCore Research Agent

An automated AI-powered research assistant built with Python. It takes a research topic, creates targeted search queries, gathers up-to-date information using Tavily, and uses Groq to generate a structured research report saved as a Markdown file.

## Project Structure

```text
triumph10-mycore-research-agent/
├── README.md
├── main.py
├── researcher.py
├── search_tool.py
├── report_generator.py
├── requirements.txt
├── .env
└── reports/
    └── .gitkeep
```

## Features

- **Automated Research Planning:** Generates targeted search queries based on the research topic.
- **Web Search Integration:** Uses Tavily to gather relevant web sources.
- **AI-Powered Reports:** Uses Groq to create structured reports with summaries, findings, opportunities, risks, and references.
- **Markdown Export:** Automatically saves timestamped reports in the `reports/` directory.

## Prerequisites

- Python 3.8 or higher
- Groq API key
- Tavily API key

## Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/your-username/triumph10-mycore-research-agent.git
cd triumph10-mycore-research-agent
```

**2. Install dependencies**

Make sure `requirements.txt` contains:

```text
groq
tavily-python
python-dotenv
```

Install them:

```bash
pip install -r requirements.txt
```

**3. Configure environment variables**

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
GROQ_MODEL=openai/gpt-oss-120b
```

Never upload your `.env` file or share your API keys publicly.

## Usage

Run the research agent:

```bash
python main.py
```

Enter your research topic when prompted. ResearchMate AI will gather sources, generate a report, and save it in the `reports/` directory.

## Output

Reports are saved as timestamped Markdown files