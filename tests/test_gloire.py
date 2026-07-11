"""Tests unitaires basiques pour GloireDevIA."""

from src.gloire_dev_ia import GloireDevIA
from src.security import SecurityAudit

def test_agent_analyze_returns_dict():
    agent = GloireDevIA()
    res = agent.analyze({"foo": "bar"})
    assert isinstance(res, dict)
    assert "agent" in res
    assert res["agent"] == agent.name

def test_audit_reports_structure():
    sa = SecurityAudit()
    report = sa.audit({})
    # Doit contenir les 6 piliers
    assert set(report.keys()) == set(sa.piliers)
    for v in report.values():
        assert isinstance(v, list)
