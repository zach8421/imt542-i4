"""
access_example.py - Fetch Seattle waste-sorting data from the SPU taxonomy API.

HOW TO RUN:
    pip install requests
    python3 access_example.py

Requires Python 3.8+. No API key or account needed.
"""

import json
import requests  # type: ignore[import-untyped]


def fetch_json_from_api():
    """Call Seattle Public Utilities' taxonomy API and print a sample of the JSON.

    Information structure: JSON
    Access technology:     HTTP GET to a public REST-ish API (no auth)

    PROS:
      - Always current; no file re-downloads.
      - Structured JSON; minimal parsing.
      - Low bandwidth; fetch only what you need.
    CONS:
      - Needs network; no offline use.
      - Undocumented; may change without notice.
      - Aggressive use may trigger rate limits.
    """
    url = "https://www.seattle.gov/api/content/taxonomy/3086/pages"
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    items = response.json()

    print("JSON via HTTP API")
    print(f"Source: {url}")
    print(f"Received {len(items)} items. First item (truncated):")
    print(json.dumps(items[0], indent=2)[:500] + "...")


if __name__ == "__main__":
    fetch_json_from_api()
