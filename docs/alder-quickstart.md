# Alder quickstart — AI Capsule Technical Preview

**Audience:** technically inclined collaborators with local Ollama and Open WebUI experience. **Status:** instructions reconstructed from one working MacBook setup (14 October 2026); **independent clean installation NOT TESTED**. This is **not** an AI Capsule 1.0 installer.

This exercise tests Spanish-language questions against three **fictional English documents**. The demo is under [CC0 1.0](../demo/alder-station-v0.1/LICENSE). It does not handle real health or community-governed knowledge.

## 1. Get the components

- Clone this repository with `git clone https://github.com/AudiopediaFoundation/ai-capsule.git` **once it is public**, or download its ZIP. The repository contains **documentation, example sources and configuration**, not the model or an app bundle.
- Install **Ollama** and **Open WebUI Desktop** from their respective official distribution channels, respecting their upstream licenses. The tested Mac ran **macOS 15.7.9, Open WebUI Desktop 0.0.20 / server 0.11.4**, and local `qwen2.5:7b` **Q4_K_M**. UI labels and installation steps may differ by version.
- Obtain the model from Ollama while connected (for example `ollama pull qwen2.5:7b`; on macOS you may need the Ollama application's bundled CLI). **Download/install before attempting offline use.**

See [full observed environment](implementation.md). Neither the Ollama executable version nor the embedding model artifact digest was recorded; no first-time offline setup is claimed.

## 2. Create a separate Alder collection

In Open WebUI's administration/document settings, configure the following **before importing documents**:

| Setting | Tested value |
| --- | --- |
| Embedding model | `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` |
| Markdown Header Splitter | OFF |
| Chunk size / overlap | **5000 / 100** |
| Retrieval Top K | **6** |
| Hybrid Search / Full Context Mode | **OFF / OFF** |

Create a **new, otherwise empty** Knowledge collection, e.g. **AI Capsule | Alder Demo v0.1**. Import **only**:

```text
demo/alder-station-v0.1/documents/ALD-001.md
demo/alder-station-v0.1/documents/ALD-002.md
demo/alder-station-v0.1/documents/ALD-003.md
```

Wait for indexing to finish. **Do not import** the README, manifest or test cases: they contain expected answers and would contaminate retrieval. The [manifest](../demo/alder-station-v0.1/MANIFEST.md) gives the SHA-256 hashes of all three source files.

## 3. Create the experimental preset

Create a **new custom model/preset** based on `qwen2.5:7b`. Attach **only** your new Alder collection, and use:

- **Function Calling:** Native; **Builtin Tools:** ON
- **File Context:** ON; **Citations:** ON; **Memory:** OFF
- **Temperature:** 0.1; other unnecessary tools disabled
- **System prompt:** copy [`config/native-system-prompt-v1.3.txt`](../config/native-system-prompt-v1.3.txt) in full.

The prompt's historical “AI Capsule 1.0” wording is an experimental model label, **not a claim that the later product has shipped**. Keep other collections/presets separate. Some settings may be named differently in other Open WebUI versions.

## 4. Try the two observed prompts in separate new chats

**A. Single-source test (ALD-T01; one locally observed PASS)**

```text
Según los documentos de Alder Learning Station, ¿qué días y en qué horarios abre la estación? Identifica el documento utilizado.
```

**Check:** Open WebUI actually calls `query_knowledge_files` and returns `ALD-001.md`. The answer should attribute Tuesday **09:00–11:00** and Friday **14:00–16:00** to that document, and not invent other hours. The tool was selected autonomously in the recorded run, but this is **not guaranteed** in a new run.

**B. Explicit two-source search (ALD-T03c; locally observed retrieval/synthesis, PARTIAL attribution)**

```text
Utiliza la herramienta query_knowledge_files para buscar en el contenido de los documentos de conocimiento adjuntos antes de responder.

¿Cuándo abre Alder Learning Station y cómo se escuchan las historias cuando no hay Internet? Usa solamente los documentos disponibles e identifica las fuentes.
```

**Check:** the tool should actually retrieve both `ALD-001.md` (opening hours) and `ALD-002.md` (headphones and audio stored on the local laptop, without Internet). **Inspect claim-level citations:** in the observed run, the model wrongly cited `ALD-001.md` for an offline-audio claim belonging to `ALD-002.md`. Mark such output **PARTIAL**, not a full PASS.

**Known failure to reproduce:** Run just the second question **without** the explicit `query_knowledge_files` instruction in a new chat (ALD-T03). In the original setup it **failed to initiate retrieval in 3/3 runs**, instead asking for information already present in the collection. This is a known autonomous tool-selection limitation.

## 5. Record results without overclaiming

For each run, note the software/hardware, model and preset, fresh-chat prompt, visible knowledge tool call, returned filenames, whether each claim matches its source, and **PASS / PARTIAL / FAIL / NOT TESTED**. Compare the answer with the original fictional documents—not merely the UI's source list. See [six fixed test cases](../demo/alder-station-v0.1/TEST_CASES.md).

The [OFF-01 record](offline-test-2026-10-14.md) documents a successful disconnected run **after all components were already installed**; it does **not** demonstrate prevention of network egress when online. One local query took [49 seconds end-to-end](performance-2026-10-14.md), with green macOS memory pressure—performance suitability depends on the actual task and operating environment.
