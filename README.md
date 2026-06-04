# 🪙 CryptoMarket Analysis — Professional Cryptocurrency Research Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-orange.svg)](https://claude.com/claude-code)
[![Status: Production Ready](https://img.shields.io/badge/Status-Production_Success-green.svg)]()

> A professional-grade cryptocurrency research harness for Claude Code — combining on-chain analytics, tokenomics evaluation, DeFi protocol analysis, and evidence-based investment advisory with mandatory risk disclosure.

---

## 🎯 Overview

**CryptoMarket Analysis** is a sophisticated Claude Code skill that transforms how you research and analyze cryptocurrencies. Unlike simple chatbot responses, this skill orchestrates a multi-stage research pipeline that mirrors professional crypto analyst workflows.

### What It Does

- **On-Chain Analytics**: MVRV Z-Score, NVT ratio, exchange flows, whale tracking, miner/validator economics
- **Tokenomics Evaluation**: Supply schedules, vesting cliffs, holder concentration, utility assessment, health scoring
- **DeFi Protocol Analysis**: TVL trends, yield sustainability, smart contract risk, audit verification, governance health
- **Evidence Aggregation**: Tiered source system (T1-T5), regulatory intelligence, developer activity tracking
- **Investment Advisory**: Weighted signal synthesis, three-scenario analysis, risk-calibrated recommendations

### What Makes It Different

| Feature | Typical AI Response | CryptoMarket Analysis |
|---------|---------------------|------------------------|
| **Evidence Sourcing** | "Analysts say..." | Every claim cites specific source with URL and timestamp |
| **Risk Disclosure** | Optional or omitted | **MANDATORY** — full disclosure in every output |
| **Scenario Analysis** | Single directional call | Bull/Base/Bear with specific catalysts and probabilities |
| **DeFi Intelligence** | Generic optimism | Real yield vs emissions yield, audit tiers, exploit history |
| **Red Flag Detection** | False balance ("consider both sides") | AVOID signal for unsustainable yields with zero credible audits |

---

## 🏗️ Architecture

### Harness Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                     CRYPTO MARKET ANALYSIS SKILL                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  Stage 0: INTAKE & QUERY PARSING                                     │
│  ├─ Extract: Asset, Timeframe, Risk Tolerance, Portfolio Context     │
│  └─ Emergency Mode Detection (regulatory shocks, panic queries)      │
│                              │                                        │
│                              ▼                                        │
│  Stage 1: EVIDENCE COLLECTION (sub-evidence-collector.md)            │
│  ├─ Tier 1: Academic papers (ArXiv, SSRN, NBER, BIS)                  │
│  ├─ Tier 2: Regulatory documents (SEC, CFTC, FSB, MiCA)               │
│  ├─ Tier 3: Crypto-native media (CoinDesk, The Block, Decrypt)        │
│  ├─ Tier 4: Social sentiment (Reddit, Twitter/X — context only)      │
│  └─ Tier 5: Opinion pieces (contextual only)                        │
│                              │                                        │
│                              ▼                                        │
│  Stage 2: ON-CHAIN ANALYTICS (sub-onchain-analytics.md)               │
│  ├─ Valuation: MVRV Z-Score, Realized Price, Mayer Multiple           │
│  ├─ Network: NVT Ratio, Active Addresses, Hash Rate                   │
│  ├─ Flows: Exchange Inflows/Outflows, Stablecoin Flows                │
│  ├─ Whales: Smart money tracking, large holder behavior               │
│  └─ Economics: Miner/Validator profitability, SOPR                    │
│                              │                                        │
│                              ▼                                        │
│  Stage 3: TOKENOMICS EVALUATION (sub-tokenomics-evaluator.md)         │
│  ├─ Supply Dynamics: Fixed vs inflationary, unlock calendar           │
│  ├─ Holder Distribution: Concentration analysis, HODLer metrics        │
│  ├─ Utility Assessment: Governance, staking, DeFi collateral          │
│  └─ Health Score: 5 dimensions, /25 total                             │
│                              │                                        │
│                              ▼                                        │
│  Stage 4: DEFI ANALYSIS (Conditional — sub-defi-analyzer.md)          │
│  ├─ Protocol Metrics: TVL, P/S ratio, fee revenue                    │
│  ├─ Yield Sustainability: Real yield vs emissions yield                │
│  ├─ Smart Contract Risk: Audit tiers, exploit history                 │
│  ├─ Governance: Token voting concentration, proposal activity         │
│  └─ Competitive Positioning: Market share vs alternatives             │
│                              │                                        │
│                              ▼                                        │
│  Stage 5: INVESTMENT ADVISORY (sub-investment-advisor.md)             │
│  ├─ Signal Aggregation: Weighted composite score (35/25/20/20%)       │
│  ├─ Scenario Analysis: Bull/Base/Bear with probabilities               │
│  ├─ Risk Calibration: Conservative ≤3%, Moderate ≤10%, Aggressive ≤20% │
│  ├─ Recommendation: Signal, timeframe, allocation, entry zone        │
│  └─ **MANDATORY**: Full risk disclosure verbatim                      │
│                              │                                        │
│                              ▼                                        │
│  Stage 6: QUALITY GATE (7 Gates)                                      │
│  ├─ G1: Citation completeness                                        │
│  ├─ G2: Risk disclosure present                                      │
│  ├─ G3: No certainty claims                                          │
│  ├─ G4: Data freshness                                               │
│  ├─ G5: Unlock review complete                                       │
│  ├─ G6: Bear case rigor                                              │
│  └─ G7: Risk calibration verified                                    │
│                              │                                        │
│                              ▼                                        │
│  Stage 7: FINAL REPORT DELIVERY                                        │
│  └─ Professional research artifact with all sections                  │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

### Sub-Skills

| Sub-Skill | File | Purpose |
|-----------|------|---------|
| **Evidence Collector** | `skills/sub-evidence-collector.md` | Multi-source research with T1-T5 tiering |
| **On-Chain Analytics** | `skills/sub-onchain-analytics.md` | Blockchain metrics interpretation |
| **Tokenomics Evaluator** | `skills/sub-tokenomics-evaluator.md` | Supply, vesting, utility, health scoring |
| **DeFi Analyzer** | `skills/sub-defi-analyzer.md` | Protocol TVL, yield, audit, governance |
| **Investment Advisor** | `skills/sub-investment-advisor.md` | Signal synthesis, scenarios, disclosure |

---

## 🚀 Installation

### Prerequisites

- **Claude Code** (desktop app or CLI) — [Get Claude Code](https://claude.com/claude-code)
- Git (for cloning the repository)

### Installation Steps

#### Option 1: Clone to Claude Skills Directory

```bash
# Navigate to your Claude skills directory
cd ~/.claude/skills/

# Clone the repository
git clone https://github.com/dungnotnull/crypto-market-analysis-hd-skill.git

# The skill will be available as /crypto-market-analysis in Claude Code
```

#### Option 2: Manual Installation

```bash
# Clone to any directory
git clone https://github.com/dungnotnull/crypto-market-analysis-hd-skill.git

# Create a symlink in your Claude skills directory
ln -s /path/to/crypto-market-analysis-hd-skill ~/.claude/skills/crypto-market-analysis
```

#### Optional: Python Dependencies

If you want to use the automatic knowledge updater:

```bash
cd crypto-market-analysis-hd-skill
pip install -r requirements.txt
```

---

## 📖 Usage

### Basic Usage

Once installed, invoke the skill in Claude Code:

```
/crypto-market-analysis
```

### Example Queries

#### Bitcoin Market Analysis

> "Is Bitcoin in a good position to buy right now? I'm a moderate risk investor with a 6-month horizon."

**Output includes:**
- MVRV Z-Score with historical context
- Exchange net flow analysis
- Next halving date and supply impact
- Moderate-risk recommendation (≤10% allocation)
- Three scenarios (Bull/Base/Bear) with probabilities

#### DeFi Governance Token

> "Should I buy UNI? There's a fee switch proposal. I'm aggressive risk, 4-week horizon."

**Output includes:**
- Uniswap TVL and DEX market share
- Fee switch catalyst analysis
- Current revenue share (0% — bear case)
- Smart contract audit status
- Aggressive-risk recommendation (≤20% allocation)

#### Red Flag Detection

> "What do you think about XCHAIN? It's offering 500% APY staking rewards."

**Output includes:**
- Yield sustainability analysis (Unsustainable/Ponzinomics)
- Audit status check (likely: none found)
- **AVOID** signal (not false balance)
- Historical precedent warnings
- Emphasized risk disclosure

#### Emergency Assessment

> "The SEC just sued a major crypto exchange. Should I sell everything?"

**Output includes:**
- Emergency mode prioritization
- Historical precedents (Binance, Coinbase cases)
- Exchange outflow data
- **No panic-sell recommendation**
- Specific risk management steps
- Epistemic humility (uncertainty acknowledged)

---

## 🧪 Testing

The skill includes comprehensive test scenarios with pass criteria.

### Run Test Verification

```bash
# View test scenarios
cat tests/test-scenarios.md

# View test execution report
cat tests/TEST-EXECUTION-REPORT.md
```

### Test Coverage

| Scenario | Type | Status |
|----------|------|--------|
| Bitcoin Broad Market | Spot Analysis | ✅ Pass (10/10) |
| Uniswap DeFi Token | DeFi Governance | ✅ Pass (9/9) |
| Unknown High-Yield Token | Red Flag Detection | ✅ Pass (9/9) |
| ETH Staking (Conservative) | Conservative Calibration | ✅ Pass (10/10) |
| Portfolio Macro Rebalancing | Portfolio-Level | ✅ Pass (9/9) |
| Regulatory Shock Response | Emergency Mode | ✅ Pass (9/9) |

**Overall: 100% pass rate across all scenarios**

---

## 📊 Output Format

Each analysis produces a professional research report with the following sections:

```
# Crypto Research Report: [ASSET] ([TICKER])
**Date:** YYYY-MM-DD | **Confidence:** High/Medium/Low

---

## RISK DISCLOSURE
⚠️ Full mandatory disclosure text...

---

## 1. Asset Overview
Market cap, price, 24h/7d/30d changes, data timestamp

---

## 2. Evidence Summary
Tiered sources (T1-T5), regulatory status, developer activity, sentiment

---

## 3. On-Chain Analysis
Valuation metrics, exchange flows, network health, on-chain verdict

---

## 4. Tokenomics Analysis
Supply dynamics, unlock calendar, holder concentration, health score /25

---

## 5. DeFi / Protocol Analysis
TVL trend, yield sustainability, smart contract risk, governance
(Or: "DeFi analysis not applicable")

---

## 6. Scenario Analysis
| Scenario | Probability | Catalyst | Implication |
| Bull Case | 40% | Specific catalyst | Outcome |
| Base Case | 45% | Current trend | Outcome |
| Bear Case | 15% | Specific triggers | Outcome |

---

## 7. Investment Recommendation
Signal, timeframe, allocation ceiling, entry zone, stop-loss guidance

---

## 8. Sources & Citations
Numbered list with URLs and access dates
```

---

## 🛡️ Risk Disclosure

**This skill includes MANDATORY risk disclosure in every output.**

The full disclosure text:

> ⚠️ **IMPORTANT — READ BEFORE PROCEEDING:**
> This report is for **informational and educational purposes only**. It does NOT constitute financial advice, investment advice, trading advice, or a solicitation to buy or sell any asset. Cryptocurrency investments involve **extreme risk** including but not limited to: total loss of capital, extreme volatility (assets can drop 80–90% or more from peak), regulatory changes and enforcement actions, technological failures, smart contract exploits, market manipulation, and liquidity crises. Past performance does not predict future results. The analyst does not hold any regulatory license to provide financial advice. **Always consult a qualified, licensed financial advisor before making investment decisions. Only invest capital you can afford to lose entirely.**

---

## 🔧 Configuration

### Knowledge Base

The skill includes `SECOND-KNOWLEDGE-BRAIN.md` — a self-improving knowledge base seeded with:
- 12 foundational research papers
- Core concepts and frameworks
- Authoritative data sources directory
- Analytical frameworks adapted from research-first-reasoning

### Knowledge Updater (Optional)

```bash
# Run the knowledge updater to refresh from live sources
python tools/knowledge_updater.py

# This fetches from:
# - ArXiv (cs.CR, q-fin)
# - SSRN crypto papers
# - CoinDesk, Glassnode, DeFiLlama
# - BIS bulletins
```

---

## 🤝 Contributing

Contributions are welcome! Areas for contribution:

### High Priority
- [ ] Additional academic paper sources in knowledge base
- [ ] More regional regulatory sources (Asia, LATAM)
- [ ] Additional DeFi protocol coverage
- [ ] Test scenarios for edge cases

### Medium Priority
- [ ] Localization (non-English sources)
- [ ] Additional language models
- [ ] Performance optimizations

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Ensure all tests pass
5. Submit a pull request

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

**MIT License Summary:**
- ✅ Free to use for commercial and personal projects
- ✅ Free to modify and distribute
- ✅ No warranty provided
- ✅ License and copyright notice required

---

## 🙏 Acknowledgments

### Data Sources
- **Glassnode** — On-chain metrics and analytics
- **Dune Analytics** — Crypto data dashboards
- **DeFiLlama** — DeFi TVL and protocol metrics
- **CoinGecko / CoinMarketCap** — Market data
- **CoinDesk, The Block, Decrypt** — Crypto-native journalism
- **ArXiv, SSRN, NBER, BIS** — Academic and institutional research

### Regulatory Sources
- **SEC (USA)** — Securities and Exchange Commission
- **CFTC (USA)** — Commodity Futures Trading Commission
- **FSB (Global)** — Financial Stability Board
- **ESMA / MiCA (EU)** — European Securities and Markets Authority
- **MAS (Singapore)** — Monetary Authority of Singapore
- **FCA (UK)** — Financial Conduct Authority

### Inspired By
- Professional crypto analyst workflows at Glassnode, Messari, and Token Terminal
- Research-first reasoning methodology
- Evidence-based investment practices

---

## 📈 Roadmap

### Completed ✅
- [x] Phase 0: Research & Architecture
- [x] Phase 1: Core Sub-Skills (5 sub-skills)
- [x] Phase 2: Main Harness + Quality Gates
- [x] Phase 3: SECOND-KNOWLEDGE-BRAIN Pipeline
- [x] Phase 4: Testing & Validation (100% pass rate)

### In Progress 🔄
- [ ] Phase 5: Integration with research-first-reasoning skill

### Future 🚀
- [ ] Real-time data API integration
- [ ] Custom report templates
- [ ] Portfolio tracking mode
- [ ] Alert system for key events
- [ ] Multi-language support

---

## 📞 Support

### Documentation
- [PROJECT-detail.md](PROJECT-detail.md) — Full technical specification
- [PROJECT-DEVELOPMENT-PHASE-TRACKING.md](PROJECT-DEVELOPMENT-PHASE-TRACKING.md) — Development roadmap
- [CLAUDE.md](CLAUDE.md) — Project-specific Claude instructions

### Issues & Questions
- **GitHub Issues**: [Report bugs or request features](https://github.com/dungnotnull/crypto-market-analysis-hd-skill/issues)
- **Discussions**: [Ask questions or share ideas](https://github.com/dungnotnull/crypto-market-analysis-hd-skill/discussions)

### Community
- Star the repository if you find it useful ⭐
- Share your use cases in Discussions
- Contribute improvements via Pull Requests

---

## ⚠️ Disclaimer

**CRYPTOCURRENCY INVESTMENTS INVOLVE EXTREME RISK.**

This skill provides informational and educational content only. It does not constitute financial advice. Always:
- Consult a qualified, licensed financial advisor
- Only invest what you can afford to lose entirely
- Understand that cryptocurrencies can drop 80–90% in value
- Be aware of regulatory, technological, and market risks
- Recognize that past performance does not predict future results

**The authors and contributors of this skill are not responsible for any investment decisions you make.**

---

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=dungnotnull/crypto-market-analysis-hd-skill&type=Date)](https://star-history.com/#dungnotnull/crypto-market-analysis-hd-skill&Date)

---

**Made with ❤️ for the crypto community**

*Professional research meets AI-powered analysis*
