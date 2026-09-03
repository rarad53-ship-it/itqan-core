class AnchorEvidenceValidator:
    @staticmethod
    def validate(cmr_data: dict) -> bool:
        """Ensures 100% visual anchor evidence coverage for sensitive nodes."""
        # Enforces that all sensitive nodes possess explicit visual anchor identifiers.
        ast = cmr_data.get("semantic_math_ast", {})
        def check_anchors(node):
            if isinstance(node, dict):
                if node.get("type") in ["MIXED_NUMBER", "FRACTION", "ROOT", "POWER"] and not node.get("visual_anchor_id"):
                    return False
                for v in node.values():
                    if not check_anchors(v):
                        return False
            elif isinstance(node, list):
                for item in node:
                    if not check_anchors(item):
                        return False
            return True
        
        if not check_anchors(ast):
            raise ValueError("Anchor evidence coverage is less than 100%. Build Blocked.")
        return True
