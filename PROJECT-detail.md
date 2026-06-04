# PROJECT-detail.md — crypto-market-analysis Skill
**Skill:** crypto-market-analysis | **Folder:** `D:\Dungchan\5\` | **Version:** 1.0 | **Date:** 2026-06-04

---

## Executive Summary

The `crypto-market-analysis` skill is a professional-grade cryptocurrency research harness for Claude Code. It transforms a simple user query (e.g., "Should I buy ETH?") into a structured, evidence-based research report covering on-chain metrics, tokenomics analysis, DeFi protocol assessment, and investment advisory — always backed by named sources and accompanied by mandatory risk disclosure.

The skill belongs to **Cluster B** (Financial Intelligence Harnesses) alongside Skill 4 (vn-finance-analysis). Both share a deep research-first philosophy with continuous self-improvement via a `crawl4ai` knowledge pipeline.

---

## Problem Statement

### Domain Context
Cryptocurrency markets present a unique analytical challenge:

1. **Information asymmetry at scale** — On-chain data is public, but interpreting it requires specialized knowledge (MVRV, NVT, exchange flows). Most retail users cannot decode this data.
2. **24/7 global markets with extreme volatility** — A tweet, a regulatory announcement, or a smart contract exploit can move markets 30–50% in hours.
3. **Narrative-driven price action** — Crypto prices often disconnect from fundamentals for months. Distinguishing narrative momentum from fundamental value requires structured frameworks.
4. **DeFi complexity** — Decentralized finance introduces novel risks: tokenomics inflation spirals, mercenary capital yield farming, smart contract exploits, and governance attacks — none of which exist in traditional finance.
5. **Regulatory uncertainty** — Crypto regulation varies by jurisdiction and evolves rapidly, creating binary risk events (SEC enforcement action, country ban, ETF approval).

### What Users Need
A retail or semi-professional user asking about crypto needs:
- **Data they cannot easily gather themselves** (on-chain metrics, TVL, tokenomics schedules)
- **A structured framework** to avoid cognitive biases (FOMO, FUD, confirmation bias)
- **Multiple scenarios**, not just a one-directional price call
- **Explicit risk disclosure** to protect against uninformed decisions
- **Traceable evidence**, not "some analysts say..."

---

## Target Users & Use Cases

### User Profiles
| Profile | Background | Typical Query |
|---------|-----------|--------------|
| Retail Investor | Basic crypto knowledge, holds Bitcoin/ETH | "Is now a good time to buy more BTC?" |
| DeFi Participant | Familiar with wallets, DeFi protocols | "Is Aave's yield sustainable? Should I deposit?" |
| Portfolio Manager | Manages crypto allocation for fund/family office | "Evaluate adding 5% Solana to our portfolio" |
| Researcher/Analyst | Crypto-native, wants second opinion | "What does on-chain data say about ETH accumulation right now?" |
| Cautious Observer | New to crypto, risk-aware | "Is crypto worth investing in at all? What are the real risks?" |

### Trigger Conditions → Skill Response Mapping
| User Says... | Skill Does... |
|-------------|--------------|
| "Should I buy [TOKEN]?" | Full harness: evidence → on-chain → tokenomics → DeFi (if applicable) → advisory |
| "Is [PROTOCOL] DeFi yield safe?" | Focus: sub-defi-analyzer + sub-tokenomics-evaluator + advisory |
| "What does on-chain say about [ASSET]?" | Focus: sub-evidence-collector + sub-onchain-analytics |
| "What's the regulatory risk for [ASSET]?" | Focus: sub-evidence-collector (regulatory section) → advisory |
| "Help me think through my crypto portfolio" | Portfolio-level harness: macro scope, not single-asset call |
| "[Event] just happened. What does it mean?" | Emergency assessment mode: evidence-first, epistemic humility |

---

## Harness Architecture

```
User Query
    │
    ▼
┌─────────────────────────────────┐
│   Stage 0: Intake & Parsing     │
│   - Extract: asset, timeframe,  │
│     risk tolerance, query type  │
│   - Clarify if ambiguous        │
└─────────────────┬───────────────┘
                  │
                  ▼
