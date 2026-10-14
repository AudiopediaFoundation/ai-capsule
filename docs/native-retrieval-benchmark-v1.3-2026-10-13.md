# Native Retrieval v1.3 — bounded structural benchmark

**Observed:** 13 October 2026 · **Status:** Internal exploratory benchmark, summarized for the AI Capsule Technical Preview. **Not a public-corpus benchmark or a product validation.**

## Question and setup

Can a locally running model choose the appropriate knowledge-search tool for clear document questions, ask for clarification when the request itself is ambiguous, and retrieve relevant sources when the requested information may not exist?

- **Hardware:** MacBook Air M1, 16 GB RAM; locally installed Qwen 2.5 7B (`qwen2.5:7b`, Q4_K_M), Open WebUI Desktop.
- **Frozen candidate:** Native Function Calling and [system prompt v1.3](../config/native-system-prompt-v1.3.txt), temperature 0.1; knowledge tools enabled, File Context/Citations ON, Memory OFF.
- **Retrieval:** A separate, **internal-only** 23-document English health collection; multilingual MiniLM embeddings, Markdown header splitting OFF, chunk size 5,000, overlap 100, Top K 6, Hybrid Search OFF, Full Context OFF. This corpus is **not** the [fictional Alder demonstration pack](../demo/alder-station-v0.1/README.md).
- **Method:** Local automated benchmark runner **v0.2**, four fixed cases repeated three times, with fresh-run records of actual tool calls and returned source filenames. The runner, source documents and raw response transcripts remain **outside this public-release candidate** pending code/content review.

## Recorded results — 4 cases × 3 repetitions

| Case | Structural behavior being checked | Observed runs | Interpretation |
| --- | --- | ---: | --- |
| **WH-18** | Clear, source-specific question should trigger document-content search and return both intended source IDs | **3/3 PASS** | `query_knowledge_files` called and both expected source filenames returned in every run. Does not independently establish complete answer fidelity. |
| **WH-19** | Under-specified request should be clarified without searching | **3/3 PASS** | No knowledge-tool calls or source returns in the three runs. |
| **WH-22** | Clear question requesting a detail that the relevant source does not specify should nevertheless trigger retrieval | **3/3 PASS** | `query_knowledge_files` called; the relevant source appeared **fifth of five** each time. The structural score **does not verify** that the response avoided inventing a detail. |
| **WH-23** | Clear, source-specific question about an unsupported statistic should search before deciding what can be answered | **0/3 FAIL** | No knowledge-tool calls or returned sources. A repeated **retrieval-decision failure**, not a successful document-based absence check. |

**Aggregate: 9 of 12 structural checks passed.** This denominator is a small, deliberately selected set of repeated checks: **9/12 is not a 75% accuracy, safety or general reliability score.**

A preceding controlled prompt comparison found that changing only the experimental system prompt from v1.3 to v1.4 coincided with WH-18 changing from **3/3 tool-use PASS** to **0/3**, while WH-23 remained **0/3**. For this experimental baseline, **v1.3 was restored and frozen**. These observations do not isolate broader causes or guarantee reproducibility.

## Why this matters for the preview

The results demonstrate that **retrieval capability, the decision to invoke retrieval, and claim-level source attribution are separate properties**. The available documents may be searchable while the model still fails to initiate a search for a clear query. Other experiments also found cases where retrieved sources were displayed but not fully attributed in generated prose.

These are **source-tool and workflow observations only**. No clinical or factual correctness of health-domain answers is certified. The underlying source rights, currency and clinical appropriateness are unreviewed, so no full health questions, source texts, treatment recommendations or raw model outputs are published here.

To reproduce a **publication-safe** example instead, use the three original **CC0 fictional Alder documents**, following the [Alder quickstart](alder-quickstart.md) and [test cases](../demo/alder-station-v0.1/TEST_CASES.md). The Alder results are separate observations and **must not be presented as a repeat** of these WH cases.
