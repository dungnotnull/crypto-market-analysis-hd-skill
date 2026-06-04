#!/usr/bin/env python3
"""
knowledge_updater.py — Crypto Market Analysis Skill (Folder 5)
==============================================================
Crawls ArXiv, SSRN, CoinDesk, Glassnode Insights, DeFiLlama Blog, BIS, and
Token Terminal to discover new crypto research and articles. Appends new
findings to SECOND-KNOWLEDGE-BRAIN.md with deduplication.

Requirements:
    pip install crawl4ai

Recommended Schedule:
    Weekly — Sunday 02:00 UTC via cron or Windows Task Scheduler

Usage:
    python tools/knowledge_updater.py
"""

import asyncio
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BRAIN_PATH = Path(__file__).parent.parent / "SECOND-KNOWLEDGE-BRAIN.md"
STATE_PATH = Path(__file__).parent / "crawler_state.json"

ARXIV_BASE_URL = "https://export.arxiv.org/api/query"

ARXIV_QUERIES = [
    "cryptocurrency bitcoin blockchain",
    "DeFi decentralized finance yield",
    "tokenomics cryptoasset token economics",
    "on-chain analytics bitcoin ethereum",
    "cryptocurrency market microstructure",
    "stablecoin mechanism design",
    "crypto regulation compliance digital assets",
    "zero knowledge proof layer2 ZKP scaling",
]

ARXIV_CATEGORIES = ["cs.CR", "econ.GN", "q-fin.TR", "q-fin.RM", "cs.CE"]

WEB_SOURCES = [
    {
        "name": "CoinDesk Research",
        "url": "https://www.coindesk.com/research/",
        "type": "news",
    },
    {
        "name": "The Block Research",
        "url": "https://www.theblock.co/research",
        "type": "news",
    },
    {
        "name": "Glassnode Insights",
        "url": "https://insights.glassnode.com/",
        "type": "onchain",
    },
    {
        "name": "DeFiLlama Blog",
        "url": "https://defillama.com/blog",
        "type": "defi",
    },
    {
        "name": "Token Terminal Resources",
        "url": "https://tokenterminal.com/resources",
        "type": "analytics",
    },
    {
        "name": "BIS Crypto Reports",
        "url": "https://www.bis.org/topics/cryptoassets.htm",
        "type": "regulatory",
    },
    {
        "name": "Messari Research",
        "url": "https://messari.io/research",
        "type": "research",
    },
]

# Keywords used to score relevance (higher match count = more relevant)
CRYPTO_KEYWORDS = [
    "bitcoin", "ethereum", "defi", "tokenomics", "on-chain", "blockchain",
    "cryptocurrency", "crypto", "layer2", "zk-proof", "stablecoin",
    "mvrv", "nvt", "exchange flow", "whale", "validator", "consensus",
    "smart contract", "protocol", "tvl", "yield", "liquidity", "amm",
    "nft", "dao", "governance", "token", "wallet", "dex", "lending",
    "cross-chain", "bridge", "oracle", "mev", "flashloan", "l2",
]

MAX_PAPERS_PER_RUN = 20
MAX_ARTICLES_PER_SOURCE = 3
MAX_SOURCES_PER_RUN = 5
MIN_RELEVANCE_SCORE = 2  # Minimum keyword matches to include an entry


# ---------------------------------------------------------------------------
# State Management
# ---------------------------------------------------------------------------

def load_state() -> dict:
    """Load crawler state (seen hashes, last run date) from JSON file."""
    if STATE_PATH.exists():
        with open(STATE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"seen_hashes": [], "last_run": None, "total_entries_added": 0}


def save_state(state: dict) -> None:
    """Persist crawler state after each run."""
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def compute_hash(identifier: str) -> str:
    """Compute a short MD5 hash for deduplication (URL or DOI)."""
    return hashlib.md5(identifier.strip().lower().encode("utf-8")).hexdigest()[:12]


# ---------------------------------------------------------------------------
# Relevance Scoring
# ---------------------------------------------------------------------------

def score_relevance(text: str) -> int:
    """Score text relevance to crypto domain (0–10+ keyword matches)."""
    text_lower = text.lower()
    return sum(1 for kw in CRYPTO_KEYWORDS if kw in text_lower)