┌─────────────────────────────────┐
│   Stage 1: Evidence Collection  │
│   → sub-evidence-collector      │
│   - News (7d/30d/90d)           │
│   - Academic papers             │
│   - Regulatory intelligence     │
│   - Social sentiment            │
│   - Developer activity          │
└─────────────────┬───────────────┘
                  │
          ┌───────┼───────┐
          │       │       │
          ▼       ▼       ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────────┐
│  Stage 2:    │  │  Stage 3:    │  │  Stage 4:        │
│  On-Chain    │  │  Tokenomics  │  │  DeFi Analysis   │
│  Analytics   │  │  Evaluator   │  │  (conditional)   │
│              │  │              │  │                  │
│ → sub-       │  │ → sub-       │  │ → sub-           │
│   onchain-   │  │   tokenomics-│  │   defi-          │
│   analytics  │  │   evaluator  │  │   analyzer       │
└──────┬───────┘  └──────┬───────┘  └────────┬─────────┘
       │                 │                   │
       └─────────────────┴───────────────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Stage 5:           │
              │   Investment         │
              │   Advisory           │
              │ → sub-investment-    │
              │   advisor            │
              │                      │
              │ Signal aggregation   │
              │ Scenario analysis    │
              │ Risk disclosure      │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Stage 6:           │
              │   Quality Gate       │
              │ - All claims cited?  │
              │ - Risk disclosure?   │
              │ - Scenarios sum ~100%│
              │ - Data timestamped?  │
              └──────────┬───────────┘
                         │
                    PASS │ FAIL → back to relevant stage
                         │
                         ▼
              ┌──────────────────────┐
              │   Stage 7:           │
              │   Final Report       │
              │   (Write artifact)   │
              └──────────────────────┘
```

---

## Full Sub-Skill Catalog

### 1. sub-evidence-collector
**File:** `skills/sub-evidence-collector.md`  
**Purpose:** Multi-source research gathering before any analysis begins  
**Inputs:** Asset/protocol name, timeframe (7d/30d/90d/12m), query focus  
**Outputs:** Evidence summary with tiered sources, sentiment assessment, regulatory status  
**Tools:** WebSearch, WebFetch (optional)  
**Quality Gate:** ≥5 dated sources with URLs, ≥1 T1/T2 source, regulatory status confirmed, sentiment evidence-based  

### 2. sub-onchain-analytics
**File:** `skills/sub-onchain-analytics.md`  
**Purpose:** Blockchain data metrics interpretation for investment signals  
**Inputs:** Asset name and blockchain network, analysis scope  
**Outputs:** Valuation metrics table, exchange flow analysis, network health assessment, on-chain verdict  
**Tools:** WebSearch, WebFetch (Glassnode, Dune, Token Terminal)  
**Quality Gate:** ≥3 on-chain metrics with values, provider named, exchange flow direction stated, limitations noted  

### 3. sub-tokenomics-evaluator
**File:** `skills/sub-tokenomics-evaluator.md`  
**Purpose:** Token supply, distribution, vesting, and utility analysis  
**Inputs:** Asset/protocol name and ticker, contract address (optional), analysis focus  
**Outputs:** Supply overview table, unlock calendar (90-day horizon), holder concentration, utility assessment, health score /25  
**Tools:** WebSearch, WebFetch (CoinGecko, Messari, project docs, token.unlocks.app)  
**Quality Gate:** Circulating/total ratio stated, inflation rate estimated, unlock events searched, utility classified, health score computed  

### 4. sub-defi-analyzer
**File:** `skills/sub-defi-analyzer.md`  
**Purpose:** DeFi protocol risk assessment and yield sustainability audit  
**Inputs:** Protocol name, category (DEX/Lending/Yield/Staking), analysis focus  
**Outputs:** Protocol metrics table, yield sustainability classification, smart contract audit findings, governance health, competitive position, verdict  
**Tools:** WebSearch, WebFetch (DeFiLlama, Token Terminal, Immunefi, Rekt.news)  
**Invoke Condition:** Only when user query involves a DeFi protocol, governance token, or DeFi yield opportunity  
**Quality Gate:** TVL sourced from DeFiLlama, yield sustainability classified, audit status confirmed, exploits checked, verdict justified  

### 5. sub-investment-advisor
**File:** `skills/sub-investment-advisor.md`  
**Purpose:** Final synthesis into evidence-based recommendation with mandatory risk disclosure  
**Inputs:** Signals from all upstream sub-skills, user risk tolerance, timeframe, portfolio context  
**Outputs:** Signal aggregation table, composite score, investment signal, three-scenario analysis, recommendation table, risk disclosure  
**Tools:** None (synthesis from prior stages)  
**Quality Gate:** Full risk disclosure present, probabilities sum ~100%, specific catalysts in each scenario, allocation labeled "educational reference only", ≥3 risks listed  

---

## Skill File Format Specification

### Frontmatter Schema
```yaml
---
name: crypto-market-analysis          # Invocation name (no spaces)
description: One-line summary shown   # in /help and skill picker
---
```

### Required Sections in main.md
1. `## Role & Persona` — who Claude becomes
2. `## Workflow (Harness Flow)` — numbered stages with sub-skill invocations
3. `## Sub-skills Available` — table: sub-skill | invocation | purpose
4. `## Tools` — which Claude Code tools are used
5. `## Output Format` — exact deliverable structure (markdown template)
6. `## Quality Gates` — checklist Claude must pass before final output

