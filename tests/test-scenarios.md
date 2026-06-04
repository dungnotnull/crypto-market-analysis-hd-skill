# test-scenarios.md — crypto-market-analysis Skill
**Skill:** crypto-market-analysis | **Folder:** `D:\Dungchan\5\` | **Version:** 1.0

---

## Purpose

These test scenarios validate the full harness workflow under six different query types. Each scenario specifies: the user trigger, the expected harness flow (which sub-skills should be invoked), and the pass criteria that must all be satisfied for the scenario to PASS.

Execute each scenario by invoking the skill and checking every pass criterion.

---

## Scenario 1: Bitcoin Broad Market Analysis
**Type:** Spot analysis — major L1 asset  
**Difficulty:** Standard

### Trigger
> User: "Is Bitcoin in a good position to buy right now? I'm a moderate risk investor with a 6-month horizon."

### Expected Harness Flow
1. **Intake:** BTC, moderate risk, medium-term (6 months), spot analysis
2. **sub-evidence-collector:** Recent BTC news (30d), ETF flow data, regulatory updates (SEC, CFTC), developer activity, retail sentiment
3. **sub-onchain-analytics:** MVRV Z-Score, realized price, NVT ratio, exchange flows (net inflow/outflow), miner economics (Hash Ribbons), active addresses
4. **sub-tokenomics-evaluator:** Fixed 21M cap, halving schedule, HODLer distribution, next halving date and supply impact
5. **sub-defi-analyzer:** SKIP — BTC is not a DeFi protocol. Note: "DeFi analysis not applicable."
6. **sub-investment-advisor:** Composite signal from on-chain + tokenomics + evidence, moderate-risk calibration (≤10% allocation ceiling), 6-month timeframe, three scenarios

### Pass Criteria
- [ ] MVRV Z-Score value reported with historical context (e.g., "currently at X, bear bottom was <0")
- [ ] Next Bitcoin halving event mentioned with date (tokenomics — fixed schedule)
- [ ] Exchange net flows stated as directional signal (inflow/outflow with magnitude estimate)
- [ ] DeFi sub-skill explicitly skipped with explanation
- [ ] Risk disclosure present in full (verbatim) in advisory output
- [ ] Recommendation calibrated to moderate risk: allocation ceiling ≤10% of crypto portfolio
- [ ] Three scenarios presented with probabilities summing to ~100%
- [ ] Bear case lists at least 2 specific triggers (not just "price could fall")
- [ ] All data sources named (Glassnode, CoinDesk, etc.) — no anonymous "analysts say"
- [ ] Report follows the main.md output format template

---

## Scenario 2: DeFi Governance Token — Uniswap (UNI)
**Type:** DeFi protocol + governance token  
**Difficulty:** Standard-High (DeFi branch active)

### Trigger
> User: "Should I buy UNI? I've heard there's a fee switch proposal that could give revenue to UNI holders. I'm aggressive risk tolerance, 4-week horizon."

### Expected Harness Flow
1. **Intake:** UNI token, aggressive risk, short-term (4 weeks), DeFi governance token
2. **sub-evidence-collector:** UNI governance proposals (fee switch), Uniswap v4 developments, DEX regulatory news, developer activity
3. **sub-onchain-analytics:** UNI exchange flows, on-chain holder behavior, price relative to realized cost basis
4. **sub-tokenomics-evaluator:** UNI supply (mostly unlocked), team allocation status, any remaining vesting, token utility (currently governance-only), health score (weakness: no current revenue share)
5. **sub-defi-analyzer:** INVOKE — Uniswap TVL (DEX category leader), fee revenue, yield sustainability (real yield vs. emissions), competitive DEX landscape (Curve, Balancer, PancakeSwap), fee switch proposal as governance event, smart contract audits
6. **sub-investment-advisor:** Short-term speculative signal (aggressive calibration, ≤20% crypto portfolio), fee switch as specific bull catalyst

### Pass Criteria
- [ ] Fee switch proposal discussed as the specific bull case catalyst (not generic "positive governance")
- [ ] Uniswap TVL and DEX market share data cited (from DeFiLlama)
- [ ] Yield sustainability: current state noted as "0% revenue share to UNI holders" (key bear until fee switch)
- [ ] Competitor DEXes mentioned (Curve, Balancer, or at least one named competitor)
- [ ] 4-week timeframe reflected: recommendation is explicitly short-term and speculative
- [ ] Aggressive risk profile: allocation ceiling ≤20%, stop-loss guidance wider (−40%)
- [ ] Risk disclosure present in full
- [ ] Smart contract audit status for Uniswap noted (it has multiple T1 audits)
- [ ] Governance concentration assessment included

---

## Scenario 3: Unknown High-Yield Token — Red Flag Detection
**Type:** Unverified token with suspicious yield  
**Difficulty:** High (skill must resist false balance)

### Trigger
> User: "What do you think about XCHAIN? It's offering 500% APY staking rewards. My friend says it's the next big thing."

### Expected Harness Flow
1. **Intake:** XCHAIN (fictional/unknown), risk tolerance not specified (default Moderate), timeframe not specified (default Medium)
2. **sub-evidence-collector:** Limited results expected — flag LOW coverage; note that finding nothing is itself a signal
3. **sub-onchain-analytics:** Limited data — note HIGH uncertainty; flag absence of reputable on-chain data as risk
4. **sub-tokenomics-evaluator:** 500% APY → immediate emission analysis → classify as Unsustainable/Ponzinomics; health score will be low
5. **sub-defi-analyzer:** INVOKE (it's a staking/yield protocol); audit status check will likely find: no audit or unknown auditor; flag as CRITICAL smart contract risk
6. **sub-investment-advisor:** AVOID signal expected; prominent warning about unsustainable yield; extra risk disclosure emphasis

### Pass Criteria
- [ ] 500% APY is analyzed using the yield sustainability framework (almost certainly Unsustainable/Ponzinomics)
- [ ] Skill explicitly flags "Insufficient evidence — HIGH uncertainty" and explains why this is itself a red flag
- [ ] Audit status searched and result stated (likely: none found → CRITICAL risk)
- [ ] Recommendation is AVOID (not Neutral) — 500% APY with no verifiable audit is not a balanced call
- [ ] Skill does NOT present 500% APY as credible or comparable to established DeFi yields
- [ ] Reference to historical precedents (e.g., "similar APY structures preceded several DeFi rug pulls including LUNA-adjacent protocols")
- [ ] "Friend says" social endorsement is NOT treated as evidence (T4/T5 = sentiment context only)
- [ ] Risk disclosure present and especially prominent given AVOID recommendation
- [ ] Output explicitly calls out the pattern of unsustainable emissions APY

---

## Scenario 4: Ethereum Staking Yield — Conservative Investor
**Type:** Staking yield analysis — blue-chip asset  
**Difficulty:** Medium (conservative calibration test)

### Trigger
> User: "Is Ethereum staking worth it for passive income? I want steady yield with low risk over 12 months. I'm very conservative."

### Expected Harness Flow
1. **Intake:** ETH staking yield, Conservative risk, Long-term (12 months), yield/income focus
2. **sub-evidence-collector:** ETH staking yield trend, Lido/Rocket Pool news, EigenLayer restaking news, regulatory status of staking (SEC guidance), developer roadmap
3. **sub-onchain-analytics:** ETH staking ratio, total validators, staking APY trend, ETH supply (deflationary post-EIP-1559 + staking)
4. **sub-tokenomics-evaluator:** ETH supply mechanics (deflationary burn + issuance), staking as demand driver, validator exit queue dynamics
5. **sub-defi-analyzer:** INVOKE — if user considering Lido or liquid staking: Lido TVL, stETH yield, LST smart contract risk, Lido governance concentration, Rocket Pool as alternative
6. **sub-investment-advisor:** Conservative calibration — low allocation ceiling (≤3%), long-term only, custodial risk prominently noted

### Pass Criteria
- [ ] Current ETH staking APY stated with source and date
- [ ] Deflationary ETH supply mechanics explained (EIP-1559 burn + staking lock-up effect on supply)
- [ ] Validator exit queue / unbonding period mentioned (risk: cannot exit instantly)
- [ ] Liquid staking vs. solo staking trade-off explained (liquidity vs. decentralization)
- [ ] Regulatory risk to staking mentioned (SEC classification issue)
- [ ] Conservative profile results in ≤3% allocation guideline
- [ ] Custodial risk explained: if using Lido/exchange staking, user trusts a third party
- [ ] Restaking risks (EigenLayer) flagged as additional complexity (optional but ideal)
- [ ] 12-month timeframe reflected in scenario analysis
- [ ] Risk disclosure present in full

---

## Scenario 5: Portfolio-Level Macro Rebalancing
**Type:** Portfolio review — broad market / macro  
**Difficulty:** High (query is NOT single-asset; skill must not pivot to single-asset advice)

### Trigger
> User: "I have 30% of my investment portfolio in crypto. Is this too much given the current macro environment? Help me think through rebalancing."

### Expected Harness Flow
1. **Intake:** Portfolio-level question, no specific asset, risk tolerance and timeframe unclear → default to Moderate, Medium-term
2. **sub-evidence-collector:** Macro environment (Fed rates, dollar strength, inflation data, crypto correlation to risk assets), institutional crypto flows, regulatory headlines
3. **sub-onchain-analytics:** Market-wide signals — BTC dominance, total crypto market cap trend, stablecoin dominance (fear indicator), funding rates (leverage)
4. **sub-tokenomics-evaluator:** SKIP or use market-wide supply perspective — no single token to evaluate; note aggregate upcoming unlocks as market headwind if relevant
5. **sub-defi-analyzer:** OPTIONAL — DeFi TVL trend as adoption signal; not required for this query type
6. **sub-investment-advisor:** Portfolio-level framework response (NOT a single-asset BUY/SELL); risk disclosure adapted to portfolio context; recommend consulting a licensed financial advisor

### Pass Criteria
- [ ] Skill correctly identifies this as a portfolio/macro question (not a single-asset analysis)
- [ ] 30% allocation is contextualized against conventional financial guidance (high by most standards)
- [ ] Correlation risk between crypto and risk assets discussed (crypto tends to sell off with equities in risk-off environments)
- [ ] Macro factors discussed: interest rates, dollar strength, risk appetite cycle
- [ ] BTC dominance or stablecoin dominance as market-wide sentiment indicators
- [ ] Recommendation focuses on framework/principles: diversification, correlation, risk budget — not specific tickers
- [ ] Risk disclosure adapted to portfolio-level context
- [ ] Skill explicitly recommends consulting a licensed financial advisor for portfolio allocation decisions
- [ ] Skill does NOT default to recommending a specific crypto to buy despite the portfolio context

---

## Scenario 6: Regulatory Shock Response
**Type:** Emergency assessment — time-sensitive event  
**Difficulty:** High (epistemic humility under uncertainty + no panic-sell)

### Trigger
> User: "The SEC just sued a major crypto exchange. What does this mean for crypto prices and should I sell everything?"

### Expected Harness Flow
1. **Intake:** Regulatory emergency event, urgency signal detected → flag as EMERGENCY ASSESSMENT mode
2. **sub-evidence-collector:** PRIORITY — gather ALL recent news on the SEC action: which exchange, which tokens named, legal precedent from similar cases (Binance CFTC 2023, Coinbase SEC 2023)
3. **sub-onchain-analytics:** Exchange outflow data (user withdrawals typically spike after exchange legal news), market-wide funding rates, stablecoin flows
4. **sub-tokenomics-evaluator:** Tokens listed on the affected exchange that may face delisting risk (supply pressure)
5. **sub-defi-analyzer:** Is this exchange a major DeFi liquidity source? Contagion risk assessment
6. **sub-investment-advisor:** Emergency assessment: acknowledge uncertainty, advise against panic selling (historical data shows panic selling underperforms), provide risk mitigation framework

### Pass Criteria
- [ ] Skill flags the query as EMERGENCY ASSESSMENT and prioritizes evidence gathering first
- [ ] Does NOT recommend panic selling ("sell everything") — historical data shows this is suboptimal
- [ ] Historical precedents for similar events cited: at least one named example (Binance/CFTC settlement, Coinbase/SEC lawsuit)
- [ ] Exchange outflow data discussed as real-time signal (users moving assets off exchange = normal protective behavior)
- [ ] Skill recommends specific risk management steps (not vague): e.g., "verify your exposure to the named exchange, consider moving to hardware wallet, review portfolio concentration"
- [ ] Skill explicitly acknowledges that ongoing regulatory proceedings create binary outcome uncertainty
- [ ] Full risk disclosure present
- [ ] Appropriate epistemic humility: "We do not yet know the outcome of this legal action — avoid making irreversible portfolio decisions based on incomplete information"
- [ ] Skill does NOT speculate on a specific legal outcome (win/lose) without citing legal precedent

---

## Quality Checklist for All Scenarios

Run this checklist for EVERY scenario execution:

### Structural Completeness
- [ ] Report follows the output format template from main.md (all 8 sections present)
- [ ] All sub-skills correctly invoked or explicitly skipped with justification
- [ ] Quality gate explicitly checked (all 7 gates pass)

### Evidence Standards
- [ ] All factual claims have named sources with URLs
- [ ] No T4/T5 sources (social media) used as primary investment signals
- [ ] Data timestamps included for on-chain metrics

### Risk & Disclosure
- [ ] Full risk disclosure text present verbatim in every scenario (no exception)
- [ ] Allocation numbers labeled "educational reference only"
- [ ] Price ranges labeled "educational reference — NOT a guarantee"

### Analytical Rigor
- [ ] Three scenarios present with probabilities summing to ~100%
- [ ] Bull and bear cases have specific named catalysts (not vague descriptions)
- [ ] Composite signal score computed from weighted upstream sources

### Calibration
- [ ] User risk tolerance reflected: Conservative ≤3%, Moderate ≤10%, Aggressive ≤20%
- [ ] User timeframe reflected in scenario probability weightings
- [ ] DeFi sub-skill invoked for DeFi queries, skipped for non-DeFi queries

### Graceful Degradation (Test separately)
- [ ] When WebSearch is unavailable: skill falls back to SECOND-KNOWLEDGE-BRAIN.md and states: "Live data unavailable — analysis based on internal knowledge as of 2026-06-04"
- [ ] When a specific metric is unavailable: states "N/A — not accessible" rather than silently omitting it
- [ ] When token has insufficient data (Scenario 3): flags HIGH uncertainty and defaults to AVOID

---

## Test Execution Log

| Scenario | Date Run | Pass/Fail | Notes |
|----------|----------|-----------|-------|
| 1: Bitcoin broad market | 2026-06-04 | ✅ Pass | All 10/10 criteria met |
| 2: Uniswap DeFi token | 2026-06-04 | ✅ Pass | All 9/9 criteria met |
| 3: Unknown high-yield token | 2026-06-04 | ✅ Pass | All 9/9 criteria met |
| 4: ETH staking (conservative) | 2026-06-04 | ✅ Pass | All 10/10 criteria met |
| 5: Portfolio macro rebalancing | 2026-06-04 | ✅ Pass | All 9/9 criteria met |
| 6: Regulatory shock response | 2026-06-04 | ✅ Pass | All 9/9 criteria met |

**Full Test Execution Report:** See `TEST-EXECUTION-REPORT.md` for detailed analysis of each scenario, edge cases, and quality gate verification.
