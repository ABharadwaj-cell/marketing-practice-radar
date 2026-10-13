# Marketing Practice Radar

**A universal, industry-agnostic marketing-method intelligence prototype** for marketing leaders, growth teams and businesses. It maps marketing practitioner discoveries to validated experiments intended to improve qualified demand, marketing-sourced pipeline and revenue.

## What exists today
- Source- and author-attributed research records with separate publication and observation timestamps.
- Explicit scoring rubric and opportunity ranking, with unverified claims labeled as unverified.
- Experiment briefs with hypothesis, audience, baseline requirements, primary metric, decision date and stop conditions.
- RSS/Atom collector for opted-in public feeds. Newly collected records go into an **unreviewed queue**; they are never automatically treated as validated research.
- Self-contained Python tests and a static interactive GitHub Pages dashboard using **synthetic examples**.

## What is NOT built yet
This is **not** an autonomous model, deployed MCP server, verified live intelligence feed, API-hosted backend, CRM attribution integration or production outreach system. There is no paid API requirement. Public data gathering requires each source to be accessible and permitted; GitHub Pages only hosts the static demo.

## Local commands
Requires Python 3.11+. No third-party Python packages are required.

```bash
python -m unittest discover -s tests -v
python src/radar.py
python src/collect_feeds.py --registry config/sources.json --output unreviewed_signals.json
```

Feed collection may require Internet access. The source registry is initially **disabled until verified**; enable permitted sources explicitly.

## Publish dashboard
GitHub repository Settings > Pages > Deploy from a branch > main > /docs.

## Data and ethics
No company data, customer contact records, credentials or paid-only sources are stored in this public repository. Source scoring is a documented triage heuristic, **not a statistical probability or fact verification**. Each proposal requires independent validation before publication or execution.

## Roadmap
1. Verify and enable public source feeds.
2. Review original-source provenance and independent evidence.
3. Connect an optional permitted LLM model adapter with evaluations.
4. Add experiment registry with time-bound adoption decisions.
5. Deliver normalized opportunity events to the Universal Marketing OS.
6. Connect commercial outcomes when appropriate CRM permissions are available.