---

## E2E Execution Flow

```
Step 1: User types /crypto-market-analysis [optional: asset name]
Step 2: Harness reads user message — extracts: asset, timeframe, risk tolerance, query type
  → If any parameter ambiguous: ask ONE clarifying question, then proceed
Step 3: Invoke sub-evidence-collector
  → WebSearch: 5+ news queries + 2+ academic queries + 1+ regulatory query
  → Assess sentiment, tier sources, flag regulatory risks
  → Return: evidence summary block
Step 4: Invoke sub-onchain-analytics
  → WebSearch/WebFetch: on-chain data providers (Glassnode, Dune, etc.)
  → Compute: MVRV context, exchange flow direction, network health
  → Return: on-chain analysis block
Step 5: Invoke sub-tokenomics-evaluator
  → WebSearch: CoinGecko supply data, Messari tokenomics, project docs
  → Compute: health score /25, identify upcoming unlock events
  → Return: tokenomics analysis block
Step 6 (conditional): Invoke sub-defi-analyzer
  → If query involves DeFi protocol or DeFi yield:
    → WebSearch/WebFetch: DeFiLlama TVL, Token Terminal revenue, Immunefi audits, Rekt.news
    → Classify: yield sustainability (sustainable/at risk/unsustainable)
    → Return: DeFi protocol analysis block
  → Else: skip, note "DeFi analysis not applicable for [ASSET]"
Step 7: Invoke sub-investment-advisor
  → Aggregate all signals → compute composite weighted score
  → Map to signal tier (Strong Buy → Avoid)
  → Calibrate to user risk tolerance
  → Write: bull/base/bear scenarios with probabilities
  → Write: FULL risk disclosure (no abbreviation allowed)
  → Return: investment advisory block
Step 8: Quality Gate check
  → All 7 gates must pass (see Quality Gates section in main.md)
  → If any gate fails: return to relevant stage and correct
Step 9: Write final report (Write tool)
  → Structured report artifact in Output Format template
  → Saved to conversation or file if requested
```

### Error Handling
| Condition | Behavior |
|-----------|---------|
| WebSearch unavailable | Fall back to SECOND-KNOWLEDGE-BRAIN.md + clearly label: "Live data unavailable — internal knowledge as of [date]" |
| Asset not found in any source | Flag: "Insufficient data — HIGH uncertainty" + issue AVOID signal by default |
| User does not specify risk tolerance | Default to Moderate; note assumption in output |
| DeFi protocol has no audit data | Flag as HIGH smart contract risk; do NOT assume audited |
| Regulatory status unclear | Flag as UNKNOWN — do not assume safe |
| On-chain data > 48 hours old | Label as "cached — may not reflect current state" |

---

## SECOND-KNOWLEDGE-BRAIN Integration

