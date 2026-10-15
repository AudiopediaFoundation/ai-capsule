# Publication review — AI Capsule Technical Preview

**Review date:** 15 October 2026  
**Technical review:** ChatGPT-assisted inspection of GitHub-connected repository content, history and documentation.  
**Recommendation:** **CONDITIONAL GO** for a narrowly described, publicly inspectable **Technical Preview (PoC)**; **not** for AI Capsule 1.0 as a finished product.  
**Authorization:** The recommendation is not itself Foundation release authorization. A repository owner must deliberately approve and perform the change to public visibility. Until then, this repository remains private.

## Completed release checks

- **Clean repository boundary:** New Git history with one root, single `main` branch, **25 examined commits**, **21 tracked files**, zero imported issues, and no GitHub releases at review. The original internal development repository remains private.
- **Credential/private-reference scan:** All 21 current files and all 25 available commit diffs were scanned programmatically for common GitHub/OpenAI/cloud/slack-type tokens, private-key headers, pasted bearer keys, local macOS home-directory paths, and references to confidential operational repositories or named prospective partners. **No matches found; no commit diff missing from inspection.** Commit authors use GitHub no-reply addresses. This is a **targeted pattern-based scan, not Gitleaks/TruffleHog or a penetration test**. Unreachable Git objects, repository settings, org-level secrets, local untracked files and future commits were not scanned.
- **Content rights:** Three Alder source files and their stable IDs/file sizes match the fictional demo manifest; original code/configuration, original documentation and the fictitious demo have distinct approved Apache-2.0, CC BY 4.0 and CC0 1.0 terms documented in [LICENSING.md](LICENSING.md). Raw Audiopedia Women's Health corpus, health-model outputs and real community-governed knowledge are **not included**. The preview does not bundle or rebrand third-party components.
- **Upstream terms:** Qwen2.5-7B and multilingual MiniLM model cards declare Apache-2.0; Ollama uses MIT. Open WebUI uses its own license for relevant modern versions, including branding terms, and is **not represented as OSI-approved open source**. Their software/model licenses are **not** changed by this repository.
- **Integrity of documentation links:** Checked all relative Markdown links in the current repository; no unresolved relative file links. External sites can evolve after publication.
- **Reproducibility disclosure:** A [quickstart](docs/alder-quickstart.md) and [setup record](docs/implementation.md) provide the tested configuration, separate collection ingestion and exact Spanish demonstration prompts. **An independent clean installation was NOT TESTED**, and the exact Ollama executable and embedding artifact digests were not captured.
- **Evidence and known defects:** Bounded v1.3 benchmark reports 9/12 **structural** checks, including 0/3 failure to initiate retrieval for one clear question; Alder two-source test 0/3 without explicit tool instruction, and a resulting source-attribution error when retrieval was forced. A user-confirmed disconnected run demonstrated local retrieval/inference on already installed components; it was **not** a network-egress audit. A single end-to-end response took about 49 seconds. Neither medical accuracy nor field suitability is claimed.

## Open limitations acknowledged for the Technical Preview

These **are disclosed limitations, not conditions requiring us to build AI Capsule 1.0 before publication**:

- Independent fresh-machine reproduction is **NOT TESTED**. Installation remains a technical, manual process.
- Dedicated third-party secret scanner, active network-exposure check, egress/telemetry instrumentation and full dependency security review are **NOT PERFORMED**. The scope of the pattern scan is stated above.
- Retrieval-tool decisions are inconsistent; citations can misattribute individual claims. Structural benchmarks are not an accuracy, clinical safety or general reliability rating.
- Permission systems, The Membrane, a production knowledge-to-audio workflow, and Indigenous/community governance controls are not implemented in the preview.

## Release authorization and maintenance

**Technical recommendation:** The reviewed candidate is **ready for owner-controlled publication as a technical preview**, with the limitations above. Do not describe it as a finished AI Capsule 1.0 product, certified secure environment or tested installation appliance.

**Final release GO is the Foundation repository owner's decision**. The change from private to public must be intentional; publication does not occur automatically as a result of this report. Review any subsequent commits/issues/attachments before changing visibility. Once public, preserve the reviewed wording and record the actual publication date/reviewer if useful.

Keep historical experiments, internal partner discussions, private issue timelines and confidential planning in the private development workspace. Do not import that history into this repository.
