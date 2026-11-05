"""Generates the final report."""

from pathlib import Path


def generate_report(topic: str, findings: list[str]) -> Path:
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    report_path = reports_dir / "report.txt"
    report_content = f"Topic: {topic}\n\nFindings:\n" + "\n".join(findings)
    report_path.write_text(report_content, encoding="utf-8")
    return report_path