### Sources Crawled
| Source | Category | Frequency | Method |
|--------|---------|-----------|--------|
| ArXiv (cs.CR, q-fin) | Academic papers | Weekly | crawl4ai API fetch |
| SSRN Crypto section | Academic papers | Weekly | crawl4ai scrape |
| CoinDesk Research | News/Research | Weekly | crawl4ai scrape |
| The Block Research | News/Research | Weekly | crawl4ai scrape |
| Glassnode Insights | On-chain commentary | Weekly | crawl4ai scrape |
| DeFiLlama Blog | DeFi data | Weekly | crawl4ai scrape |
| Token Terminal Resources | Fundamentals | Weekly | crawl4ai scrape |
| BIS Crypto Reports | Regulatory/Academic | Weekly | crawl4ai scrape |

### Knowledge Brain Sections
1. **Core Concepts & Frameworks** — on-chain analysis, tokenomics, DeFi risk, sentiment
2. **Key Research Papers** — foundational and recent academic work (table format)
3. **State-of-the-Art Methods & Tools** — on-chain providers, market data APIs, DeFi analytics
4. **Authoritative Data Sources** — URL directory by category
5. **Analytical Frameworks** — Skill 7 methods applied to crypto domain
6. **Self-Update Protocol** — crawl configuration, append format, deduplication
7. **Knowledge Update Log** — date-stamped history of additions

---

## Quality Gates

The following 7 gates must all pass before final output is presented:

| Gate | Description | Fail Action |
|------|-------------|-------------|
| G1: Citation completeness | All factual claims have named, dated sources | Return to relevant stage, add missing citations |
| G2: Risk disclosure | Full risk disclosure text present (not abbreviated) | Add full disclosure to advisory section |
| G3: No certainty claims | No price predictions stated as certainties | Rephrase as probability statements or scenarios |
| G4: Data freshness | On-chain data timestamp noted; if >48h old, labeled as cached | Add timestamp or cached label |
| G5: Unlock review | Tokenomics includes 90-day unlock event search result | Re-run sub-tokenomics-evaluator |
| G6: Bear case rigor | Bear case has specific catalysts, not vague "price could fall" | Rewrite bear case with concrete triggers |
| G7: Risk calibration | Recommendation reflects user's stated risk tolerance | Adjust allocation ceiling and signal threshold |

---

## Test Scenarios

See `tests/test-scenarios.md` for 6 complete test scenarios covering:
1. Bitcoin broad market analysis (moderate risk, 6-month)
2. Uniswap DeFi governance token (aggressive risk, 4-week)
3. Unknown high-yield token (red flag detection)
4. Ethereum staking yield (conservative risk, 12-month)
5. Portfolio-level macro rebalancing question
6. Regulatory shock response (emergency assessment mode)

---

## Key Design Decisions

1. **DeFi sub-skill is conditional:** Unlike on-chain and tokenomics (always run), sub-defi-analyzer is only invoked for DeFi-relevant queries. Running it on BTC analysis would add noise, not signal.

2. **Weighted composite score for advisory:** Rather than subjective judgement, sub-investment-advisor uses a weighted scoring rubric (on-chain 35%, tokenomics 25%, evidence 20%, DeFi 20%) to derive the signal tier.

3. **Full risk disclosure is non-negotiable:** The quality gate for risk disclosure has no exceptions — even for "obvious" risk scenarios. This protects against legal liability and user harm.

4. **Graceful degradation by design:** All stages explicitly handle the case where live data is unavailable. The skill degrades to internal knowledge (SECOND-KNOWLEDGE-BRAIN.md) rather than failing silently.

5. **Three-scenario framework (not just bull/bear):** Base case prevents binary thinking and forces the analyst to quantify the probability of the "most likely outcome" — often the most important signal.

6. **Evidence tiering (T1–T5):** Prevents social media sentiment from overriding on-chain data in the final recommendation. T4/T5 sources inform sentiment context only, never primary signals.

7. **Skill 7 integration pathway:** The `research-first-reasoning` meta-skill can be invoked via `Skill("research-first-reasoning")` from within the evidence collection stage for any query requiring deeper methodological rigor (e.g., a novel DeFi mechanism with no precedent).
