"""Controls the research process."""

from report_generator import generate_report
from search_tool import search_internet


class Researcher:
    def run(self) -> None:
        topic = "example topic"
        findings = search_internet(topic)
        generate_report(topic, findings)
