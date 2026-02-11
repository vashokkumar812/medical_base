#!/usr/bin/env python
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medical_wiki.settings")
    try:
        from django.core.management import execute_from_command_line
    except ModuleNotFoundError as exc:
        if exc.name == "django":
            sys.stderr.write(
                "Django is not installed in this environment.\n"
                "Install backend dependencies first:\n"
                "  python -m pip install -r backend/requirements.txt\n"
                "Or run the app with Docker:\n"
                "  docker compose up --build\n"
            )
            raise SystemExit(1) from exc
        raise

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