# ---------------------------------------------------------------------------
# ArXiv Fetcher
# ---------------------------------------------------------------------------

async def fetch_arxiv_papers(
    queries: list[str],
    categories: list[str],
    crawler,
) -> list[dict]:
    """Fetch recent crypto-relevant papers from ArXiv API."""
    papers = []
    cat_filter = "+OR+".join(f"cat:{c}" for c in categories[:3])

    for query in queries[:4]:  # Limit to 4 queries to avoid rate limiting
        search_url = (
            f"{ARXIV_BASE_URL}?search_query="
            f"({query.replace(' ', '+')})+"
            f"AND+({cat_filter})"
            f"&sortBy=submittedDate&sortOrder=descending&max_results=10"
        )
        try:
            result = await crawler.arun(url=search_url)
            if result.success:
                content = result.html or result.markdown or ""
                batch = _parse_arxiv_xml(content)
                papers.extend(batch)
                print(f"  ArXiv '{query}': {len(batch)} papers found")
        except Exception as e:
            print(f"  ArXiv error for '{query}': {e}")

        await asyncio.sleep(1)  # Respectful delay between ArXiv requests

    return papers[:MAX_PAPERS_PER_RUN]


def _parse_arxiv_xml(content: str) -> list[dict]:
    """Parse ArXiv API Atom/XML response into paper dictionaries."""
    papers = []
    entries = re.findall(r"<entry>(.*?)</entry>", content, re.DOTALL)

    for entry in entries:
        try:
            title_m = re.search(r"<title>(.*?)</title>", entry, re.DOTALL)
            authors_m = re.findall(r"<author><name>(.*?)</name></author>", entry)
            id_m = re.search(r"<id>(.*?)</id>", entry)
            pub_m = re.search(r"<published>(.*?)</published>", entry)
            summary_m = re.search(r"<summary>(.*?)</summary>", entry, re.DOTALL)

            if not title_m or not id_m:
                continue

            title = re.sub(r"\s+", " ", title_m.group(1)).strip()
            authors_list = authors_m[:3]
            authors = ", ".join(authors_list)
            if len(authors_m) > 3:
                authors += " et al."
            arxiv_url = id_m.group(1).strip()
            arxiv_id = arxiv_url.split("/abs/")[-1] if "/abs/" in arxiv_url else arxiv_url
            year = pub_m.group(1)[:4] if pub_m else datetime.now().strftime("%Y")
            summary = re.sub(r"\s+", " ", summary_m.group(1)).strip() if summary_m else ""

            relevance = score_relevance(title + " " + summary)
            if relevance < MIN_RELEVANCE_SCORE:
                continue

            papers.append({
                "title": title,
                "authors": authors,
                "year": year,
                "arxiv_id": arxiv_id,
                "url": arxiv_url,
                "summary": summary[:200],
                "relevance_note": (summary[:80] if summary else "See abstract"),
                "relevance_score": relevance,
                "hash": compute_hash(arxiv_url),
            })
        except Exception:
            continue

    return sorted(papers, key=lambda p: p["relevance_score"], reverse=True)


def _fallback_arxiv_papers() -> list[dict]:
    """
    Return seed papers when crawl4ai is unavailable.
    These are high-quality foundational crypto papers that should always be
    available in the knowledge base even without live crawling.
    """
    return [
        {
            "title": "Flash Boys 2.0: Frontrunning in Decentralized Exchanges",
            "authors": "Daian, P., Goldfeder, S., Kell, T. et al.",
            "year": "2019",
            "arxiv_id": "1904.05234",
            "url": "https://arxiv.org/abs/1904.05234",
            "summary": "Seminal paper on miner extractable value (MEV) and front-running in DeFi.",
            "relevance_note": "Foundation for MEV understanding — essential for DeFi risk analysis",
            "relevance_score": 10,
            "hash": compute_hash("https://arxiv.org/abs/1904.05234"),
        },
        {
            "title": "DeFi and the Future of Finance",
            "authors": "Harvey, C., Ramachandran, A., Santoro, J.",
            "year": "2021",
            "arxiv_id": "2106.08157",
            "url": "https://arxiv.org/abs/2106.08157",
            "summary": "Comprehensive analysis of decentralized finance protocols, risks, and opportunities.",
            "relevance_note": "Essential DeFi reference — covers AMMs, lending, stablecoins, governance",
            "relevance_score": 10,
            "hash": compute_hash("https://arxiv.org/abs/2106.08157"),
        },
        {
            "title": "SoK: Decentralized Finance (DeFi)",
            "authors": "Werner, S., Perez, D., Gudgeon, L. et al.",
            "year": "2022",
            "arxiv_id": "2101.08778",
            "url": "https://arxiv.org/abs/2101.08778",
            "summary": "Systematic overview of the DeFi ecosystem covering protocols, attacks, and research challenges.",
            "relevance_note": "Most comprehensive DeFi survey paper — essential reading",
            "relevance_score": 10,
            "hash": compute_hash("https://arxiv.org/abs/2101.08778"),
        },
    ]


