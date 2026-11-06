from researcher import run_research
from report_generator import generate_report

from pathlib import Path
from datetime import datetime


def main():

    print("\n===== RESEARCHMATE AI =====")

    topic = input("\nEnter research topic: ")

    if not topic.strip():
        print("Please enter a research topic.")
        return

    # Step 1: Search the web
    sources = run_research(topic)

    if not sources:
        print("No research sources found.")
        return

    print(f"\nFound {len(sources)} unique sources.")

    # Step 2: Generate report
    print("\nGenerating research report...")

    report = generate_report(topic, sources)

    # Step 3: Save report
    Path("reports").mkdir(exist_ok=True)

    filename = (
        datetime.now().strftime("%Y%m%d_%H%M%S")
        + "_research.md"
    )

    filepath = Path("reports") / filename

    filepath.write_text(report, encoding="utf-8")

    print("\nResearch completed!")
    print(f"Report saved at: {filepath}")

    print("\n===== REPORT PREVIEW =====\n")
    print(report[:2000])


if __name__ == "__main__":
    main()