# Alder Learning Station v0.1 — fictional demonstration Knowledge Pack

The three English documents in [documents/](documents/) describe an entirely invented listening station. The pack tests whether a local assistant retrieves English sources for Spanish questions and attributes its claims to the right files. It contains no real community, health or partner material.

**Status (14 October 2026):** CC0-licensed fictional pack; locally tested in one Open WebUI environment. A clean installation and public release have not been approved.

## Files

- [ALD-001](documents/ALD-001.md): schedule and access.
- [ALD-002](documents/ALD-002.md): equipment and local audio playback.
- [ALD-003](documents/ALD-003.md): fictional update procedure and absence of usage statistics.
- [Manifest](MANIFEST.md): origin, rights and SHA-256 values.
- [Test cases](TEST_CASES.md): questions, expected sources and assessment conditions.

**Ingest only the three `ALD-00x.md` files.** The manifest and test cases contain expected answers and would contaminate retrieval.

## Setup

Use the recorded versions and settings in [implementation.md](../../docs/implementation.md). Create a new knowledge collection, upload only the three documents, then create a separate Qwen 2.5 7B preset using [the archived prompt](../../config/native-system-prompt-v1.3.txt). Test each question in a fresh chat and inspect actual tool calls, source files and claims. The setup has not been independently repeated on a new machine.

## Bounded observations

On 14 October 2026, one user-observed ALD-T01 run retrieved `ALD-001.md` correctly. A two-source question initially failed to trigger retrieval in three runs; a more explicit query retrieved both files but attributed one offline detail to the wrong file. The operator also reported a successful local retrieval while Wi-Fi, Ethernet and mobile hotspot were off, with components previously installed. These observations are not a reliability estimate or a network-isolation proof.

The fictional coordinator procedure is not evidence of community consent or software-enforced authorization. The pack does not test health accuracy or real-world use. See [license](LICENSE) and [publication gate](../../PUBLICATION.md).
