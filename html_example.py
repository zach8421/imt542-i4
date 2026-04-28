"""
html_example.py - Scrape the Wikipedia "Recycling" article over HTTP and parse the HTML.

HOW TO RUN:
    pip install requests beautifulsoup4
    python3 html_example.py

Requires Python 3.8+. No API key or account needed.
"""

import requests  # type: ignore[import-untyped]
from bs4 import BeautifulSoup  # type: ignore[import-untyped]


def scrape_html_page():
    """Download an HTML page and extract structured content with BeautifulSoup.

    Information structure: HTML
    Access technology:     HTTP GET + HTML parsing library (BeautifulSoup)

    PROS:
      - Works on any public web page, even when no API exists.
      - BeautifulSoup makes traversing the DOM straightforward.
      - Good for one-off data pulls where building/maintaining an API client is overkill.
    CONS:
      - Brittle: any markup change on the source page can break the scraper.
      - Slower and heavier than an API; the whole page is downloaded and parsed.
      - Risk of violating site terms of service or rate limits; needs a polite User-Agent
        and ideally caching/backoff for repeated runs.
    """
    url = "https://en.wikipedia.org/wiki/Recycling"
    headers = {"User-Agent": "IMT542-coursework/1.0 (educational scrape)"}
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1").get_text(strip=True)
    first_paragraph = next(
        p.get_text(strip=True)
        for p in soup.select("div.mw-parser-output > p")
        if p.get_text(strip=True)
    )
    section_headings = [h.get_text(strip=True) for h in soup.select("div.mw-parser-output h2")]

    print("HTML via HTTP + BeautifulSoup")
    print(f"Source: {url}")
    print(f"Title:  {title}")
    print(f"\nFirst paragraph (truncated):\n  {first_paragraph[:400]}...")
    print(f"\nFound {len(section_headings)} top-level section headings. First 10:")
    for heading in section_headings[:10]:
        print(f"  - {heading}")


if __name__ == "__main__":
    scrape_html_page()
