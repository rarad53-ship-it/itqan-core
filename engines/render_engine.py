class RenderEngine:
    @staticmethod
    def render_cmr(cmr_data: dict) -> str:
        """Deterministically renders CMR into standard mathematical output format without reinterpreting source."""
        ast = cmr_data.get("semantic_math_ast", {})
        node_type = ast.get("type", "UNKNOWN")
        display_val = ast.get("display", "")
        return f"RENDERED_{node_type}({display_val})"
