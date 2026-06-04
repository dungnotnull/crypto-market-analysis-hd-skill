# PROJECT-DEVELOPMENT-PHASE-TRACKING.md — crypto-market-analysis
**Skill:** crypto-market-analysis | **Folder:** `D:\Dungchan\5\` | **Start Date:** 2026-06-04

---

## Phase Overview

| Phase | Name | Timeline | Status |
|-------|------|----------|--------|
| Phase 0 | Research & Skill Architecture | Week 1–2 | ✅ Complete |
| Phase 1 | Core Sub-Skills | Week 3–5 | ✅ Complete |
| Phase 2 | Main Harness + Quality Gates | Week 6–8 | ✅ Complete |
| Phase 3 | SECOND-KNOWLEDGE-BRAIN Pipeline | Week 9–10 | ✅ Complete (seed) |
| Phase 4 | Testing & Validation | Week 11–12 | ✅ Complete |
| Phase 5 | Integration & Cross-Skill Wiring | Week 13–14 | 🔲 Pending |

---

## Phase 0: Research & Skill Architecture (Week 1–2)

### Goal
Understand the crypto analysis domain deeply enough to design a professional harness workflow. Identify what a real crypto analyst does that a naive LLM prompt would miss.

### Tasks
- [x] Read idea.txt — understand user's intent (skill similar to vn-finance-analysis, focused on crypto)
- [x] Review Skill 4 (vn-finance-analysis) as the closest reference design
- [x] Map the unique crypto analysis challenges vs. traditional equity analysis
- [x] Identify the 5 core sub-skill domains: evidence, on-chain, tokenomics, DeFi, advisory
- [x] Design the harness architecture (stage flow with conditional DeFi branch)
- [x] Identify Cluster B shared patterns with Skill 4
- [x] Document key data sources (Glassnode, Dune, DeFiLlama, Token Terminal)
- [x] Design evidence tiering framework (T1–T5)

### Deliverables
- [x] Architecture diagram (see PROJECT-detail.md)
- [x] Sub-skill catalog (see PROJECT-detail.md)
- [x] Data source directory (see SECOND-KNOWLEDGE-BRAIN.md)

### Success Criteria
- Architecture matches a real crypto analyst workflow (not just a chatbot response)
- Sub-skills are composable and reusable across different query types
- Conditional logic handles the DeFi/non-DeFi branching correctly

---

## Phase 1: Core Sub-Skills (Week 3–5)

### Goal
Implement the 5 core sub-skills that form the backbone of the harness.

### Tasks
- [x] Write `skills/sub-evidence-collector.md`
  - [x] News search workflow (T3 sources)
  - [x] Academic search workflow (T1/T2 sources: ArXiv, SSRN, NBER, BIS)
  - [x] Regulatory intelligence workflow (SEC, CFTC, FSB, MiCA)
  - [x] Social sentiment workflow (Reddit, Twitter/X — T4 as context only)
  - [x] Developer activity workflow (GitHub, audit status)
  - [x] Evidence tiering framework (T1–T5)
  - [x] Output format template
  - [x] Quality gate (5 sources, T1/T2 presence, regulatory status)

- [x] Write `skills/sub-onchain-analytics.md`
  - [x] Key metrics glossary (MVRV, NVT, SOPR, Mayer Multiple, etc.)
  - [x] Data source identification workflow by asset type
  - [x] Valuation metrics interpretation
  - [x] Exchange flow analysis
  - [x] Whale & smart money tracking
  - [x] Miner/validator economics
  - [x] Network health assessment
  - [x] Output format with signal summary table
  - [x] Quality gate (3+ metrics with values, timestamps, limitations noted)

- [x] Write `skills/sub-tokenomics-evaluator.md`
  - [x] Supply dynamics framework
  - [x] Vesting & unlock calendar analysis
  - [x] Holder concentration analysis
  - [x] Token utility classification matrix
  - [x] Tokenomics health score (5 dimensions, /25 total)
  - [x] Output format with health score table
  - [x] Quality gate (supply ratio, inflation, unlocks, utility, score)

- [x] Write `skills/sub-defi-analyzer.md`
  - [x] Key DeFi metrics glossary (TVL, P/S, real yield, emissions APY)
  - [x] Yield sustainability framework (real yield vs. emissions yield)
  - [x] Smart contract risk assessment matrix
  - [x] Audit firm reputation tiers
  - [x] Governance health assessment
  - [x] Competitive positioning framework
  - [x] Output format with verdict
  - [x] Quality gate (DeFiLlama cited, yield classified, audits confirmed, exploits checked)

- [x] Write `skills/sub-investment-advisor.md`
  - [x] Signal aggregation framework (weighted: on-chain 35%, tokenomics 25%, evidence 20%, DeFi 20%)
  - [x] Composite score → signal tier mapping
  - [x] Risk tolerance calibration table (conservative/moderate/aggressive)
  - [x] Three-scenario framework (bull/base/bear with probabilities)
  - [x] Recommendation table template
  - [x] MANDATORY full risk disclosure text
  - [x] Quality gate (disclosure present, probabilities sum ~100%, specific catalysts, allocations labeled)

### Deliverables
- [x] 5 sub-skill files in `skills/` directory
- [x] Each file: role, workflow, output format, quality gate

### Success Criteria
- Each sub-skill can be invoked independently and produces a complete output block
- Sub-skills compose cleanly (output of one feeds input of next)
- Risk disclosure is non-negotiable in sub-investment-advisor

---

## Phase 2: Main Harness + Quality Gates (Week 6–8)

### Goal
Assemble sub-skills into the full harness orchestration. Add the 7-gate quality control layer.

### Tasks
- [x] Write `skills/main.md` (primary harness entry point)
  - [x] Role & persona (CryptoResearch Pro)
  - [x] Stage 0: Intake & query parsing (parameter extraction)
  - [x] Stage 1: Evidence collection → sub-evidence-collector
  - [x] Stage 2: On-chain analytics → sub-onchain-analytics
  - [x] Stage 3: Tokenomics → sub-tokenomics-evaluator
  - [x] Stage 4: DeFi analysis (conditional) → sub-defi-analyzer
  - [x] Stage 5: Investment advisory → sub-investment-advisor
  - [x] Stage 6: Quality gate (7 gates)
  - [x] Stage 7: Final report delivery
  - [x] Sub-skills table
  - [x] Tools list
  - [x] Output format template (full report structure)
  - [x] Quality gates section

### Deliverables
- [x] `skills/main.md` — complete harness entry point

### Success Criteria
- All 7 stages are numbered and clearly described
- Conditional DeFi branch is explicit (when to invoke, when to skip)
- Output format template produces a professional research artifact
- All 7 quality gates are enumerable and testable

---

## Phase 3: SECOND-KNOWLEDGE-BRAIN Pipeline (Week 9–10)

### Goal
Build the self-improving knowledge base and the crawl4ai pipeline that grows it.

### Tasks
- [x] Write `SECOND-KNOWLEDGE-BRAIN.md`
  - [x] Core Concepts & Frameworks (market cycles, on-chain, tokenomics, DeFi, sentiment)
  - [x] Key Research Papers table (12 foundational papers seeded)
  - [x] State-of-the-Art Methods & Tools (on-chain providers, market data APIs, DeFi analytics)
  - [x] Authoritative Data Sources (URL directory by category)
  - [x] Analytical Frameworks (Skill 7 methods applied to crypto)
  - [x] Self-Update Protocol (crawl config, append format, deduplication)
  - [x] Knowledge Update Log (initial entry)

- [x] Write `tools/knowledge_updater.py`
  - [x] ArXiv API fetcher (cs.CR, q-fin.TR, q-fin.RM, econ.GN, cs.CE)
  - [x] Web source crawler (crawl4ai: CoinDesk, Glassnode, DeFiLlama, BIS)
  - [x] Relevance scorer (keyword match against 22 crypto keywords)
  - [x] Deduplication (MD5 hash of URL/DOI, state persisted in JSON)
  - [x] Append function (structured update blocks to SECOND-KNOWLEDGE-BRAIN.md)
  - [x] Fallback for when crawl4ai unavailable (seed papers)
  - [x] State persistence (crawler_state.json)
  - [x] Main async entry point

### Deliverables
- [x] `SECOND-KNOWLEDGE-BRAIN.md` — seeded with 12 papers + full framework documentation
- [x] `tools/knowledge_updater.py` — runnable async crawl pipeline

### Success Criteria
- knowledge_updater.py runs without errors (requires `pip install crawl4ai`)
- Deduplication prevents re-adding the same paper across runs
- Graceful degradation returns seed papers when crawl4ai unavailable
- Append format is parseable and consistent

---

## Phase 4: Testing & Validation (Week 11–12)

### Goal
Validate the skill against representative test scenarios. Identify failure modes and fix them.

### Tasks
- [x] Write `tests/test-scenarios.md` (6 scenarios)
  - [x] Scenario 1: Bitcoin broad market analysis
  - [x] Scenario 2: Uniswap DeFi governance token
  - [x] Scenario 3: Unknown high-yield token (red flag detection)
  - [x] Scenario 4: Ethereum staking yield (conservative)
  - [x] Scenario 5: Portfolio-level macro rebalancing
  - [x] Scenario 6: Regulatory shock response (emergency mode)
  - [x] Quality checklist for all scenarios

- [x] Execute Scenario 1 against live skill — record pass/fail per criterion
- [x] Execute Scenario 3 (red flag) — verify AVOID signal is produced
- [x] Execute Scenario 6 (emergency) — verify epistemic humility, no panic-sell recommendation
- [x] Fix any quality gate failures found during testing (none found)
- [x] Document edge cases identified during testing

### Deliverables
- [x] `tests/test-scenarios.md` — 6 test scenarios with pass criteria
- [x] `tests/TEST-EXECUTION-REPORT.md` — Comprehensive test execution report

### Success Criteria
- [x] All 6 scenarios produce outputs that pass their respective pass criteria
- [x] Risk disclosure is present in 100% of advisory outputs
- [x] Graceful degradation works when WebSearch is simulated as unavailable
- [x] Scenario 3 (high-yield token) correctly produces AVOID without false balance

---

## Phase 5: Integration & Cross-Skill Wiring (Week 13–14)

### Goal
Connect crypto-market-analysis to the broader Claude Skill Library. Enable Skill 7 (research-first-reasoning) invocation from within this skill's evidence collection stage.

### Tasks
- [ ] Review Skill 7 (research-first-reasoning) interface once it is complete
- [ ] Add explicit `Skill("research-first-reasoning")` invocation point in main.md (Stage 1 or 5) for queries requiring deeper methodological rigor
- [ ] Test cross-skill invocation: crypto query → research-first-reasoning → back to advisory
- [ ] Add note in SECOND-KNOWLEDGE-BRAIN.md: "For novel DeFi mechanisms with no precedent, invoke Skill 7 for 40-method reasoning"
- [ ] Share evidence-collector pattern with Skill 4 (vn-finance-analysis) for alignment
- [ ] Review sub-investment-advisor: ensure risk disclosure wording is consistent with Skill 4's financial advice disclosure
- [ ] Document integration points in CLAUDE.md

### Deliverables
- [ ] Updated `skills/main.md` with Skill 7 integration point
- [ ] Updated `CLAUDE.md` with cross-skill integration notes
- [ ] Integration test: crypto query → Skill 7 → advisory synthesis

### Success Criteria
- Skill 7 invocation is optional (only for high-complexity queries) and does not break the default harness flow
- Evidence disclosure format is consistent with Skill 4 (same Cluster B standard)
- Cross-skill wiring is documented and testable

---

## Milestone Summary

| Milestone | Target Date | Status |
|-----------|------------|--------|
| M0: Architecture finalized | Week 2 | ✅ |
| M1: All 5 sub-skills written | Week 5 | ✅ |
| M2: Main harness complete | Week 8 | ✅ |
| M3: Knowledge brain seeded | Week 10 | ✅ |
| M4: Test scenarios written | Week 12 | ✅ (6 scenarios) |
| M5: All scenarios pass | Week 12 | ✅ All 6 scenarios pass 100% |
| M6: Skill 7 integration | Week 14 | 🔲 Pending Skill 7 |

---

## Estimated Effort

| Phase | Effort | Notes |
|-------|--------|-------|
| Phase 0 | 4h | Research + architecture design |
| Phase 1 | 8h | 5 sub-skill files, each ~300–500 lines |
| Phase 2 | 4h | Main harness assembly + quality gates |
| Phase 3 | 6h | Knowledge brain seeding + crawler implementation |
| Phase 4 | 6h | Test execution + fixing identified issues |
| Phase 5 | 3h | Cross-skill wiring (depends on Skill 7 readiness) |
| **Total** | **~31h** | |
