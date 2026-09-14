"""Offline null retriever plug (Opt 1) — makes GPT-Researcher's planning stage use NO web,
so a report is built ONLY from the fixed local documents. Injected at the native
`get_retriever` config seam; the pinned gpt-researcher package on disk is NOT modified.
All other stages (plan_research_outline LLM call, local-doc summarization,
curate_sources(), report generation) run UNMODIFIED.

Retriever contract (verified against Duckduckgo at v3.6.1):
  __init__(self, query, query_domains=None); search(self, max_results=5) -> list[{href,body,...}]
  class attr requires_scraping (False => no URL scraping attempted).
"""
from __future__ import annotations

class OfflineNullRetriever:
    """A retriever that never touches the network and returns zero search results."""
    requires_scraping = False
    name = "offline_null"

    def __init__(self, query, query_domains=None):
        self.query = query
        self.query_domains = query_domains

    def search(self, max_results: int = 5):
        return []  # no web results -> planning proceeds on the query + local docs only

def install_offline_retriever():
    """Force GPT-Researcher to use ONLY the offline null retriever (no web at all).

    Patches get_retrievers at BOTH the actions module and the agent namespace (agent.py does
    `self.retrievers = get_retrievers(headers, cfg)` at construction). This bypasses Config's
    name validation, which otherwise resets unknown RETRIEVER names to 'tavily'. Call BEFORE
    constructing GPTResearcher. Only retriever SELECTION is replaced; context organization,
    curate_sources(), and report generation run unmodified. The pinned package on disk is
    untouched (runtime monkeypatch only)."""
    def _get_retrievers_offline(headers, cfg):
        return [OfflineNullRetriever]
    import gpt_researcher.actions.retriever as R
    R.get_retrievers = _get_retrievers_offline
    R.get_retriever = lambda name: OfflineNullRetriever if name == "offline_null" else None
    try:
        import gpt_researcher.agent as agent_mod
        agent_mod.get_retrievers = _get_retrievers_offline  # the reference used at agent.py:176
    except Exception:
        pass
    return "offline_null"