# ---------------------------------------------------------------------------
# Web Source Crawler
# ---------------------------------------------------------------------------

async def fetch_web_sources(
    sources: list[dict],
    crawler,
) -> list[dict]:
    """Fetch and parse articles from curated web sources."""
    articles = []

    for source in sources[:MAX_SOURCES_PER_RUN]:
        try:
            result = await crawler.arun(url=source["url"])
            if result.success:
                content = result.markdown or result.html or ""
                batch = _extract_articles(content, source)
                articles.extend(batch[:MAX_ARTICLES_PER_SOURCE])
                print(f"  Web '{source['name']}': {len(batch)} articles found")
            else:
                print(f"  Web '{source['name']}': fetch failed (non-200 or timeout)")
        except Exception as e:
            print(f"  Web error for '{source['name']}': {e}")

        await asyncio.sleep(2)  # Respectful delay between web requests

    return articles


def _extract_articles(content: str, source: dict) -> list[dict]:
    """Extract article metadata from crawled markdown/HTML content."""
    today = datetime.now().strftime("%Y-%m-%d")
    articles = []

    # Extract markdown-style hyperlinks: [title](url)
    links = re.findall(r"\[([^\]]{15,100})\]\((https?://[^\s\)]+)\)", content)

    for title, url in links[:20]:
        title = title.strip()
        relevance = score_relevance(title)
        if relevance < MIN_RELEVANCE_SCORE:
            continue

        # Skip obviously non-article URLs (nav links, social, etc.)
        skip_patterns = ["twitter.com", "facebook.com", "linkedin.com", "#", "mailto:", "/tag/"]
        if any(p in url.lower() for p in skip_patterns):
            continue

        articles.append({
            "title": title,
            "url": url,
            "source": source["name"],
            "date": today,
            "type": source["type"],
            "summary": f"From {source['name']}: {title}",
            "relevance_score": relevance,
            "hash": compute_hash(url),
        })

    return sorted(articles, key=lambda a: a["relevance_score"], reverse=True)


# ---------------------------------------------------------------------------
# Knowledge Brain Updater
# ---------------------------------------------------------------------------

def format_paper_row(paper: dict) -> str:
    """Format an ArXiv paper as a markdown table row."""
    title = paper["title"][:70]
    authors = paper["authors"][:45]
    arxiv_id = paper["arxiv_id"]
    url = paper["url"]
    relevance = paper["relevance_note"][:65]
    return (
        f"| {title} | {authors} | {paper['year']} | ArXiv | "
        f"[{arxiv_id}]({url}) | {relevance} |"
    )


def format_article_bullet(article: dict) -> str:
    """Format a web article as a markdown list item."""
    return (
        f"- **[{article['title'][:65]}]({article['url']})** "
        f"({article['source']}, {article['date']}) — {article['summary'][:100]}"
    )


