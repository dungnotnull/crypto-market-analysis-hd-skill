# SECOND-KNOWLEDGE-BRAIN.md — Crypto Market Analysis Skill
**Skill:** crypto-market-analysis (Folder 5)  
**Last Updated:** 2026-06-04  
**Update Protocol:** Weekly via `tools/knowledge_updater.py` (crawl4ai pipeline)  
**Graceful Degradation:** If live data unavailable, skill uses this file with caveat: "Based on internal knowledge as of 2026-06-04 — live data not available."

---

## Core Concepts & Frameworks

### 1. Crypto Market Cycle Framework
Crypto markets exhibit 4-year cycles historically tied to Bitcoin halving events (supply shock every ~4 years):

| Phase | Characteristics | Typical Duration | Key On-Chain Signal |
|-------|---------------|-----------------|-------------------|
| Accumulation | Post-bear bottom, smart money accumulates quietly, low retail interest | 6–12 months | MVRV < 1, exchange outflows |
| Early Bull | Increasing developer activity, moderate price appreciation, media attention growing | 6–12 months | Active addresses rising, MVRV 1–3 |
| Late Bull | Retail FOMO, narrative-driven euphoria, new ATHs, high leverage | 3–6 months | MVRV > 5, funding rates positive, exchange inflows |
| Bear | Deleveraging, capitulation, declining fundamentals, project failures | 12–18 months | MVRV < 1, exchange outflows (capitulation), SOPR < 1 |

**Key indicator:** MVRV Z-Score < 0 historically marks bear market bottoms. MVRV Z-Score > 7 historically marks cycle tops. Neither signal is infallible.

### 2. On-Chain Analysis Framework

#### Valuation Metrics Reference
| Metric | Formula | Bear Bottom Range | Fair Value Range | Bull Top Range | Source |
|--------|---------|------------------|-----------------|---------------|--------|
| MVRV Z-Score | (Mkt Cap − Realized Cap) / StdDev | < 0 | 0 – 4 | > 7 | Glassnode |
| NVT Signal | Mkt Cap / 90d avg tx volume | < 40 | 40 – 100 | > 150 | Woobull |
| Puell Multiple | Daily miner revenue / 365d avg | < 0.5 | 0.5 – 4 | > 10 | Glassnode |
| Mayer Multiple | Price / 200-day MA | < 0.8 | 0.8 – 1.5 | > 2.4 | Woobull |
| Reserve Risk | Confidence / HODL Bank | < 0.002 | 0.002 – 0.01 | > 0.02 | Glassnode |
| SOPR (7d MA) | Spent Output Value / Cost Basis | < 1 (capitulation) | ≈ 1 | > 1.05 (distribution) | Glassnode |
| Realized Price | Total value paid / Circulating supply | Mkt price below | ≈ Mkt price | Mkt price above 3x | Glassnode |

#### Exchange Flow Interpretation
- **Net Inflow > 0** (tokens moving to exchanges) = Potential selling pressure
- **Net Inflow < 0** (tokens leaving exchanges) = Accumulation / HODLer behavior
- **Stablecoin Exchange Inflows** = Buying power entering market = Demand signal
- **Large sudden inflows** (>5% of exchange reserves in 24h) = High sell pressure alert

#### Network Health Signals
| Signal | Growing | Stable | Declining |
|--------|---------|--------|-----------|
| Active Addresses (30d MA) | Bullish | Neutral | Bearish |
| Daily Transaction Count | Bullish | Neutral | Bearish |
| Fee Revenue (30d avg) | Bullish | Neutral | Bearish |
| Hashrate (PoW) | Bullish | Neutral | Bearish (miner selling risk) |
| Staking Ratio (PoS) | Bullish | Neutral | Bearish (validator trust declining) |

### 3. Tokenomics Evaluation Framework

