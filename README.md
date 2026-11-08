# MyCore Research Agent

An automated AI-powered research assistant built in Python that takes any research topic, plans targeted web search queries, gathers up-to-date data using Tavily, and leverages Groq's high-performance LLM to generate a comprehensive, structured research report saved as a Markdown file.

---

## Project Structure

```text
triumph10-mycore-research-agent/
├── README.md
├── main.py
├── researcher.py
├── search_tool.py
├── report_generator.py
├── requirements.txt
└── reports/
    └── .gitkeep
Features
Automated Research Planning: Dynamically generates strategic web search queries based on your input topic.

Web Search Integration: Connects with the Tavily API to fetch clean, relevant, and up-to-date web sources.

LLM-Powered Synthesis: Uses Groq to synthesize research data into an organized report complete with an executive summary, key findings, benefits, challenges, future opportunities, and source references.

Automated Export: Timestamps and saves completed reports directly into the reports/ directory in Markdown format.

Prerequisites
Python 3.8 or higher

A Groq API Key (for LLM generation)

A Tavily API Key (for web searching)

Installation & Setup
Clone or Download the Repository:

Bash
git clone [https://github.com/your-username/triumph10-mycore-research-agent.git](https://github.com/your-username/triumph10-mycore-research-agent.git)
cd triumph10-mycore-research-agent
Populate requirements.txt:
Ensure your requirements.txt file contains the necessary project dependencies:

Plaintext
groq
tavily-python
python-dotenv
Install Dependencies:
Run the following command in your terminal:

Bash
pip install -r requirements.txt
Configure Environment Variables:
Create a .env file in the root directory of your project and add your API keys:

Code snippet
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
Usage
Run the main script to start the agent:

Bash
python main.p