def append_to_knowledge_brain(
    papers: list[dict],
    articles: list[dict],
    state: dict,
) -> int:
    """
    Append new, non-duplicate entries to SECOND-KNOWLEDGE-BRAIN.md.
    Returns the count of new entries added.
    """
    if not papers and not articles:
        print("No entries to append.")
        return 0

    today = datetime.now().strftime("%Y-%m-%d")
    seen = set(state["seen_hashes"])
    new_hashes: list[str] = []
    paper_rows: list[str] = []
    article_bullets: list[str] = []

    for paper in papers:
        if paper["hash"] in seen:
            continue
        paper_rows.append(format_paper_row(paper))
        new_hashes.append(paper["hash"])

    for article in articles:
        if article["hash"] in seen:
            continue
        article_bullets.append(format_article_bullet(article))
        new_hashes.append(article["hash"])

    if not new_hashes:
        print("All fetched entries are already in the knowledge base (deduplication).")
        return 0

    # Build the update block
    block = f"\n\n---\n## Knowledge Update — {today}\n\n"

    if paper_rows:
        block += "### New Research Papers\n"
        block += "| Title | Authors | Year | Venue | DOI/Link | Relevance |\n"
        block += "|-------|---------|------|-------|----------|----------|\n"
        block += "\n".join(paper_rows)
        block += "\n\n"

    if article_bullets:
        block += "### New Web Sources & Reports\n"
        block += "\n".join(article_bullets)
        block += "\n\n"

    block += (
        f"_Entries added: {len(new_hashes)} "
        f"({len(paper_rows)} papers, {len(article_bullets)} articles) | "
        f"Run timestamp: {datetime.now().isoformat()}_\n"
    )

    # Append to the file
    with open(BRAIN_PATH, "a", encoding="utf-8") as f:
        f.write(block)

    # Update state
    state["seen_hashes"].extend(new_hashes)
    state["last_run"] = today
    state["total_entries_added"] = state.get("total_entries_added", 0) + len(new_hashes)
    save_state(state)

    return len(new_hashes)


# ---------------------------------------------------------------------------
# Main Entry Point
# ---------------------------------------------------------------------------

async def main() -> None:
    """
    Main pipeline:
    1. Load state (deduplication hashes from previous runs)
    2. Fetch ArXiv papers using crawl4ai
    3. Fetch web source articles using crawl4ai
    4. Append new entries to SECOND-KNOWLEDGE-BRAIN.md
    5. Save updated state
    """
    print("=" * 60)
    print("knowledge_updater.py — crypto-market-analysis skill")
    print(f"Run time: {datetime.now().isoformat()}")
    print(f"Brain path: {BRAIN_PATH}")
    print("=" * 60)

    if not BRAIN_PATH.exists():
        print(f"\nERROR: SECOND-KNOWLEDGE-BRAIN.md not found at:\n  {BRAIN_PATH}")
        print("Ensure this script is run from the D:\\Dungchan\\5\\tools\\ directory")
        print("or adjust BRAIN_PATH in the script configuration.")
        return

    state = load_state()
    print(
        f"\nPrevious run: {state.get('last_run', 'never')} | "
        f"Known entries: {len(state['seen_hashes'])} | "
        f"Total added to date: {state.get('total_entries_added', 0)}"
    )

    # Attempt to import crawl4ai
    try:
        from crawl4ai import AsyncWebCrawler
        crawl4ai_available = True
    except ImportError:
        print(
            "\n⚠️  crawl4ai not installed — using seed papers only.\n"
            "   Install: pip install crawl4ai\n"
            "   After installing, re-run this script for full crawling."
        )
        crawl4ai_available = False

    papers: list[dict] = []
    articles: list[dict] = []

    if crawl4ai_available:
        async with AsyncWebCrawler(verbose=False) as crawler:
            print("\n[1/3] Fetching ArXiv papers...")
            papers = await fetch_arxiv_papers(ARXIV_QUERIES, ARXIV_CATEGORIES, crawler)
            print(f"  Total relevant papers fetched: {len(papers)}")

            print("\n[2/3] Fetching web sources...")
            articles = await fetch_web_sources(WEB_SOURCES, crawler)
            print(f"  Total relevant articles fetched: {len(articles)}")
    else:
        print("\n[1/3] Loading fallback seed papers...")
        papers = _fallback_arxiv_papers()
        print(f"  Seed papers loaded: {len(papers)}")
        print("\n[2/3] Skipping web sources (crawl4ai unavailable).")

    print("\n[3/3] Appending to SECOND-KNOWLEDGE-BRAIN.md...")
    n_added = append_to_knowledge_brain(papers, articles, state)

    print("\n" + "=" * 60)
    if n_added > 0:
        print(f"✅ Knowledge brain updated: {n_added} new entries added.")
    else:
        print("ℹ️  Knowledge brain unchanged: all entries already present.")
    print(
        f"   Total entries in knowledge base: {state.get('total_entries_added', 0)}"
    )
    print("\nSchedule this script weekly for continuous knowledge improvement.")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
