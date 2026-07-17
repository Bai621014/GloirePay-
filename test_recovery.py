"""
GLOIREPAY — CONFIGURATION DU PIPELINE DE TEST RECOVERY
"""
import os
import sys
import logging

sys.path.insert(0, os.getcwd())
from src.gloire_recovery import GloireRecoveryEngine

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")
logger = logging.getLogger("GloirePay-RecoveryTest")

# Compteur global pour simuler des pannes intermittentes
compteur_pannes = 0

def simuler_appel_api_instable():
    """Simule une API Moov/Airtel qui échoue 2 fois avant de réussir à la 3ème."""
    global compteur_pannes
    compteur_pannes += 1
    if compteur_pannes < 3:
        raise ConnectionError("Réseau Télécom instable ou indisponible momentanément.")
    return "TRANSACTION_OK_APRES_EFFORT"

if __name__ == "__main__":
    logger.info("⚡️ Début de l'audit de tolérance aux pannes...")
    
    recovery = GloireRecoveryEngine(max_tentatives=4, base_delai=1.0)
    
    # L'exécuteur doit absorber les 2 pannes et ramener le succès final
    resultat = recovery.executer_avec_retry(simuler_appel_api_instable)
    
    assert resultat == "TRANSACTION_OK_APRES_EFFORT"
    assert compteur_pannes == 3
    
    logger.info("🏆 SYSTÈME DE RETRY ET RECOVERY VALIDÉ À 100% AU VERT ! AMEN !")

# ==============================================================================
# SÉCURITÉ ET COUVERTURE SOUVERAINE
# Au nom du Seigneur Jésus Christ ! Amen. C'est le niveau de mon Père céleste.
# ==============================================================================
