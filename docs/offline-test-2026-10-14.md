# OFF-01 — AI Capsule Technical Preview offline knowledge-retrieval observation

**Date:** 2026-10-14  
**Status:** **Operator-confirmed success while disconnected; no independent network instrumentation**. One observed run. Not an independently witnessed network-isolation test.

## Purpose

Determine whether the **previously installed** AI Capsule system can execute local inference **and** source-content retrieval when the MacBook is disconnected from the internet. This is a limited feasibility test, not an audit of outbound traffic when network connectivity returns.

## Test environment

- MacBook Air M1, 16 GB, macOS 15.7.9 (build 24G830).
- Locally running Open WebUI Desktop with Ollama-backed `qwen2.5:7b` Q4_K_M.
- Separate preset: `AI Capsule | Alder Demo v0.1`, using the frozen Native Retrieval v1.3 prompt and its own three-document **synthetic, English** [Alder Station Knowledge Pack](../demo/alder-station-v0.1/README.md).
- Instructions issued to operator: keep Open WebUI/Ollama running; disable Mac Wi-Fi; confirm no Ethernet, mobile hotspot, or other active network interface; open a fresh chat and ask the question below; keep Wi-Fi off until recording result.
- **Connectivity state:** on 14 October, the operator explicitly confirmed that **Wi-Fi was off and no Ethernet or mobile hotspot was active throughout OFF-01**. This is a firsthand operator confirmation; an independent network-interface log was **not** captured.

## Prompt

> Utiliza la herramienta `query_knowledge_files` para buscar en los documentos adjuntos.
>
> Según Alder Learning Station, ¿qué días y en qué horarios abre la estación? Identifica el documento utilizado.

The tool name was stated explicitly to test the **offline execution path** without confounding the result with known autonomous tool-choice errors.

## User-reported observations

- The Open WebUI chat functioned and displayed **View Result from query_knowledge_files**.
- Returned source filenames in order: `ALD-001.md`, `ALD-003.md`, `ALD-002.md`.
- Spanish output attributed opening hours to `ALD-001.md`.
- Correctly reported the **fictional** station's schedule: Tuesday 09:00–11:00; Friday 14:00–16:00; closed on other days.
- Included an unnecessary generic communication-draft footer; this is an output-quality issue, not a retrieval failure.
- Exact wall time, inference speed, RAM, network-interface log, and system logs: **NOT RECORDED**. The operator separately confirmed the disconnection state.

## Assessment

| Property | Result | Interpretation |
| --- | --- | --- |
| UI availability and local answer generation | PASS (reported) | Model generated text during intended offline procedure |
| Content search tool execution | PASS (reported) | Open WebUI displayed the expected tool call |
| Retrieval / source identity | PASS (reported) | Correct source `ALD-001.md` returned and cited |
| Factual fidelity against test document | PASS (reviewed manually) | All reported schedule details agree with synthetic document |
| Actual internet connections disabled | **PASS (operator-confirmed)** | Wi-Fi off; no Ethernet or mobile hotspot throughout test. No independent network log |
| No cloud AI dependency for *previously loaded inference/retrieval* | **PASS (one observed offline run)** | Model and embeddings were already installed/cached; no first-install/download test |
| Prevention of network egress once connected | **NOT TESTED** | Requires distinct monitoring/audit |
| General tool-selection or response reliability | **NOT ESTABLISHED** | Question explicitly named the tool; one run |

This test should not be presented as certified air-gapping, elimination of telemetry or remote-content exposure, full installation independence, or a proof of The Membrane.

**Follow-up:** Operator's connection-state confirmation received. Optionally repeat OFF-01 with independently captured network-state, latency and RAM measurements. Proceed to publication rights/security/reproducibility checks separately. The repository stays private pending the [publication gate](../PUBLICATION.md).
