# Internal-corpus retrieval benchmark — bounded technical summary

**Observation date:** 12 October 2026. **Status:** exploratory, user-observed tests on one machine. The 23-document English Audiopedia health corpus, raw model outputs and source excerpts are **not included or licensed for redistribution**. This report contains technical settings and structural observations only; it is not medical information or a performance certificate.

## Test question

Could Spanish questions retrieve relevant English documents and produce source-grounded Spanish drafts from a small local collection? The test used a MacBook Air M1 with 16 GB RAM, `qwen2.5:7b`, Open WebUI and temperature 0.1. Exact application and model artifact versions were not captured at the initial 12 October run. The later [implementation record](implementation.md) describes a separate 14 October snapshot; do not assume every version or prompt was identical.

## Configuration sequence

| Phase | Header split | Chunk / overlap | Top K | Embedding | Bounded observation |
| --- | --- | --- | ---: | --- | --- |
| Initial | ON | 1000 / 100 | 3 | `sentence-transformers/all-MiniLM-L6-v2` | One target was retrieved; citation preview showed only metadata in one case. Unsupported suggestions appeared in draft output. |
| Single-file check | OFF | 1000 / 100 | 3 | Same | Relevant body text became available with only one document indexed; collection size was a confounder. |
| Intermediate | OFF | 5000 / 100 | 3, then 6 | Same | A Spanish multi-part question still missed a second target; a comparable English question retrieved both. |
| Final 12 October snapshot | OFF | 5000 / 100 | 6 | `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | Both intended documents appeared for the fixed Spanish question in three consecutive runs. Generated prose still did not attribute all claims to the second document. |

Hybrid Search and Full Context Mode were OFF in the final snapshot. Exact index state, ranking threshold, embedding artifact hash and the earlier prompt export were not archived.

## What the observations support

- The final configuration retrieved both intended English files for **one fixed Spanish query in three runs**. That is a case result, not a general success rate.
- Source-list presence did not guarantee that generated prose attributed each claim to the right file.
- A change to multilingual embeddings coincided with better cross-language retrieval, but other settings and earlier collection changes prevent a clean causal claim.
- Earlier failures included missed target documents, unsupported additions and incomplete citation previews. Those failures remain part of the evidence.

No clinical accuracy, medical currency, rights to redistribute the corpus, production reliability, or general multilingual performance was established. The included [fictional Alder pack](../demo/alder-station-v0.1/README.md) is a separate demonstration and does not inherit these health-corpus results. New runs should use a fixed question set, record actual retrieved filenames and claim fidelity, and report latency and resource use separately.
