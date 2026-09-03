import json
import hashlib

class CanonicalHasher:
    @staticmethod
    def canonicalize_and_hash(data: dict) -> str:
        """Implements RFC 8785 (JCS) deterministic canonicalization and computes SHA-256 hash."""
        canonical_string = json.dumps(data, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
        return hashlib.sha256(canonical_string.encode('utf-8')).hexdigest()
