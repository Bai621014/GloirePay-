import pytest
import asyncio
from src.gloire_dev_ia import GloireDevIA
from src.security import SecurityAudit

# Fixtures avec portée (scope) de module pour rapidité maximale
@pytest.fixture(scope="module")
def agent():
    return GloireDevIA()

@pytest.fixture(scope="module")
def auditor():
    return SecurityAudit()

@pytest.mark.asyncio
async def test_agent_stress_integrity(agent):
    """Test de charge : vérification de la résilience aux payloads corrompus."""
    # Payload malicieux pour tester la solidité
    corrupted_payload = {"action": None, "amount": -500, "chain": "INVALID_CHAIN"}
    
    res = agent.analyze(corrupted_payload)
    
    # Assertions de sécurité souveraine
    assert isinstance(res, dict)
    assert "error" in res or res.get("status") == "REJECTED", "Le système doit rejeter les données corrompues"

def test_audit_pillars_strict_integrity(auditor):
    """Vérification formelle de la structure des 6 piliers (ISO 20022)."""
    # Context d'audit simulé
    context = {"policies": True, "encryption": True, "checksums": True}
    report = auditor.audit(context)
    
    # Vérification de l'intégrité du rapport
    assert report["meta"]["status"] == "SECURE_AUDIT", "Le statut d'audit doit être SECURE"
    
    # Vérification récursive des piliers
    required = {"Gouvernance", "Confidentialité", "Intégrité", "Disponibilité", "Traçabilité", "Conformité"}
    assert all(p in report["findings"] for p in required), "La structure des piliers est incomplète"

def test_audit_fail_fast(auditor):
    """Test de détection immédiate des vulnérabilités."""
    empty_context = {} # Aucun contrôle de sécurité
    report = auditor.audit(empty_context)
    
    # Doit identifier au moins une erreur critique par pilier
    for findings in report["findings"].values():
        assert len(findings) > 0, "L'auditeur doit détecter l'absence de sécurité"
        assert findings[0]["severity"] in ["Critique", "Haute"], "La criticité doit être remontée"
