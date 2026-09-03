import pytest
from validators.cmr_eligibility_validator import CMREligibilityValidator
from validators.anchor_evidence_validator import AnchorEvidenceValidator
from engines.dde_engine import DDEEngine

def test_cmr_eligibility_valid():
    cmr = {
        "verification_status": "VALIDATED",
        "reconstruction_status": "RESTRUCTION_COMPLETE",
        "semantic_math_ast": {
            "type": "NUMBER",
            "value": 5
        }
    }
    assert CMREligibilityValidator.validate(cmr) is True

def test_cmr_eligibility_candidate_leakage():
    cmr = {
        "verification_status": "VALIDATED",
        "reconstruction_status": "RESTRUCTION_COMPLETE",
        "semantic_math_ast": {
            "type": "CANDIDATE_NODE",
            "value": 5
        }
    }
    with pytest.raises(ValueError, match="CANDIDATE_NODE leakage"):
        CMREligibilityValidator.validate(cmr)

def test_anchor_evidence_valid():
    cmr = {
        "semantic_math_ast": {
            "type": "MIXED_NUMBER",
            "visual_anchor_id": "anc_01"
        }
    }
    assert AnchorEvidenceValidator.validate(cmr) is True

def test_anchor_evidence_missing():
    cmr = {
        "semantic_math_ast": {
            "type": "MIXED_NUMBER"
        }
    }
    with pytest.raises(ValueError, match="Anchor evidence coverage"):
        AnchorEvidenceValidator.validate(cmr)

def test_dde_engine_execution():
    engine = DDEEngine()
    result = engine.execute_rule("MIXED_TO_IMPROPER", {"test": "data"})
    assert result["status"] == "EXECUTED_DETERMINISTICALLY"
    assert result["rule_id"] == "MIXED_TO_IMPROPER"
