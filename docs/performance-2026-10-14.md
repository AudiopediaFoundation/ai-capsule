# AI Capsule Technical Preview — MacBook Air performance observations (14 October 2026)

**Status:** Pre-query and under/after-query memory snapshots, a live Ollama model-load observation, and one manually timed end-to-end response. Peak memory and controlled repetitions remain NOT TESTED. Source: screenshots of macOS Activity Monitor supplied by the user on 2026-10-14; source images are not committed because the process-list image contains local account information and does not establish full per-process model memory. The test is observational rather than a clean-system profiling run.

## Test setup

- MacBook Air M1, physical memory 16.00 GB.
- macOS Sequoia 15.7.9 (build 24G830).
- Qwen 2.5 7B, Q4_K_M with Open WebUI Desktop and local Ollama integration, as recorded in [implementation.md](implementation.md).
- User submitted Activity Monitor **Memory** panel and a partial process list following instructions to capture the baseline **before a new answer**. Other concurrently running apps and exact uptime are not recorded.

## Snapshot: Before generating a new answer

| macOS Activity Monitor metric | Observed value |
| --- | ---: |
| Physical Memory | 16.00 GB |
| Memory Used | 13.02 GB |
| App Memory | 7.35 GB |
| Wired Memory | 1.93 GB |
| Compressed | 1.95 GB |
| Cached Files | 4.15 GB |
| Swap Used | 1.84 GB |
| Memory Pressure | Green (low on screenshot) |
| Open WebUI Helper (GPU), selected partial process listing | 173.9 MB |

**Interpretation and limits:** Green Memory Pressure at the snapshot suggests macOS was handling its then-current memory workload. **13.02 GB is system-wide**, not AI Capsule's measured process footprint. The 173.9 MB Open WebUI GPU Helper process is **not** model memory or total runtime RAM; other processes/shared/unified memory contribute. The swap value may reflect earlier system activity and does not alone demonstrate active swapping or poor performance. This screenshot cannot give model RAM, peak memory, tokens/s, load time or retrieval latency.

## Subsequent Qwen processing and model-load observations

After a local Alder Demo query, the user reported a generation-statistics panel showing approximately 21.55 seconds total completion duration (21.55 billion nanoseconds), 13.66 seconds prompt evaluation for 3,430 tokens, and 7.85 seconds generation for 94 tokens (11.97 output tokens/second). Loading duration was approximately 0.006 seconds, so this is **not evidence of a cold model load**. The full user-perceived, retrieval-inclusive elapsed time was not measured.

Immediately after a query, the locally installed Ollama CLI reported **qwen2.5:7b**, size **5.0 GB**, **100% GPU**, active context **8,192**, runner **llamacpp**, unloading in approximately four minutes. The active context is not the same as the model metadata reporting a maximum context capability of 32,768 tokens. Reported loaded size must not be naively added to system-wide RAM totals or individual process-memory readings to imply a verified Capsule-only peak footprint.

These are single user-observed samples, not statistically validated speed or memory requirements.

## Timed UI response and memory under/after a query

The user reported timing a local Alder Demo answer with a stopwatch: **first visible response at 42 seconds; complete result at 49 seconds**. This is a user-perceived time for the whole chat exchange, whereas the displayed inference statistics may cover only a final completion, not all tool calls and other backend work.

| Reported Ollama/UI statistic | Value |
| --- | ---: |
| total_duration | 22.045881 seconds |
| prompt_eval_count | 3,430 tokens |
| prompt_eval_duration | 14.231289 seconds |
| eval_count | 94 tokens |
| eval_duration | 7.773985 seconds |
| prompt_token/s | 241.02 |
| response_token/s | 12.09 |
| load_duration | 0.007896 seconds |

The ~27-second difference between 49 seconds and 22 seconds is **not independently decomposed** into retrieval, intermediate model calls, application processing and rendering.

| Activity Monitor metric | Earlier pre-query | Under/after timed query |
| --- | ---: | ---: |
| Physical RAM | 16.00 GB | 16.00 GB |
| Memory Used (system-wide) | 13.02 GB | 13.42 GB |
| App Memory | 7.35 GB | 4.01 GB |
| Wired Memory | 1.93 GB | 6.66 GB |
| Compressed | 1.95 GB | 2.06 GB |
| Cached Files | 4.15 GB | 2.64 GB |
| Swap Used | 1.84 GB | 1.71 GB |
| Memory Pressure | Green | Green |

These are **system-wide snapshots taken at different times**, not measurements of the total footprint of AI Capsule alone or the peak memory during inference. A green pressure indicator in both snapshots supports practical viability on this particular device under the observed workload, not an absence of transient spikes. Lower swap after the run does not measure swap activity during the run. Neither throughput nor latency should be extrapolated to other hardware or knowledge packs.
## Measurements still required

- [x] One user-timed Alder Demo response (42 seconds to first visible text, 49 seconds until completion), with model statistics (22.05 seconds for the reported completion). Exact tool/citations for this specific timed run not separately archived.
- [x] Two Activity Monitor system-wide memory snapshots, before and under/after query; pressure green in both. Peak values may have been missed.
- [x] Record reported Ollama generation duration/token counters and model loaded size; not equivalent to total model process RSS or peak RAM.
- [ ] Repeat a controlled prompt (e.g., three runs, distinguish warm vs cold) and record range/median rather than claiming universal performance.
- [ ] Note any user-visible lag, throttling, crashes or pressure changes.

Performance measurements are sufficient as **initial observational evidence for the narrow PoC**, but do not claim statistically validated speed, response-time guarantee, or total AI Capsule process RAM. Release remains gated by [publication gate](../PUBLICATION.md).
