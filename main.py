"""Starts the application."""

from researcher import Researcher


def main() -> None:
    researcher = Researcher()
    researcher.run()


if __name__ == "__main__":
    main()
