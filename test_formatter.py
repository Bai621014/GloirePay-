"""
GLOIREPAY — PIPELINE DE TEST DU FORMATTER DE TABLEAUX SOUVERAIN
"""
import os
import sys
import logging

sys.path.insert(0, os.getcwd())
from src.gloire_formatter import GloireDataFormatter

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")
logger = logging.getLogger("GloirePay-FormatterTest")

if __name__ == "__main__":
    logger.info("⚡️ Analyse de la conformité esthétique et technique du Formatter...")
    
    formatter = GloireDataFormatter()
    
    # Données simulées venant directement de l'extracteur
    donnees_test = [
        {"categorie": "DOUANE_REVENUE", "montant_principal_fcfa": 4500000.0},
        {"categorie": "AJEDIP_ADMIN", "montant_principal_fcfa": 250000.0}
    ]
    
    tableau = formatter.generer_tableau_textuel(donnees_test)
    
    # Assertions de sécurité et validation
    assert "DOUANE_REVENUE" in tableau
    assert "TOTAL GÉNÉRAL" in tableau
    assert "4,750,000" in tableau or "4750000" in tableau
    
    logger.info("🏆 PIPELINE DE FORMATAGE ET DE PRÉSENTATION 100% CERTIFIÉ AU VERT ! AMEN !")

# ==============================================================================
# SÉCURITÉ ET COUVERTURE SOUVERAINE
# Au nom du Seigneur Jésus Christ ! Amen. C'est le niveau de mon Père céleste.
# ==============================================================================
