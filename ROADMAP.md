# Roadmap — Technical Preview to AI Capsule 1.0

**Status:** Working roadmap, 15 October 2026. These are development objectives, not shipped features or promised release dates.

## Purpose

AI Capsule explores a practical question: can locally rooted organisations use sufficiently capable AI to work with trusted knowledge under constraints of connectivity, computing, budget and technical support?

Our design objective is:

> The simplest complete AI-enabled system that can reliably support a meaningful development outcome under the actual constraints of its operating environment.

The intended workflow is **select and prepare knowledge → retrieve and inspect evidence → draft or adapt information → human review → communication or action**. AI assists institutional work; it does not substitute for legitimate local knowledge authorities or professional judgement. LowRes.AI aims to **assemble appropriate existing components**, not build a new foundation model, inference engine or general-purpose chat platform.

## Where we are: Technical Preview (October 2026)

The [Technical Preview](README.md) documents a local Qwen2.5-7B / Ollama / Open WebUI configuration observed on one MacBook Air M1 (16 GB), a three-document **fictional** Alder demonstration corpus, a user-observed offline run, and bounded retrieval/performance experiments.

**Known gaps:** Retrieval is not consistently invoked; some source attribution is incorrect; clean installation by an independent operator and network-egress auditing have not been completed. Community permission controls and The Membrane are not implemented. This is not a deployed or clinically validated system. See [PUBLICATION.md](PUBLICATION.md) and the linked test records for evidence.

## Development path

The stages below identify work to test and evidence to gather. They need not be completed strictly in order.

| Area | Development objective | Evidence needed |
| --- | --- | --- |
| **Retrieval reliability** | Improve when retrieval occurs, which passages are selected, multilingual question handling, and attribution of claims. | Repeatable tests separating **source exists / retrieved / supplied to model / correctly used**; documented failures and improvements. |
| **Curated Knowledge Packs** | Create small, task-relevant Markdown-based collections with source provenance, licensing, dates, versioning and a reproducible preparation/indexing process. Keep externally sourced and locally governed material distinguishable. | A rebuildable, attributable example pack; tests of updates, retrieval quality and operating burden. A Knowledge Pack is not just a pile of PDFs or a vector index. |
| **Reproducible operation** | Make a known-good configuration easier to install, understand, run offline, diagnose and recover using affordable, locally obtainable components where feasible. | Independent clean-install exercise; documented models, versions, resource measurements, disconnected-operation checks and basic backup/restore procedures. |
| **Practical human governance** | Develop a **minimal, explicit** workflow for deciding what knowledge may be admitted, transformed, reviewed and released. Preserve provenance and distinguish technical controls from human procedures. | Demonstrated decisions and traceable outputs using fictional or appropriately authorised material; clear disclosure of what is and is not technically enforced. |
| **Institutional use** | Show one bounded knowledge-to-communication task in which local staff can inspect source evidence and review a draft before dissemination. Audio can be a downstream output; automated audio production is not required. | Reproducible task demonstration, documented human review, measured limitations and a comparison with a simpler non-AI workflow. |

## What counts as AI Capsule 1.0?

**AI Capsule 1.0** will mean a **documented, testable reference implementation**, not a commercial product or a claim of field readiness. The release decision should be supported by:

- A known-good configuration with an independently followed setup procedure and clearly stated hardware/operating limits.
- A curated, versioned example Knowledge Pack with lawful reuse and visible source attribution.
- Retrieval and answer-evidence evaluations that expose failures instead of treating fluent answers or citations as proof of correctness.
- A usable institutional review workflow with explicit human responsibility for outputs and truthful disclosure of implemented versus procedural governance.
- Documented offline operation, basic recovery and maintenance needs, plus licensing and security limitations.

A release may narrow supported tasks or configurations rather than pretend that unresolved capabilities are reliable.

## Boundaries and timing

The **October–December 2026 sprint** focuses on establishing evidence around the existing technical baseline, knowledge preparation, reliability, and documentation. A **15 December 2026 strategic review** will determine subsequent priorities; **no firm AI Capsule 1.0 release date is committed**.

This roadmap does **not** promise a new UI, custom hardware, a new model, support for arbitrary devices/languages, automated medical advice, an education platform, or a production-ready Membrane. Real Indigenous/community knowledge, authority arrangements, long-term maintainability and sustainable-development outcomes require partner-led field validation beyond a technical reference release.

Progress and priorities will change as tests reveal what is viable. A simpler non-AI approach remains the right choice whenever it better serves the intended outcome.
