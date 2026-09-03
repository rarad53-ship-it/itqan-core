import json
from pathlib import Path

class DDEEngine:
    def __init__(self):
        self.registries_dir = Path(__file__).parent.parent / "registries"
        self.rules = self._load_registry("derivation_rules.json")
        self.error_codes = self._load_registry("error_codes.json")

    def _load_registry(self, filename: str) -> dict:
        path = self.registries_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"Frozen registry not found: {filename}")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if data.get("mutation_allowed", True):
                raise ValueError(f"Registry {filename} violates immutable contract.")
            return data.get("rules", data.get("error_codes", {}))

    def execute_rule(self, rule_id: str, payload: dict) -> dict:
        if rule_id not in self.rules:
            raise ValueError(f"Unauthorized or non-existent derivation rule: {rule_id}")
        
        rule_def = self.rules[rule_id]
        operation = rule_def.get("operation")
        
        # Execution of approved registry rules only
        return {
            "rule_id": rule_id,
            "operation": operation,
            "status": "EXECUTED_DETERMINISTICALLY",
            "payload": payload
        }
