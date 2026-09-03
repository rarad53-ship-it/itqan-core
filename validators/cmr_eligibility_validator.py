class CMREligibilityValidator:
    @staticmethod
    def _detect_candidate_node(node) -> bool:
        """Recursively traverses the AST to detect any CANDIDATE_NODE at any depth."""
        if isinstance(node, dict):
            if node.get("type") == "CANDIDATE_NODE":
                return True
            for value in node.values():
                if CMREligibilityValidator._detect_candidate_node(value):
                    return True
        elif isinstance(node, list):
            for item in node:
                if CMREligibilityValidator._detect_candidate_node(item):
                    return True
        return False

    @classmethod
    def validate(cls, cmr_data: dict) -> bool:
        if cmr_data.get("verification_status") != "VALIDATED":
            raise ValueError("Verification status is not VALIDATED.")
        if cmr_data.get("reconstruction_status") != "RESTRUCTION_COMPLETE":
            raise ValueError("Reconstruction status is not RESTRUCTION_COMPLETE.")
        
        ast = cmr_data.get("semantic_math_ast", {})
        if cls._detect_candidate_node(ast):
            raise ValueError("CANDIDATE_NODE leakage detected anywhere in AST. Build Blocked.")
        
        return True
