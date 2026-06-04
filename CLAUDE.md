---
name: crypto-market-analysis
tagline: On-chain + off-chain crypto research → tokenomics → DeFi analysis → evidence-based investment advice
phase: Phase 1 — Core Sub-Skills (Complete)
---

## Skill Identity

**Skill Name:** crypto-market-analysis  
**Folder:** `D:\Dungchan\5\`  
**Cluster:** B — Financial Intelligence Harness (alongside Skill 4: vn-finance-analysis)  
**Invocation:** `/crypto-market-analysis`

## Problem This Skill Solves

Cryptocurrency markets are uniquely complex: they combine on-chain transparency (blockchain data visible to all) with extreme information asymmetry, narrative-driven price action, DeFi protocol risks, tokenomics manipulation, and 24/7 global trading. A retail user asking "should I buy ETH?" needs a structured analyst workflow — not a one-sentence opinion. This skill acts as a professional crypto analyst, gathering on-chain metrics, tokenomics data, DeFi TVL signals, macro sentiment, and news — then synthesizing them into an evidence-based investment recommendation with explicit risk disclosure.

## Harness Flow Summary

1. **Intake** → Parse user query: asset/protocol name, timeframe, risk tolerance, portfolio context
2. **Sub-skill: `sub-evidence-collector`** → Gather news, academic research, social signals, regulatory alerts, developer activity
3. **Sub-skill: `sub-onchain-analytics`** → Pull on-chain metrics: MVRV, NVT, exchange flows, whale activity, realized cap
4. **Sub-skill: `sub-tokenomics-evaluator`** → Analyze supply schedule, vesting cliffs, inflation rate, holder distribution
5. **Sub-skill: `sub-defi-analyzer`** → Assess DeFi protocol TVL, yield sustainability, smart contract risk, audit status (invoke only when applicable)
6. **Sub-skill: `sub-investment-advisor`** → Synthesize all signals → produce tiered recommendation with mandatory risk disclosure
7. **Quality Gate** → Verify evidence citations, risk disclosure present, no unsupported claims
8. **Final Output** → Professional crypto research report artifact

## Sub-Skills

| File | Purpose |
|------|---------|
| `skills/sub-evidence-collector.md` | Multi-source research: news, social signals, academic papers, regulatory alerts, developer activity |
| `skills/sub-onchain-analytics.md` | On-chain metrics analysis: MVRV, NVT, exchange inflows/outflows, whale tracking, miner/validator economics |
| `skills/sub-tokenomics-evaluator.md` | Supply schedule, vesting cliffs, inflation, holder concentration, token utility, health score |
| `skills/sub-defi-analyzer.md` | DeFi TVL, yield sustainability, protocol risk, audit findings, governance health, competitive positioning |
| `skills/sub-investment-advisor.md` | Signal aggregation, tiered recommendation (Buy/Hold/Sell/Avoid), position sizing, risk disclosure |

## Tools Required

- `WebSearch` — News, Reddit, CoinGecko, CoinMarketCap, DeFiLlama, regulatory sources
- `WebFetch` — Direct page fetches: Glassnode Insights, Dune Analytics, Token Terminal, Messari, GitHub
- `Read` — SECOND-KNOWLEDGE-BRAIN.md (internal knowledge fallback when live data unavailable)
- `Write` — Final research report artifact
- `Bash` — Optional: run tools/knowledge_updater.py

## Knowledge Sources (for crawl4ai)

- **On-chain data:** Glassnode.com, Dune Analytics (dune.com), Nansen.ai, Arkham Intelligence
- **Market data:** CoinGecko API, CoinMarketCap, Messari, Token Terminal
- **DeFi:** DeFiLlama (defillama.com), DeBank, L2Beat, Immunefi, Rekt.news
- **News:** CoinDesk, The Block, Decrypt, Blockworks, Cointelegraph
- **Academic:** SSRN Crypto papers, ArXiv cs.CR / q-fin sections, NBER crypto working papers, BIS Bulletin
- **Regulatory:** SEC.gov enforcement, CFTC guidance, FSB crypto reports, EU MiCA (ESMA), MAS Singapore, SFC Hong Kong, FCA UK
- **Social signals:** Reddit r/CryptoCurrency, r/Bitcoin, r/ethereum, Twitter/X crypto KOLs, Santiment

## Supporting Python Tools

- `tools/knowledge_updater.py` — crawl4ai pipeline: scrapes ArXiv, SSRN, CoinDesk, DeFiLlama, BIS weekly → appends new entries to SECOND-KNOWLEDGE-BRAIN.md with deduplication

## Active Development Tasks

- [x] idea.txt analyzed
- [x] CLAUDE.md written
- [x] PROJECT-detail.md written
- [x] PROJECT-DEVELOPMENT-PHASE-TRACKING.md written
- [x] SECOND-KNOWLEDGE-BRAIN.md written
- [x] skills/main.md written
- [x] skills/sub-evidence-collector.md written
- [x] skills/sub-onchain-analytics.md written
- [x] skills/sub-tokenomics-evaluator.md written
- [x] skills/sub-defi-analyzer.md written
- [x] skills/sub-investment-advisor.md written
- [x] tools/knowledge_updater.py written
- [x] tests/test-scenarios.md written
- [ ] Integration test: run test-scenarios.md against live skill
- [ ] Connect to Skill 7 (research-first-reasoning) as meta-skill import

## Related Files

- `PROJECT-detail.md` — Full technical specification
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — Build roadmap by phase
- `SECOND-KNOWLEDGE-BRAIN.md` — Self-improving domain knowledge base
