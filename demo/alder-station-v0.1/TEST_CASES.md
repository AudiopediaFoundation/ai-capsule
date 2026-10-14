# Alder Station v0.1 — Spanish retrieval test cases

These are fixed prompts for the fictional [Alder pack](README.md). Earlier exploratory observations are described in the README; the cases below are **not a completed benchmark**. Start a fresh chat for each run, and record actual tool use, source filenames and claim-level accuracy. A citation alone is insufficient.

| Case | Spanish prompt | Expected evidence |
| --- | --- | --- |
| ALD-T01 | Según los documentos de Alder Learning Station, ¿qué días y en qué horarios abre la estación? Identifica el documento utilizado. | ALD-001: Tuesday 09:00–11:00; Friday 14:00–16:00. No other days. |
| ALD-T02 | ¿Qué debe hacer el voluntario cuando la batería de la computadora baja del 30 por ciento en Alder Learning Station? Identifica el documento utilizado. | ALD-002: pause new sessions and connect a charged power pack. |
| ALD-T03 | ¿Cuándo abre Alder Learning Station y cómo se escuchan las historias cuando no hay Internet? Usa solamente los documentos disponibles e identifica las fuentes. | ALD-001 and ALD-002; schedule plus local laptop playback. Check attribution to both files. |
| ALD-T04 | ¿Cuántas historias de audio tiene inicialmente Alder Learning Station y quién autoriza las nuevas? Identifica la fuente. | ALD-003: 12; designated fictional coordinator reviews and logs approval. |
| ALD-T05 | ¿Cuántas personas usaron Alder Learning Station en septiembre de 2026? Busca en la documentación disponible e identifica la fuente. | ALD-003 contains no usage statistics. No invented number. Record whether retrieval occurred. |
| ALD-T06 | No funciona. ¿Qué hago? | Ambiguous; ask for clarification without inventing a device or cause. |

Record the date, hardware, model digest, preset and ingestion settings, actual tool call, returned sources, response time if measured, and PASS / PARTIAL / FAIL / NOT TESTED with reviewer notes. Changed prompt wording requires a new test ID.

These fictional files cannot establish rights over real community knowledge, medical accuracy or implementation of the Membrane.
