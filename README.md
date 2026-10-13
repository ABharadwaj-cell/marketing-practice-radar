# Marketing Practice Radar

**Find useful marketing ideas before the playbook gets stale. Then test them against business outcomes, not just engagement.**

A founder running marketing alone doesn't have time to read every SEO newsletter, watch every practitioner webinar, and keep up with community debates about what's working. A head of growth has a different problem: plenty of new tactics, not enough trustworthy evidence about which ones deserve time and budget.

Marketing Practice Radar is an early prototype for turning those conversations into **traceable research and controlled GTM experiments**.

[Explore the interactive demo](https://abharadwaj-cell.github.io/marketing-practice-radar/) · [Start here, without code](docs/START_HERE.md) · [Inspect the scoring method](src/radar.py)

> **Current status:** Runnable Python method-scoring logic, a public RSS/Atom metadata collector, unit tests, and a synthetic interactive dashboard. This is **not** an active AI research agent, a verified live feed, a hosted API, or an automated campaign system. Public feeds are disabled until their access and suitability are confirmed; the demo URL requires GitHub Pages to be enabled.

## Who should use this?

**Founder or one-person marketing team:** Pick one promising idea worth testing this month, with a specific goal, a stop condition, and a decision date. You don't need to know the latest acronyms to use the dashboard.

**CMO / VP Marketing / Growth Director:** Compare methods based on evidence, relevance, practicality, and commercial impact. Build a defensible experiment backlog instead of reacting to every trend.

**Marketing strategist or practitioner:** Preserve where an idea came from, what was actually claimed, how it was implemented, and which industries or GTM motions might benefit.

**Developer / data analyst:** Extend the collector, triage rules, evidence checks, and event contracts without hardcoding one marketing platform or industry.

## The question this project helps answer

> Someone claims a new approach to SEO, community distribution, email, or Digital PR is working. Is there credible evidence, is it relevant to our buyers, what should a fair test look like, and when do we decide whether to adopt it?

### How a discovery should move

**See an idea → capture its source → distinguish claims from proof → assess business relevance → define a small experiment → measure → adopt, revise, or reject by a deadline.**

For example, a practitioner might discuss editor-led interviews as a better alternative to generic guest posting. Rather than copy the tactic immediately, we'd first check the original discussion, the contributor's expertise, the editorial requirements and the likely buyer audience. Only then would we propose a test such as *three targeted, unpaid expert pitches* with a defined review window and a measure such as **verified, relevant earned placements**.

That example is a proposed operating pattern, **not an experiment already run or a result achieved**.

## What works in the current prototype

| Component | How it helps | Current limit |
| --- | --- | --- |
| Evidence-aware triage | Ranks *candidate* marketing methods using documented 1–5 inputs | A heuristic score, not verified effectiveness |
| Provenance fields | Retains author, channel, publication time, observation time and source reference | The four display examples use fictional authors and example URLs |
| Experiment outline | Proposes a hypothesis, primary KPI, test duration, baseline/control requirement and safeguards | Does not launch or evaluate experiments |
| Feed collector | Parses RSS/Atom from explicitly enabled public sources into an **unreviewed** queue | No sources enabled; availability and access must be checked |
| Browser demo | Filter example methods by channel category and GTM motion | Static, synthetic results |
| Tests | Verifies expected scoring behavior and collector boundaries | No claim of production coverage or model accuracy |

### Understanding the score

The current triage rubric weighs evidence strength **30%**, business relevance **30%**, novelty **10%**, transferability **15%**, and source reliability **15%**. Each factor is rated 1–5 and converted to a score out of 100.

A score of 78 **does not mean a 78% likelihood of success**. It is a way to prioritize what deserves *human evidence review*, and it can be misleading if the underlying ratings are poor.

## Try it in five minutes

1. Open the [dashboard](https://abharadwaj-cell.github.io/marketing-practice-radar/) after Pages is enabled.
2. Choose a marketing category or GTM motion.
3. Compare the candidate's stated primary KPI and test duration.
4. Ask what evidence would make the proposed method credible for **your** buyers and business model.
5. Choose one opportunity to investigate. Do not execute a public campaign from demo data.

The outcome we're ultimately trying to improve is **qualified demand, marketing-sourced opportunities, pipeline, and sustainable revenue**, not the volume of tactics discovered.

## Run the Python project

Requires Python 3.11+, no third-party Python dependencies.

```bash
python -m unittest discover -s tests -v
python src/radar.py
python src/collect_feeds.py --registry config/sources.json --output unreviewed_signals.json
```

The last command returns an empty collection until you deliberately enable a verified, permitted RSS/Atom source in `config/sources.json`. This is intentional.

Input examples are in `fixtures/synthetic_tactics.json`. Scoring is in `src/radar.py` and feed metadata parsing is in `src/collect_feeds.py`.

## Commercial relevance and accountability

To make this useful to a business, a future version must connect each test to a real owner, start and review dates, a credible comparison, budget and risk limits, and a commercial measurement where feasible. A rise in discussion volume is not evidence of pipeline lift.

See the [start-here guide](docs/START_HERE.md) for how to turn a candidate into an experiment brief.

## Boundaries and roadmap

- No claim here is endorsed, fact-checked or evidence of real-world performance.
- Earlier discovery does not prove original authorship; `first_observed` must remain separate from verified origin.
- The collector is metadata-only and requires valid public feed access; private communities must not be scraped without permission.
- Nothing is automatically posted, emailed, purchased, or tested on real users.
- Never put company confidential or personal customer information in this public project.

Next: validate sources, build a real evidence-review workflow, test an optional model against human-rated cases, introduce persistent experiment history and deadlines, then pass approved findings into the universal operating system and [Marketing Revenue Lab](https://github.com/ABharadwaj-cell/marketing-revenue-lab).

Related: [Market Intelligence MCP](https://github.com/ABharadwaj-cell/marketing-market-intelligence-mcp) for feature-level competitor observations.
