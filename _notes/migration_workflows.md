# Migration Workflows: Real Public "Research Agent" Pipelines

Purpose: document REAL, PUBLIC, open-source research-agent pipelines that go
`source materials -> intermediate notes/outline -> final report`, so our defensive
study can say precisely which pipeline stage our fixed-evidence single-turn probe
models, and which stages it does not.

Scope note: zero-model-call, public-reading only. Every claim below is cited to a
URL. Model-inference / repo-execution was NOT performed. Items I could not verify
from public docs are marked "unverified" inline and collected at the end.

Date compiled: 2026-09-13.

Systems chosen for full treatment (clearest public pipeline docs):
1. Stanford STORM (agent pipeline #1)
2. GPT-Researcher (agent pipeline #2)
3. DeepResearch Bench (the benchmark our query_id 88/89/94/73 come from) — covered
   as the evaluation/ground-truth harness, not an agent pipeline.

---

## 1. Stanford STORM

- Repo: https://github.com/stanford-oval/storm
- Project page: https://storm-project.stanford.edu/research/storm/
- Paper: "Assisting in Writing Wikipedia-like Articles From Scratch with Large
  Language Models" (NAACL 2024), https://arxiv.org/abs/2402.14207
  (HTML: https://ar5iv.labs.arxiv.org/html/2402.14207)
- One-line: an LLM system that, per its README, "researches a topic and generates a
  full-length report with citations." (attribution: stanford-oval/storm README)

STORM splits generation into a **pre-writing stage** (research + outline) and a
**writing stage** (article + polish). README describes 4 modules implemented under
`knowledge_storm/storm_wiki/modules/*`, interface in `knowledge_storm/interface.py`.
Source: https://github.com/stanford-oval/storm/blob/main/README.md

### Pipeline stages (in order)

**Stage A — Knowledge Curation** (retrieval/collection)
- Component roles (LM names from README): `conv_simulator_lm` (query splitting +
  answer synthesis), `question_asker_lm` (follow-up questions). Retrieval via
  pluggable modules: `BingSearch`, `YouRM`, `SerperRM`, `BraveRM`, `SearXNG`,
  `DuckDuckGoSearchRM`, `TavilySearchRM`, `GoogleSearch`, `VectorRM`, `AzureAISearch`.
- Mechanism: **Perspective-Guided Question Asking** (discover diverse perspectives by
  surveying similar existing articles) + **Simulated Conversation** between a
  Wikipedia writer persona and a topic expert "grounded on trusted Internet sources"
  (attribution: STORM paper/README). Each expert answer triggers real search.
- (a) Source text entering: SEARCH RESULTS as **snippets** (content + source
  metadata/URL). The paper: "the LLM synthesizes the trustworthy sources to generate
  the answer a_i, and these sources will also be added to R for full article
  generation." So the durable artifact is a **reference set R** = collected snippets
  with their source URLs, accumulated across the simulated conversation turns.
  Source: https://ar5iv.labs.arxiv.org/html/2402.14207
- (b) Constraints applied: answers are to be **grounded on the retrieved/"trusted"
  sources**; the perspective personas steer breadth of questions. No numeric
  credibility score is documented (README emphasizes "grounding" but "specific
  filtering or source-weighting mechanisms are not detailed"). Source:
  https://github.com/stanford-oval/storm/blob/main/README.md

**Stage B — Outline Generation** (intermediate representation)
- Component: `outline_gen_lm` (README suggests a stronger model, e.g. GPT-4o).
- (a) Source text entering: the CURATED KNOWLEDGE from Stage A (the conversation /
  collected snippets), NOT raw web pages — organized into a hierarchical outline.
- (b) Constraints: produce a hierarchical section/subsection outline covering the
  curated knowledge. Source: https://github.com/stanford-oval/storm/blob/main/README.md

**Stage C — Article Generation** (drafting — the key stage for us)
- Component: `article_gen_lm`.
- Mechanism (paper, verbatim): "Since it is usually impossible to fit the entire R
  within the context window of the LLM, we use the section title and headings of its
  all-level subsections to retrieve relevant documents from R based on semantic
  similarity calculated from Sentence-BERT embeddings." So STORM writes the article
  **section by section**, and for EACH section it does a **semantic retrieval over the
  reference set R** keyed on that section's title/subheadings, then drafts the section
  grounded on that retrieved subset. Source:
  https://ar5iv.labs.arxiv.org/html/2402.14207
- (a) Source text entering: a per-section SUBSET of R (snippets most similar to the
  section title), not the whole corpus, not raw full pages.
- (b) Constraints: generate grounded text where "each sentence cites a list of
  documents in R" (paper) — i.e. inline citation attribution back to the collected
  references. Source: https://ar5iv.labs.arxiv.org/html/2402.14207

**Stage D — Article Polishing** (post-processing)
- Component: `article_polish_lm`. Adds a summary/lead section and optionally removes
  duplicate content. Source: https://github.com/stanford-oval/storm/blob/main/README.md

**Co-STORM (collaborative extension).** Adds human-in-the-loop discourse: Co-STORM
LLM experts "grounded on external knowledge sources", a Moderator that raises
"thought-provoking questions inspired by information discovered by the retriever", a
dynamic "mind map" concept structure, and a `DiscourseManager`
(`knowledge_storm/collaborative_storm/engine.py`; agents in
`.../modules/co_storm_agents.py`). Not central to our probe. Source:
https://github.com/stanford-oval/storm/blob/main/README.md

### Single-source domination & credibility

- Domination point: **Stage C**. Because each section is grounded on the top-k
  semantically-similar snippets from R, a section can be dominated by whatever was
  collected for that heading. If a rebuttal/correcting source is NOT in R (never
  retrieved in Stage A) OR is not among the semantically-nearest snippets for that
  heading, it cannot influence the section — exactly the failure mode our finding
  describes ("if the correct rebuttal isn't retrieved, it can't help").
- Credibility/weighting step: **none documented as an explicit numeric filter.**
  Selection into a section is by **semantic similarity (Sentence-BERT)**, not by
  source credibility. Language of "trusted sources" appears but no scoring/weighting
  algorithm is described. (unverified whether any credibility heuristic exists in
  code.) Source: https://github.com/stanford-oval/storm/blob/main/README.md ;
  https://ar5iv.labs.arxiv.org/html/2402.14207

### Data-flow sketch (STORM)

```
topic
  |
  v
[A: Knowledge Curation]  perspectives -> simulated Q&A -> web search (snippets)
  |    each expert answer is grounded on retrieved sources
  |    all sources appended -> reference set R = {(snippet, url)}
  v
[B: Outline Generation]  R/conversation -> hierarchical outline (sections)
  |
  v
[C: Article Generation]  FOR each section:
  |    section title/headings --Sentence-BERT similarity--> top-k docs from R
  |    draft section grounded ONLY on that retrieved subset, sentence-level citations
  v
[D: Polish]  add lead/summary, dedup
  |
  v
final article (with inline citations to R)
```

---

## 2. GPT-Researcher

- Repo: https://github.com/assafelovic/gpt-researcher
- Architecture wiki (community-generated): https://deepwiki.com/assafelovic/gpt-researcher
- Product manual (author-hosted): https://gptr.dev/llms-full.txt
- One-line: per its repo, "an autonomous agent that conducts deep research on any data
  using any LLM providers." (attribution: assafelovic/gpt-researcher README)

Planner/executor design. README (via docs): "The planner generates research
questions, while the execution agents gather relevant information. The publisher then
aggregates all findings into a comprehensive report." Source:
https://github.com/assafelovic/gpt-researcher

### Pipeline stages (in order)

Component/file names below are from the DeepWiki architecture pages (community-built
from source; treat exact paths as "high-confidence but secondary", not read from the
repo directly in this task). Source: https://deepwiki.com/assafelovic/gpt-researcher

**Stage A — Planning (sub-query generation)**
- Component: `ResearchConductor` (`gpt_researcher/skills/researcher.py`), method
  `plan_research()`; agent role chosen via `choose_agent()`.
- (a) Source text entering: the user query (plus optional prior context).
- (b) Constraints: generate "a set of questions that collectively form an objective
  opinion on the task." Source: https://deepwiki.com/assafelovic/gpt-researcher

**Stage B — Collection / scraping (per sub-query)**
- Components: retriever(s) (Tavily/Bing/Google/DuckDuckGo/etc.) return result lists;
  `BrowserManager` (`gpt_researcher/skills/browser.py`) does parallel URL scraping via
  a `WorkerPool`. Per-sub-query orchestration = `process_sub_query()`.
- (a) Source text entering: retriever results (URL + snippet), then **scraped page
  content** for chosen URLs. README bias-reduction claim: "the more sites we scrape
  the less chances of incorrect data. By scraping multiple sites per research, and
  choosing the most frequent information, the chances that they are all wrong is
  extremely low." (attribution: GPT-Researcher README). Reports "aggregate over 20
  sources." Source: https://github.com/assafelovic/gpt-researcher
- (b) Constraints: gather per research question from online/local resources; "each
  resource is summarized and its source is tracked." Source:
  https://deepwiki.com/assafelovic/gpt-researcher

**Stage C — Summarization + context assembly (intermediate representation)**
- Components: summarization per scraped resource; `ContextManager` "filters and
  compresses gathered information to fit LLM context windows." The accumulated
  artifact is the **"research context"** (dense text; deep-research mode also
  vectorizes/persists it in a vector store).
- (a) Source text entering: scraped page text -> **per-source SUMMARIES** (not full
  text stored downstream) + tracked source URL. So intermediate notes = summaries,
  not raw pages. Source: https://deepwiki.com/assafelovic/gpt-researcher ;
  https://gptr.dev/llms-full.txt
- (b) Constraints: compress/filter to fit context; keep source attribution.

**Stage C2 — Source curation / validation (optional, credibility step)**
- Component: `SourceCurator` class, async `curate_sources()`; runs AFTER gathering +
  context compression, BEFORE report generation. Sends sources to a "Smart LLM"
  (config `smart_llm_model`, temp 0.2, max_tokens 8000, top ~10 results) ranked by a
  `PromptFamily` guideline. Documented ranking criteria: Quantitative Value (highest),
  Relevance, Credibility ("authoritative sources favored over blogs"), Currency,
  Objectivity. Fallback: if the LLM output is malformed, return sources UNRANKED and
  proceed. Source: https://deepwiki.com/assafelovic/gpt-researcher/9.4-source-curation-and-validation
- NOTE: this is an LLM-judged ranking, and (per DeepWiki) appears to be an optional/
  configurable path rather than always-on. (unverified whether enabled by default.)

**Stage D — Report generation (drafting)**
- Component: `ReportGenerator` (`gpt_researcher/skills/writer.py`), `write_report()`.
- (a) Source text entering: the assembled **research context** (aggregated summaries +
  tracked sources), NOT the raw pages.
- (b) Constraints: produce a structured long-form report (README: typically >2,000
  words) with inline citations; multiple output formats (Markdown/PDF/DOCX/JSON) each
  "include a list of source URLs." Source: https://gptr.dev/llms-full.txt ;
  https://deepwiki.com/assafelovic/gpt-researcher

### Source / context object shape

- Documented behavior: each source has a URL that is tracked alongside a SUMMARY of
  the scraped content; retriever results carry URL + snippet; scraped content is the
  page body. Exact JSON field names (e.g. `url`/`href`, `title`, `raw_content`,
  `content`) are NOT confirmed from a repo read in this task — **field-name specifics
  = unverified.** Source: https://deepwiki.com/assafelovic/gpt-researcher

### Single-source domination & credibility

- Domination point: **Stage D drafting** consumes the aggregated research context.
  The design's own bias defense is **volume + frequency** ("choosing the most frequent
  information"), which means a single correct-but-rare rebuttal that is either (i) not
  scraped in Stage B, or (ii) filtered out in Stage C/C2, or (iii) a minority view
  outvoted by "most frequent information," can fail to affect the report — matching our
  finding. Source: https://github.com/assafelovic/gpt-researcher
- Credibility/weighting step: **YES, but LLM-judged and optional** — `SourceCurator`
  ranks by relevance/credibility/etc. Unlike STORM, there is an explicit credibility
  criterion, but it is a prompt-guided LLM ranking with an unranked fallback, not a
  hard verification. Source:
  https://deepwiki.com/assafelovic/gpt-researcher/9.4-source-curation-and-validation

### Data-flow sketch (GPT-Researcher)

```
user query
  |
  v
[A: plan_research]  -> sub-queries (research questions)
  |
  v
[B: per sub-query]  retriever (url+snippet) -> BrowserManager scrape (page text)
  |                 (parallel; aim ~20+ sources)
  v
[C: summarize + ContextManager]  page text -> per-source SUMMARY (+url tracked)
  |                              filter/compress -> "research context"
  |
  +--[C2: SourceCurator.curate_sources] (optional) LLM rank by relevance/credibility
  |
  v
[D: ReportGenerator.write_report]  research context -> long-form report
  |                                inline citations + source-URL list
  v
final report (md/pdf/docx/json)
```

---

## 3. DeepResearch Bench (source of our query_id 88/89/94/73)

- Repo: https://github.com/Ayanami0730/deep_research_bench
- Paper: "DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents"
  (arXiv 2506.11763), https://arxiv.org/pdf/2506.11763
- One-line: "A Comprehensive Benchmark for Deep Research Agents" (attribution: repo
  title) — 100 PhD-level tasks over 22 domains, 50 EN + 50 ZH.

This is NOT a materials->notes->report agent; it is the **evaluation harness** that
supplies our task prompts and defines what a "good, cited report" is. Included because
our probe's tasks (query_id 88/89/94/73) are drawn from it, and its FACT metric is
exactly a citation-verification stage we should be explicit about NOT modeling.

### Task data format (what our query_ids are)
- File: `data/prompt_data/query.jsonl`; each task has `id` + `prompt` (query text).
  Model outputs go to `data/test_data/raw_data/<model>.jsonl` as
  `{"id","prompt","article"}` (article = generated report with citations). Source:
  https://github.com/Ayanami0730/deep_research_bench

### Reference-report ("ground truth") construction
- Reference reports for RACE were, per the paper/search summary, "selected from deep
  research articles generated by the Gemini-2.5-pro-based Deep Research, as available
  in April 2025." Task set built from analysis of ~96,147 real user queries, binned
  into 22 domains (WebOrganizer taxonomy), refined by PhD-level experts. Sources:
  https://arxiv.org/pdf/2506.11763 ; https://www.emergentmind.com/papers/2506.11763
- Exact cleaning/selection pipeline for reference reports = only partially described
  publicly (data lives in `data/test_data/cleaned_data/`). **unverified** in detail.
  Source: https://github.com/Ayanami0730/deep_research_bench

### Evaluation stages
- **RACE** (Reference-based Adaptive Criteria-driven Evaluation): scores a target
  report against a reference report across four dimensions — Comprehensiveness,
  Insight/Depth, Instruction-Following, Readability — using task-adaptive dynamic
  weights. Script: `deepresearch_bench_race.py`. Source:
  https://github.com/Ayanami0730/deep_research_bench
- **FACT** (Factual Abundance & Citation Trustworthiness): (1) Statement-URL
  Extraction — extract factual claims + cited sources; (2) Deduplication; (3) Support
  Verification — scrape the cited URL and use an LLM to judge whether it actually
  supports the claim. Metrics: **Citation Accuracy** (% of citations truly supported)
  and **Effective Citations** (avg supported citations/task). Web scraping via Jina
  API. Source: https://github.com/Ayanami0730/deep_research_bench

### Relevance to single-source domination
- DeepResearch Bench does not itself decide which source dominates a section — it
  MEASURES the finished report. But FACT's Support-Verification step is precisely a
  per-citation check of "does the cited source back this claim," which is the check a
  robust pipeline would need and which our fixed-evidence probe does NOT perform.

### Data-flow sketch (benchmark harness)
```
query.jsonl (id, prompt)  --run YOUR agent-->  raw_data/<model>.jsonl (id,prompt,article)
                                                   |
                          +------------------------+------------------------+
                          v                                                 v
              [RACE] vs reference report                       [FACT] extract stmt->URL,
              (4 dims, adaptive weights)                       dedup, scrape+LLM verify
                          |                                                 |
                          v                                                 v
                  quality score                                citation accuracy / eff. citations
```

---

## WHERE OUR FIXED-EVIDENCE PROBE MAPS IN

Our probe = a single-turn setup where the model is handed an **already-collected,
fixed set of evidence snippets** (the evidence pack: q88/q89/q94/q73) and asked to
produce an answer/section from them. Mapping:

- **STORM:** corresponds to **Stage C, Article Generation, for one section** — the
  step that consumes an already-retrieved subset of R and drafts grounded text with
  citations. Our fixed pack ~= "the top-k snippets retrieved for a heading." We do NOT
  model STORM Stage A (knowledge curation / perspective Q&A / web search), the
  Sentence-BERT per-section retrieval that CHOOSES which snippets a section sees, Stage
  B outline construction, or Stage D polish.
- **GPT-Researcher:** corresponds to **Stage D, `write_report()`** consuming a frozen
  "research context" — or, more tightly, to a single section's drafting from that
  context. Our fixed pack ~= the assembled research context. We do NOT model Stage A
  planning/sub-query decomposition, Stage B scraping (`BrowserManager`/WorkerPool),
  Stage C summarization + `ContextManager` compression, or the optional
  `SourceCurator` credibility ranking (Stage C2).
- **DeepResearch Bench:** our tasks come from its `query.jsonl` prompts; our output is
  analogous to the `article` field. We do NOT run its **FACT** citation-verification
  (statement-URL extraction + scrape + LLM support check) nor **RACE** reference-based
  scoring as part of the probe.

Stages we explicitly did NOT model (across all three):
1. Retrieval / collection (which sources ever enter the pack).
2. Note/summary synthesis and context compression (how raw pages become snippets).
3. Source curation / credibility weighting (STORM: none numeric; GPTR: optional LLM
   ranking; Bench: FACT verification).
4. Multi-hop / iterative question-asking loops (STORM simulated conversation; GPTR
   deep-research iteration).
5. Per-section retrieval selection (STORM Sentence-BERT top-k choosing what a section
   sees).
6. Citation verification (Bench FACT).

Why this matters for the finding: our result ("if the correct rebuttal isn't in the
evidence, it can't help; and a poisoned/dominant source in the evidence steers the
output") lands squarely at the **drafting stage**. It says nothing yet about whether
the UPSTREAM stages (retrieval, curation, credibility ranking, citation verification)
would have admitted or filtered that source — those are separate stages the parent
should decide whether to probe. In real STORM the choice of a section's evidence is
made by semantic similarity (no credibility gate); in real GPT-Researcher there is an
optional LLM credibility ranking before drafting; in DeepResearch Bench a downstream
FACT check would catch an unsupported citation but not a plausibly-supported-but-wrong
framing.

---

## 未取得 / unverified

- STORM: whether the code has ANY credibility/source-weighting beyond Sentence-BERT
  semantic similarity (README says grounding is emphasized but "specific filtering or
  source-weighting mechanisms are not detailed"). Not confirmed by a code read here.
- STORM: exact top-k value and exact prompt text of the per-section generation step
  (paraphrased from paper; not quoted line-for-line beyond the sentences given).
- GPT-Researcher: exact source/context OBJECT schema and field names
  (url/href/title/content/raw_content). Component names (`ResearchConductor`,
  `BrowserManager`, `ContextManager`, `ReportGenerator`, `SourceCurator`) and file
  paths come from DeepWiki (community-generated from source), NOT from a direct repo
  file read in this task — treat as high-confidence-secondary.
- GPT-Researcher: whether `SourceCurator.curate_sources()` runs by default or only
  when configured; the exact `PromptFamily` guideline text.
- DeepResearch Bench: exact evaluator MODELS. DeepWiki listed current-repo evaluator
  configs as `openai/gpt-5.5` (RACE) and `openai/gpt-5.4-mini` (FACT) via OpenRouter;
  the original 2506.11763 paper used different (2025-era) judge models. Treat exact
  judge-model names as unverified / version-dependent.
- DeepResearch Bench: detailed reference-report cleaning/selection pipeline beyond
  "Gemini-2.5-pro Deep Research, April 2025" + expert refinement.
- The STORM arXiv PDF endpoint returned binary (unreadable) on direct fetch; STORM
  article-generation quotes were obtained from the ar5iv HTML mirror
  (https://ar5iv.labs.arxiv.org/html/2402.14207), not the canonical PDF.

---

## Source list (URLs cited above)

- https://github.com/stanford-oval/storm
- https://github.com/stanford-oval/storm/blob/main/README.md
- https://storm-project.stanford.edu/research/storm/
- https://arxiv.org/abs/2402.14207
- https://ar5iv.labs.arxiv.org/html/2402.14207
- https://github.com/assafelovic/gpt-researcher
- https://gptr.dev/llms-full.txt
- https://deepwiki.com/assafelovic/gpt-researcher
- https://deepwiki.com/assafelovic/gpt-researcher/9.4-source-curation-and-validation
- https://github.com/Ayanami0730/deep_research_bench
- https://arxiv.org/pdf/2506.11763
- https://www.emergentmind.com/papers/2506.11763
