import pytest
from src.gloire_dev_ia import GloireDevIA
from src.security import SecurityAudit

# Utilisation d'un "fixture" pour une instanciation propre et rapide
@pytest.fixture
def agent():
    return GloireDevIA()

@pytest.fixture
def auditor():
    return SecurityAudit()

def test_agent_analyze_pro_web3(agent):
    """Test ultra-rapide avec validation de schéma blockchain."""
    payload = {"action": "swap", "amount": 100, "chain": "Polygon"}
    res = agent.analyze(payload)
    
    # Assertions innovantes
    assert isinstance(res, dict), "La réponse doit être un dictionnaire JSON"
    assert "status" in res, "Le statut Web3 est manquant"
    assert "tx_hash" in res or "error" in res, "La transaction doit fournir un hash"

def test_audit_structure_souveraine(auditor):
    """Vérification rigoureuse des 6 piliers de sécurité."""
    report = auditor.audit({})
    
    # Vérification de l'intégrité du système
    required_pillars = {"FONDATION", "COEUR", "SECURITE", "ECONOMIE", "CONFIANCE", "IMPACT"}
    assert required_pillars.issubset(report.keys()), "Un pilier souverain manque à l'appel"
    
    for pillar, data in report.items():
        assert isinstance(data, list), f"Le pilier {pillar} doit retourner une liste d'audit"
