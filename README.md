# MultiAgent Research Analyst

An autonomous multi-agent research system that **queries, evaluates, and synthesizes** web data into **cited, structured research reports**.

Built on a stateful LangGraph pipeline (Search → Summarize → Critique → Write) with a **critique-revise reflection loop**, production guardrails, and end-to-end tracing.

> 🚧 **Status:** Under active development — Phase 0 (setup).

---

## Why this project

A single LLM call gives shallow, unverified answers (hallucination, no sources). This system runs an **autonomous multi-agent workflow** that gathers sources, summarizes with attribution, critiques its own work, and writes a grounded report with citations — reliably, with guardrails against infinite loops and runaway cost.

## Architecture

```
START → 🔍 Search → 📝 Summarize → 🧐 Critique ──gaps?──┐
                          ▲                              │
                          └──────────── revise ──────────┘
                                     │ enough
                                     ▼
                          ✍️ Write → review → END (report + citations)
```

- **Search** — generates focused sub-queries, fetches & dedups web sources
- **Summarize** — condenses findings with source attribution
- **Critique** — checks gaps, coverage, unsupported claims (self-correction)
- **Write** — produces a grounded report with citations

Cross-cutting: max-iteration & cost guardrails · retries/fallbacks · Postgres checkpointing · Langfuse tracing.

## Tech stack

| Layer | Choice |
|---|---|
| Language | Python 3.11+ |
| Orchestration | LangGraph |
| Backend | FastAPI (async, SSE) |
| LLM | OpenAI / Anthropic / Gemini via LiteLLM |
| Search | Tavily |
| Observability | Langfuse |
| State / persistence | Postgres (LangGraph checkpointer) |
| UI | Streamlit |
| Infra | Docker · GitHub Actions |

## Getting started

```bash
# (setup steps will be added as the project is built)
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -e .
```

## Roadmap

Phase-wise build: setup → single agent → 4-agent linear pipeline → reflection loop + guardrails → reliability → persistence + human-in-loop + streaming → evaluation + observability → deploy.

---

## License

MIT (to be added)