#### Supply Dynamics
| Supply Type | Definition | Risk Level |
|------------|-----------|-----------|
| Fixed cap (e.g., BTC 21M) | Hard limit — no new supply ever | Lowest |
| Decreasing emissions (e.g., ETH post-EIP1559) | Deflation possible below demand | Low |
| Controlled low inflation (≤5%/yr) | Predictable, manageable dilution | Medium |
| High inflation (5–20%/yr) | Significant dilution risk | High |
| Hyperinflation (>20%/yr or unlimited) | Death spiral risk — emissions > demand | Very High |

#### Token Utility Quality Matrix
| Utility Type | Example | Quality Rating | Durability |
|-------------|---------|---------------|-----------|
| Native gas / fee payment | ETH for gas | Excellent | Structural demand |
| Protocol revenue share | GMX fee sharing | Very Good | Cash flow backed |
| Collateral in DeFi | wBTC, ETH | Very Good | Trust-derived demand |
| Staking for security | ETH, SOL | Good | Yield dependency risk |
| Governance voting | UNI, AAVE | Fair | Low participation typical |
| Access / subscription | Chainlink LINK | Fair | Substitution risk |
| Pure speculation | Meme coins | Poor | No fundamental floor |

#### Vesting Risk Calendar
- **>5% of circulating supply unlocking in 30 days** = HIGH risk — flag in red
- **2–5% of circulating supply unlocking in 30 days** = MEDIUM risk — note in output
- **<2% of circulating supply unlocking in 30 days** = LOW risk — mention briefly
- **Team/VC allocation unlocking** = Higher risk than ecosystem/community unlocks (profit-taking incentive)

### 4. DeFi Risk Assessment Framework

#### Yield Sustainability Rule
```
Total APY = Real Yield (from protocol fees) + Emissions Yield (from token incentives)

Sustainable:   Real Yield > Emissions Yield
At Risk:       Real Yield 20–50% of Total APY
Unsustainable: Real Yield < 20% of Total APY

Warning sign: APY > 50% is almost always >80% emissions-driven.
Exception:     New protocol bootstrapping phase — expected, but high exit risk.
```

#### Smart Contract Risk Tiers
| Risk Level | Indicators | Example |
|-----------|-----------|---------|
| Low | Multiple T1 audits + time in production + bug bounty + formal verification | Uniswap v3, Aave v3 |
| Medium | 1–2 audits by reputable firms, significant time in production without major exploit | Curve v2, Compound |
| High | Single audit or unrecognized auditor, novel untested mechanism, <6 months old | Most new protocols |
| Critical | No audit, admin keys upgradeable without timelock, anonymous team, no bug bounty | AVOID |

#### Audit Firm Reputation Tiers
| Tier | Firms | Notes |
|------|-------|-------|
| Tier 1 | Trail of Bits, OpenZeppelin, Consensys Diligence | Highest rigor and track record |
| Tier 2 | Sherlock, Spearbit, Code4rena contests | Strong competitive audit models |
| Tier 3 | Certik (verify findings independently), PeckShield | Prolific but variable quality |
| Unrecognized | Unknown firms | Treat as unaudited |

#### DeFi Exploit History Reference (Major Events)
| Date | Protocol | Loss | Attack Type | Lesson |
|------|---------|------|------------|-------|
| 2022-11 | FTX (CeFi, not DeFi) | ~$8B | Fraud / misuse of customer funds | CeFi counterparty risk |
| 2022-05 | Terra/LUNA UST | ~$40B | Algorithmic stablecoin death spiral | Reflexivity in token design |
| 2022-10 | BNB Bridge | $566M | Bridge exploit | Cross-chain bridge risk |
| 2022-02 | Wormhole | $320M | Signature verification bug | Smart contract complexity risk |
| 2021-08 | Poly Network | $611M | Access control bug | Admin key risk |
| 2020-02 | bZx | $954K | Flash loan oracle manipulation | Oracle manipulation risk |

