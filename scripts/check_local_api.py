#!/usr/bin/env python3
"""Read-only, dependency-free Open WebUI API metadata check for AI Capsule.

Does not run inference, retrieve content, write files or modify configuration.
Never paste full /api/models responses into a public issue: they may contain
machine-specific metadata. This helper prints only selected nonsecret fields.
"""
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, build_opener, HTTPRedirectHandler
from urllib.parse import urlparse

URL = os.getenv("OWUI_URL", "http://127.0.0.1:8080").rstrip("/")
PRESET = os.getenv("OWUI_MODEL")
API_KEY = os.getenv("OWUI_API_KEY")


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


OPENER = build_opener(NoRedirect)


def request_json(path, bearer=None):
    headers = {"Accept": "application/json"}
    if bearer:
        headers["Authorization"] = "Bearer " + bearer
    req = Request(URL + path, headers=headers)
    with OPENER.open(req, timeout=15) as response:
        return json.load(response)


def main():
    if not API_KEY:
        sys.exit("OWUI_API_KEY is not set. Enter it locally; never commit or paste it.")
    if not PRESET:
        sys.exit("OWUI_MODEL is not set. Supply your local Alder preset ID.")
    parsed = urlparse(URL)
    if parsed.scheme != "http" or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}:
        sys.exit("OWUI_URL must use a local HTTP loopback address.")
    try:
        health = request_json("/health")
        result = request_json("/api/models", API_KEY)
    except HTTPError as exc:
        sys.exit("API request failed with HTTP " + str(exc.code) +
                 ". Confirm server URL, authentication and permissions.")
    except (URLError, OSError, ValueError, json.JSONDecodeError) as exc:
        sys.exit("Cannot read local Open WebUI JSON response: " + str(exc))

    models = result.get("data", []) if isinstance(result, dict) else []
    if not isinstance(models, list):
        sys.exit("Unexpected /api/models shape (no list in data field).")
    preset = next((m for m in models if m.get("id") == PRESET), None)
    if preset is None:
        sys.exit("Preset not listed in /api/models: " + PRESET)

    info = preset.get("info") or {}
    meta = info.get("meta") or {}
    caps = meta.get("capabilities") or {}
    base_id = info.get("base_model_id") or preset.get("id")
    base = next((m for m in models if m.get("id") == base_id), None) or {}
    ollama = base.get("ollama") or {}
    details = ollama.get("details") or {}

    snapshot = {
        "api_health_ok": health.get("status") is True if isinstance(health, dict) else False,
        "requested_preset": PRESET,
        "preset_found": True,
        "base_model_id": base_id,
        "provider_reported": base.get("owned_by", preset.get("owned_by")),
        "model_digest_reported": ollama.get("digest"),
        "quantization_reported": details.get("quantization_level"),
        "parameter_size_reported": details.get("parameter_size"),
        "context_length_reported": details.get("context_length"),
        "capabilities_reported": {
            "builtin_tools": caps.get("builtin_tools"),
            "file_context": caps.get("file_context"),
            "citations": caps.get("citations"),
            "memory": caps.get("memory"),
        },
        "knowledge_collections_attached_count": len(meta.get("knowledge") or []),
        "notes": [
            "API model metadata does not prove current prompt text or function-calling mode.",
            "This read-only check is not a retrieval, offline, reproducibility or safety test.",
        ],
    }
    print(json.dumps(snapshot, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
