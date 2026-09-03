import json
from pathlib import Path
from jsonschema import validate, ValidationError

class SchemaValidator:
    @staticmethod
    def validate_instance(instance: dict, schema_name: str) -> bool:
        schemas_dir = Path(__file__).parent.parent / "schemas"
        schema_path = schemas_dir / schema_name
        if not schema_path.exists():
            raise FileNotFoundError(f"Schema not found: {schema_name}")
        
        with open(schema_path, "r", encoding="utf-8") as f:
            schema = json.load(f)
            
        try:
            validate(instance=instance, schema=schema)
            return True
        except ValidationError as e:
            raise ValueError(f"Schema validation failed for {schema_name}: {e.message}")
