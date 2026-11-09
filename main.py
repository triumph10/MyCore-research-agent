
from researcher import run_research
from report_generator import generate_report
from pathlib import Path
from datetime import datetime


def main():
    print("\n===== RESEARCHMATE AI =====")

    research_date = datetime.now().astimezone()

    topic = input("\nEnter research topic: ").strip()

    if not topic:
        print("Please enter a research topic.")
        return

    print("\nCreating research plan...")

    try:
        sources = run_research(topic)

        if not sources:
            print("No research sources found.")
            return

        print(f"\nFound {len(sources)} unique sources.")

        print("\nGenerating research report...")

        report = generate_report(topic, sources)

        if not report:
            print("Report generation returned no content.")
            return

        Path("reports").mkdir(exist_ok=True)

        filename = (
            research_date.strftime("%Y%m%d_%H%M%S")
            + "_research.md"
        )

        filepath = Path("reports") / filename

        filepath.write_text(report, encoding="utf-8")

        print("\nResearch completed!")
        print(f"Research date: {research_date.date()}")
        print(f"Sources used: {len(sources)}")
        print(f"Report saved at: {filepath}")

        print("\n===== REPORT PREVIEW =====\n")
        print(report[:2500])

    except Exception as error:
        print(f"\nResearchMate encountered an error: {error}")


if __name__ == "__main__":
    main()
