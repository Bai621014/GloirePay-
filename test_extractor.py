"""
GLOIREPAY — PIPELINE DE TEST DE L'EXTRACTOR ADMINISTRATIF
"""
import os
import sys
import logging

sys.path.insert(0, os.getcwd())
from src.gloire_extractor import GloireDataExtractor

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")
logger = logging.getLogger("GloirePay-ExtractorTest")

if __name__ == "__main__":
    logger.info("⚡️ Vérification de la puissance de tri du module administratif...")
    
    tri_agent = GloireDataExtractor()
    
    # Simulation d'un document brut administratif mixte (Douane & Association)
    document_brut = """
    Bureau des Douanes de Roro - Perception de Juillet : 4500000 FCFA
    Cotisation AJEDIP - Module de formation IA : 250000 FCFA
    """
    
    resultat_tri = tri_agent.extraire_et_trier_rapport(document_brut)
    
    # Assertions de validation VIP
    assert len(resultat_tri) == 2
    assert resultat_tri[0]["categorie"] == "DOUANE_REVENUE"
    assert resultat_tri[0]["montant_principal_fcfa"] == 4500000.0
    assert resultat_tri[1]["categorie"] == "AJEDIP_ADMIN"
    
    logger.info("🏆 PIPELINE DE TRI ADMINISTRATIF COMPLÈTEMENT AU VERT ! ALLÉLUIA !")

# ==============================================================================
# SÉCURITÉ ET COUVERTURE SOUVERAINE
# Au nom du Seigneur Jésus Christ ! Amen. C'est le niveau de mon Père céleste.
# ==============================================================================
