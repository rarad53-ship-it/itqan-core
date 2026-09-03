class TraceabilityValidator:
    @staticmethod
    def validate_trace(audit_log: dict) -> bool:
        """Ensures full audit traceability: Question Item -> CMR Node -> Visual Anchor -> Source Image."""
        required_keys = ["question_id", "cmr_node_id", "visual_anchor_id", "source_image_id"]
        for key in required_keys:
            if not audit_log.get(key):
                raise ValueError(f"Traceability breach: Missing {key}")
        return True
