# AI Capsule — Technical Preview

AI Capsule is an experimental local, multilingual, source-grounded knowledge assistant from [LowRes.AI](https://lowres.ai/) and Audiopedia Foundation. This repository is a **technical preview for technically inclined collaborators**, not the AI Capsule 1.0 product or a ready-to-install application.

**Release:** Technical Preview (October 2026). Audiopedia Foundation has approved the licenses for its original material. The [publication review](PUBLICATION.md) records the security/content checks, open limitations and final repository-owner authorization requirement.

## What has been observed

On one MacBook Air M1 (16 GB), a locally run Qwen 2.5 7B model with Open WebUI retrieved English documents in response to Spanish questions. The entirely fictional [Alder Learning Station pack](demo/alder-station-v0.1/README.md) has been tested in a separate collection. One single-source test and an offline retrieval test succeeded in user-observed runs. Other tests exposed inconsistent tool selection and an incorrect source attribution. These observations do not establish reliability on a new machine.

The demo contains no real Indigenous or community-governed knowledge, no health source documents, and no medical advice. It does not implement community permission controls. See the [setup and evidence limits](docs/implementation.md).

## Evidence and limits

- [Alder test cases](demo/alder-station-v0.1/TEST_CASES.md) and [offline observation OFF-01](docs/offline-test-2026-10-14.md) document the fictional demonstration and the operator-confirmed disconnected run.
- [MacBook Air performance observations](docs/performance-2026-10-14.md) report one timed response and system-wide memory snapshots; these are not a hardware requirement or a verified process footprint.
- [Internal-corpus retrieval benchmark summary](docs/retrieval-benchmark-2026-10-12.md) preserves structural findings and failures from the earlier health-corpus test without distributing source text, raw outputs or health-specific prompts. Its results do not transfer automatically to Alder.


## Explore the preview

Start with the [Alder quickstart](docs/alder-quickstart.md) and review the [v1.3 structural benchmark](docs/native-retrieval-benchmark-v1.3-2026-10-13.md), which also documents a retrieval-decision failure.

1. Install the upstream runtime, model and interface separately. The tested versions and settings are in [docs/implementation.md](docs/implementation.md); a clean installation has **not** been independently verified.
2. Ingest only the three synthetic files in [demo/alder-station-v0.1/documents/](demo/alder-station-v0.1/documents/) into a new Open WebUI knowledge collection.
3. Create a separate experimental preset using the [archived v1.3 prompt](config/native-system-prompt-v1.3.txt). Its historical opening says “AI Capsule 1.0”; that was a working label, not a product-release claim.
4. Run the [Alder test cases](demo/alder-station-v0.1/TEST_CASES.md) and record actual tool calls, sources and claim accuracy. A citation alone is not evidence that every statement is supported.

The preview uses separately installed Qwen, Ollama, Open WebUI and an embedding model. Their licenses are independent of the licenses for material in this repository. See [LICENSING.md](LICENSING.md).

## Scope

The later **AI Capsule 1.0** is intended to be easier to obtain and install, with useful starter Knowledge Packs and a more reliable workflow. Those are development goals, not features delivered here. This technical preview is not a medical assistant, a production service or a validated community knowledge system.

No GitHub issue history was imported from the private development repository. New public-facing issues, if needed, should be written and reviewed afresh.