Source: Rekt.news (https://rekt.news/leaderboard/)

### 5. Sentiment & Behavioral Finance Framework

#### Sentiment Indicators
| Indicator | Source | Interpretation |
|-----------|--------|---------------|
| Fear & Greed Index | alternative.me | 0–24: Extreme Fear (buy signal) / 75–100: Extreme Greed (sell signal) |
| Bitcoin Funding Rates | Coinglass, Bybit | Positive = leveraged longs dominant (overextension risk) |
| Google Trends "Bitcoin" | trends.google.com | Spike = retail FOMO entering = often near-term top |
| Reddit Sentiment | r/CryptoCurrency | Useful as contrarian indicator at extremes |
| Developer Activity | GitHub commits | Consistent activity = long-term health signal |

#### Cognitive Biases in Crypto Trading
| Bias | How It Manifests in Crypto | Countermeasure in This Skill |
|------|---------------------------|----------------------------|
| FOMO | Buying ATHs driven by social media | On-chain valuation check (MVRV) before entry signal |
| Recency Bias | "Crypto is dead" after bear market | Historical cycle analysis |
| Confirmation Bias | Only reading bull-case content | Explicit devil's advocate / bear case requirement |
| Narrative Fallacy | Price story without data | Evidence tiering requirement (T1/T2 before T4/T5) |
| Anchoring | "BTC must go back to $69K" | Realized price / on-chain valuation anchoring instead |

---

## Key Research Papers

| Title | Authors | Year | Venue | DOI/Link | Relevance |
|-------|---------|------|-------|----------|-----------|
| Bitcoin: A Peer-to-Peer Electronic Cash System | Nakamoto, S. | 2008 | Whitepaper | [bitcoin.org/bitcoin.pdf](https://bitcoin.org/bitcoin.pdf) | Foundational Bitcoin whitepaper |
| Ethereum Yellow Paper | Wood, G. | 2014 | Tech Report | [ethereum.github.io/yellowpaper](https://ethereum.github.io/yellowpaper/paper.pdf) | Foundational Ethereum spec and EVM |
| Flash Boys 2.0: Frontrunning in Decentralized Exchanges | Daian, P. et al. | 2019 | IEEE S&P | [arxiv:1904.05234](https://arxiv.org/abs/1904.05234) | MEV and front-running in DeFi |
| DeFi and the Future of Finance | Harvey, C. et al. | 2021 | Duke/Fuqua | [arxiv:2106.08157](https://arxiv.org/abs/2106.08157) | Comprehensive DeFi survey and analysis |
| SoK: Decentralized Finance (DeFi) | Werner, S. et al. | 2022 | ACM CCS | [arxiv:2101.08778](https://arxiv.org/abs/2101.08778) | Systematic literature review of DeFi protocols |
| Automated Market Makers: Mean, Variance, and Fees | Cartea, Á. et al. | 2022 | Oxford | [arxiv:2205.15891](https://arxiv.org/abs/2205.15891) | AMM pricing mechanics and impermanent loss |
| Tokenomics: Dynamic Adoption and Valuation | Cong, L. et al. | 2021 | NBER | [NBER w26532](https://www.nber.org/papers/w26532) | Token pricing and adoption models |
| Are Cryptocurrency Markets Efficient? | Urquhart, A. | 2016 | Economics Letters | [doi:10.1016/j.econlet.2016.09.019](https://doi.org/10.1016/j.econlet.2016.09.019) | Crypto market efficiency analysis |
| Decentralized Finance: On Blockchain-Based Financial Markets | Schär, F. | 2021 | FRB St. Louis Review | [doi:10.20955/r.103.153-74](https://doi.org/10.20955/r.103.153-74) | Academic overview of DeFi ecosystem |
| Stablecoins: Risks, Potential and Regulation | BIS | 2021 | BIS Bulletin 52 | [bis.org/publ/bisbull52.pdf](https://www.bis.org/publ/bisbull52.pdf) | Regulatory perspective on stablecoins |
| On the Impossibility of Fully Decentralized Governance | Barbereau, T. et al. | 2023 | ArXiv | [arxiv:2209.07655](https://arxiv.org/abs/2209.07655) | DAO governance limitations research |
| Cryptoassets: The Innovative Investor's Guide | Burniske, C. & Tatar, J. | 2017 | Book | [Amazon](https://www.amazon.com/Cryptoassets-Innovative-Investors-Bitcoin-Beyond/dp/1260026671) | Foundational cryptoasset valuation framework |
| The Economics of Initial Coin Offerings | Catalini, C. & Gans, J.S. | 2018 | NBER | [NBER w24418](https://www.nber.org/papers/w24418) | ICO mechanism design and token economics |
| Blockchain and Cryptocurrency Regulation | Zetzsche, D. et al. | 2020 | Georgetown J. Int'l Law | [SSRN:3251001](https://ssrn.com/abstract=3251001) | Cross-jurisdictional regulatory analysis |

---

## State-of-the-Art Methods & Tools

### On-Chain Data Providers
| Provider | Asset Coverage | Free Tier | Key Unique Metrics | URL |
|---------|--------------|---------|-------------------|-----|
| Glassnode | BTC, ETH, 30+ assets | Limited (most metrics paywalled) | MVRV, SOPR, HODL waves, exchange flows | glassnode.com |
| Dune Analytics | All EVM chains | Yes — community dashboards | Custom SQL on raw chain data | dune.com |
| Nansen | ETH + EVM chains | Paid | Smart money wallet labeling | nansen.ai |
| Arkham Intelligence | Multi-chain | Freemium | Entity identification, fund tracking | arkhamintelligence.com |
| Token Terminal | Multi-chain protocols | Freemium | Revenue, P/S, P/F, fees data | tokenterminal.com |
| DeFiLlama | All DeFi chains | Free | TVL, yield, revenue, protocol comparisons | defillama.com |
| Woobull Charts | Bitcoin | Free | NVT, Mayer Multiple, MVRV | woobull.com |
| CryptoQuant | BTC, ETH | Freemium | Exchange inflows, miner metrics | cryptoquant.com |
| IntoTheBlock | Multi-chain | Freemium | Holder analytics, large transactions | intotheblock.com |

### Market Data APIs
| Provider | Token Coverage | Free Tier | Rate Limit | URL |
|---------|--------------|---------|-----------|-----|
| CoinGecko API | 10,000+ tokens | Yes | 150 calls/min | coingecko.com/en/api |
| CoinMarketCap API | 9,000+ tokens | Yes (limited endpoints) | 333 calls/day free | coinmarketcap.com/api |
| Messari API | 1,500+ tokens | Limited free | Paid for bulk | messari.io/api |
| Binance API | Spot + futures | Yes | 1,200 requests/min | binance.com/en/binance-api |
| CryptoCompare | 5,000+ assets | Freemium | 100 calls/min free | cryptocompare.com/api |

### DeFi-Specific Analytics
| Tool | Purpose | Key Feature | URL |
|------|---------|------------|-----|
| DeFiLlama | TVL aggregation | Cross-chain protocol comparison | defillama.com |
| DeBank | Portfolio + positions | DeFi position tracking across wallets | debank.com |
| L2Beat | Layer 2 assessment | Security risk ratings for L2s | l2beat.com |
| Immunefi | Bug bounty database | Protocol bug bounty amounts | immunefi.com |
| Rekt.news | Exploit history | Comprehensive DeFi hack database | rekt.news |
| Token Unlocks | Vesting schedules | Upcoming unlock events | token.unlocks.app |

### Sentiment & Social Analytics
| Tool | Signal Type | Key Use | URL |
|------|-----------|---------|-----|
| Alternative.me Fear & Greed | Composite sentiment | Market cycle extremes | alternative.me/crypto |
| Santiment | Social volume + dev activity | Narrative momentum | santiment.net |
| LunarCrush | Social engagement | Token-specific sentiment score | lunarcrush.com |
| Google Trends | Search volume | Retail interest proxy | trends.google.com |
| Coinglass | Funding rates + open interest | Leverage / positioning data | coinglass.com |

---

## Authoritative Data Sources

### Price & Market Data
- CoinGecko: https://www.coingecko.com — primary market data, supply, historical price
- CoinMarketCap: https://coinmarketcap.com — market cap rankings, token info
- TradingView: https://tradingview.com — charting, technical analysis, community scripts

### On-Chain Analytics
- Glassnode Insights (free articles): https://insights.glassnode.com
- Dune Analytics (community dashboards): https://dune.com
- Token Terminal (fundamentals): https://tokenterminal.com
- CryptoQuant: https://cryptoquant.com
- Woobull Charts: https://woobull.com

### DeFi Data
- DeFiLlama: https://defillama.com — TVL, yield, revenue, chain comparisons
- L2Beat: https://l2beat.com — Layer 2 security and TVL
- DeBank: https://debank.com — DeFi portfolio analytics
- Rekt.news: https://rekt.news — exploit history and post-mortems
- Immunefi: https://immunefi.com — bug bounty amounts and project security commitments
- Token Unlocks: https://token.unlocks.app — vesting schedules

### Research & News
- CoinDesk Research: https://www.coindesk.com/research
- The Block Research: https://www.theblock.co/research
- Messari Research: https://messari.io/research
- Blockworks Research: https://blockworks.co/research
- Decrypt: https://decrypt.co
- Cointelegraph: https://cointelegraph.com

### Regulatory Sources
- SEC Crypto: https://www.sec.gov/spotlight/cybersecurity-and-cryptoassets.shtml
- CFTC Digital Assets: https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/index.htm
- EU MiCA (ESMA): https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica
- FSB Crypto: https://www.fsb.org/work-of-the-fsb/financial-innovation-and-structural-change/crypto-assets/
- BIS Crypto Research: https://www.bis.org/topics/cryptoassets.htm
- MAS Singapore: https://www.mas.gov.sg/regulation/digital-payment-tokens
- FCA UK Crypto: https://www.fca.org.uk/consumers/cryptoassets

### Academic Repositories
- ArXiv cs.CR: https://arxiv.org/list/cs.CR/recent — cryptography and security
- ArXiv q-fin.TR: https://arxiv.org/list/q-fin.TR/recent — trading and market microstructure
- SSRN Crypto: https://papers.ssrn.com/sol3/JELJOUR_Results.cfm?form_name=journalbrowse&journal_id=3638 — social science research
- NBER Crypto Papers: https://www.nber.org/search?q=cryptocurrency

---

## Analytical Frameworks (From Skill 7 Research-First-Reasoning)

The following Skill 7 analytical methods are most applicable to crypto market analysis:

| Group | Method | How It Applies to Crypto |
|-------|--------|--------------------------|
| Quantitative | Base Rate Analysis | Historical MVRV ranges for bear bottoms and bull tops; halving cycle return distributions |
| Quantitative | Regression to Mean | Price vs. realized price convergence; NVT reversion to historical mean |
| Quantitative | Bayesian Updating | Update price probability distribution as new on-chain data arrives |
| Quantitative | Statistical Process Control | Flag anomalies in exchange flow data (sudden large deviations from baseline) |
| Risk Analysis | Scenario Analysis | Bull/Base/Bear cases with quantified probabilities for each investment decision |
| Risk Analysis | Pre-mortem Analysis | "Assume this investment fails — what specifically caused it?" (forces bear case rigor) |
| Risk Analysis | Risk-adjusted Return | Sharpe ratio, Sortino ratio applied to crypto portfolio construction |
| Risk Analysis | Failure Mode Analysis | Smart contract risks, tokenomics failure modes, regulatory shutdowns |
| Critical Thinking | Devil's Advocate | Challenge the bull thesis with the strongest counter-evidence available |
| Critical Thinking | Falsification | "What single piece of evidence would disprove this investment thesis?" |
| Critical Thinking | Steelmanning | Build the strongest possible version of the opposing view before rebutting it |
| Systems Thinking | Feedback Loop Mapping | Narrative → adoption → price → narrative → more FOMO (positive feedback loops) |
| Systems Thinking | Second-Order Effects | ETF approval → institutional inflows → who exits → what replaces them |
| Research | Citation Chaining | One on-chain anomaly → find academic precedent → find regulatory context |
| Research | Cross-Domain Analogies | Compare DeFi bank runs to traditional bank runs (Diamond-Dybvig model) |

---

## Self-Update Protocol

### Crawl Configuration
```yaml
schedule: Weekly (every Sunday 02:00 UTC recommended)
script: tools/knowledge_updater.py
runner: python tools/knowledge_updater.py

sources:
  arxiv:
    base_url: https://export.arxiv.org/api/query
    categories:
      - cs.CR    # cryptography and computer security
      - econ.GN  # general economics
      - q-fin.TR # trading and market microstructure
      - q-fin.RM # risk management
      - cs.CE    # computational engineering and finance
    queries:
      - "cryptocurrency bitcoin blockchain"
      - "DeFi decentralized finance yield"
      - "tokenomics cryptoasset token economics"
      - "on-chain analytics bitcoin ethereum"
      - "cryptocurrency market microstructure"
      - "stablecoin mechanism design"
      - "crypto regulation compliance"
      - "zero knowledge proof layer2 zkp"
    max_results_per_query: 10
    sort_by: submittedDate
    sort_order: descending

  web_sources:
    - name: CoinDesk Research
      url: https://www.coindesk.com/research/
      type: news
    - name: Glassnode Insights
      url: https://insights.glassnode.com/
      type: onchain
    - name: DeFiLlama Blog
      url: https://defillama.com/blog
      type: defi
    - name: BIS Crypto Reports
      url: https://www.bis.org/topics/cryptoassets.htm
      type: regulatory
    - name: Token Terminal Insights
      url: https://tokenterminal.com/resources
      type: analytics
    - name: The Block Research
      url: https://www.theblock.co/research
      type: news

deduplication:
  method: MD5 hash of URL or DOI
  state_file: tools/crawler_state.json
  
relevance_scoring:
  keywords: [bitcoin, ethereum, defi, tokenomics, on-chain, blockchain, cryptocurrency, 
             crypto, layer2, zk-proof, stablecoin, mvrv, nvt, exchange flow, whale, 
             validator, consensus, smart contract, protocol, tvl, yield, liquidity, amm]
  min_score: 2  # minimum keyword matches to include

limits:
  max_papers_per_run: 20
  max_articles_per_source: 3
  max_sources_per_run: 6
```

### Append Format
Each weekly update appends a standardized block:
```markdown
---
## Knowledge Update — YYYY-MM-DD

### New Research Papers
| Title | Authors | Year | Venue | DOI/Link | Relevance |
|-------|---------|------|-------|----------|-----------|
| [title] | [authors] | [year] | [venue] | [[id](url)] | [relevance note] |

### New Web Sources & Reports
- **[[title](url)]** (Source Name, YYYY-MM-DD) — [summary]

_Entries added: N | Run timestamp: ISO-8601_
```

### Graceful Degradation
When crawl4ai is unavailable (`pip install crawl4ai` required):
1. Seed papers from `_fallback_arxiv_papers()` are returned (3 foundational papers)
2. Web source crawl is skipped
3. Console message: "crawl4ai not installed — using seed papers only"
4. In skill output: "Live data unavailable — using internal knowledge base as of 2026-06-04"

---

## Knowledge Update Log

| Date | Papers Added | Articles Added | Notes |
|------|-------------|---------------|-------|
| 2026-06-04 | 0 (seed) | 0 (seed) | Initial file creation — 14 foundational papers pre-seeded above |

_Next scheduled update: 2026-06-11 (weekly cadence)_
