# Using Marketing Practice Radar: From interesting idea to a decision

An interesting discussion is not a strategy. This guide is about turning a marketing claim into something you can honestly evaluate and, if worthwhile, apply.

## The five-minute route for a solo founder

Open the [public demonstration](https://abharadwaj-cell.github.io/marketing-practice-radar/). It uses fictional ideas. Filter to **Digital PR**.

You'll see **Expert Q&A editorial partnerships**. The example suggests that original practitioner commentary *might* earn useful editorial exposure.

Before doing anything, ask three questions:

1. **Is this the right audience?** Would an editor's readership include the people who buy your product?
2. **What evidence exists?** Who tested the approach, under what conditions, and was the result independently confirmed?
3. **What would success look like for us?** One relevant editorial mention might matter more than twenty irrelevant links.

If it survives those questions, define a narrow test. For example:

| Experiment element | Illustrative definition |
| --- | --- |
| Hypothesis | Relevant subject-matter expertise will earn editorial interest more often than generic promotional pitches |
| Target | Editors writing for a specific buyer or practitioner segment |
| Treatment | Three individually researched, accurate, unpaid contributions |
| Comparison | Historic pitches or another ethically comparable pitch type |
| Primary metric | Verified relevant placements, not emails sent |
| Supporting metric | Qualified referral visits or later account engagement, if trackable |
| Time window | A pre-agreed 45 days, with a review date |
| Safeguards | No purchased undisclosed links; no fabricated expertise; stop repeated unsolicited outreach or source-policy violations |
| Decision | Adopt, refine or stop using the pre-agreed success threshold |

This is a **possible experiment design**, not an actual trial or reported result.

## For a CMO or growth leader

Use the radar to manage *investment in experiments* rather than chasing a daily list of tactics. Compare candidates across evidence strength, customer relevance, estimated effort, timing, downside risk, and the specific funnel outcome you want to improve.

Don't treat the score as permission to launch. It is an input to your decision. A method with excellent external evidence can still be wrong for your business model, compliance context, buying journey or available capacity.

An experiment should have an owner, a deadline, a budget cap, an approved measurement plan and an explicit rollback/stop rule. If a test works, assign a deadline to integrate it into the relevant existing GTM workflow. A lesson that stays in a PDF hasn't improved an operating system.

## For marketing specialists

Preserve the *original discussion or article*, the author and their expertise, the first observed date, original publication date, underlying data, method, result, contradictory evidence and platform restrictions.

Classify a source as independently verified, partly supported, opinion or unverified. Do not confuse a viral repost with an original claim, or a single impressive screenshot with a reproducible result.

Be careful with community posts: respect access restrictions, community rules and the writer's intent. Genuine contribution beats stealth promotion.

## For technical users

- `src/radar.py` contains the scoring and experiment-outline logic.
- `fixtures/synthetic_tactics.json` contains four invented examples.
- `config/sources.json` lists candidate sources; they are **disabled**.
- `src/collect_feeds.py` parses authorized RSS/Atom metadata, not full-page analysis.
- `tests/test_radar.py` verifies deterministic behavior.

Run `python -m unittest discover -s tests -v` before changing any scoring rule. Scores are weighted preferences, not calibrated probabilities. Enable sources only after checking their access terms and relevance.

## What the current version cannot tell you

It cannot prove that a marketing technique works, predict ROI, attribute revenue, evaluate expert credibility independently, or run a live campaign. Those require better evidence, actual integrations, defined experiments and commercial records.

For pipeline measurement, see [Marketing Revenue Lab](https://github.com/ABharadwaj-cell/marketing-revenue-lab). For market/product competition, see [Market Intelligence MCP](https://github.com/ABharadwaj-cell/marketing-market-intelligence-mcp).
