# Reproducing the technical preview

**Evidence snapshot: 14 October 2026.** The baseline below was observed or reported on one working Mac. No second-operator clean install has been verified.

## Recorded environment

| Item | Recorded value |
| --- | --- |
| Hardware and OS | MacBook Air M1, 16 GB RAM; macOS 15.7.9 |
| Open WebUI Desktop / server | 0.0.20 / 0.11.4 |
| Local model | `qwen2.5:7b`, Q4_K_M; reported model digest `845dbda0ea48ed749caafd9e6037047aa19acfcfd82e704d7ca97d631a0b697e` |
| Embedding model | `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` |
| Document settings | Markdown Header Splitter OFF; chunk size 5000; overlap 100; Top K 6; Hybrid Search OFF; Full Context Mode OFF |
| Preset | Native Function Calling; Builtin Tools ON; File Context ON; Citations ON; Memory OFF; temperature 0.1 (reported) |
| Prompt | [Native Retrieval v1.3](../config/native-system-prompt-v1.3.txt) |

The precise Ollama executable version, embedding artifact digest and reproducibility on another computer remain unrecorded. Obtain upstream components from their official distribution channels and check their current setup and license instructions. The preview does not supply an installer or model weights.

## Run the fictional demonstration

1. Start a local Open WebUI installation with `qwen2.5:7b` available.
2. Create a **new** knowledge collection for Alder. Set the embedding and document settings above **before ingestion**. If settings change later, reindex and record the change.
3. Add only `demo/alder-station-v0.1/documents/ALD-001.md`, `ALD-002.md`, and `ALD-003.md`. Do not ingest the manifest, README or test cases.
4. Create a **separate** custom preset using the settings above and the archived prompt. Attach only the Alder collection. The prompt's “AI Capsule 1.0” label is historical; it does not mean the product is released.
5. Start a fresh chat for each [test case](../demo/alder-station-v0.1/TEST_CASES.md). Inspect the actual knowledge tool call, returned filenames and every substantive claim. Record PASS, PARTIAL, FAIL or NOT TESTED based on observed output.

In the observed baseline, content retrieval used `query_knowledge_files`; filename search via `search_knowledge_files` was insufficient for document-content questions. Model selection of the right tool was inconsistent. A two-source Alder run retrieved both files but misattributed an offline detail to the wrong one. Do not treat a citation as proof of claim-level fidelity.

A local `/health` response and a user-observed [Alder retrieval](offline-test-2026-10-14.md) with Wi-Fi disabled were recorded after the model and embeddings had already been installed. The operator confirmed no Ethernet or mobile hotspot was active. No independent network-interface log, fresh offline installation, or guarantee against later outbound traffic was established. See the separate [performance observations](performance-2026-10-14.md) and [earlier internal-corpus benchmark summary](retrieval-benchmark-2026-10-12.md) for their distinct evidence limits.

## Local API check

`scripts/check_local_api.py` reads local Open WebUI health and model metadata. It does not run inference or inspect document content. Supply your own locally created API key through `OWUI_API_KEY` and the ID of your new Alder preset through `OWUI_MODEL`. Never commit either value or paste full model-list JSON into an issue.

```sh
curl -sS http://127.0.0.1:8080/health
OWUI_MODEL='your-local-alder-preset-id' python3 scripts/check_local_api.py
```

The script requires `OWUI_API_KEY` in the environment. Consult your local Open WebUI installation for its key creation workflow. The API check alone is not a retrieval, offline or safety test.
