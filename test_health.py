"""
GLOIREPAY — PIPELINE DE TEST DU DIAGNOSTIC DE SANTÉ SYSTEME
"""
import os
import sys
import logging

sys.path.insert(0, os.getcwd())
from src.gloire_health import GloireHealthMonitor

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")
logger = logging.getLogger("GloirePay-HealthTest")

if __name__ == "__main__":
    logger.info("⚡️ Analyse de la viabilité des moniteurs de santé...")
    
    moniteur = GloireHealthMonitor()
    rapport = moniteur.executer_check_vital()
    
    # Vérifications de la conformité du rapport
    assert rapport["statut_global"] == "SAIN"
    assert rapport["simulations_api"]["polygon_zkevm_rpc"] == "DISPONIBLE"
    
    logger.info("🏆 PIPELINE DE SURVEILLANCE ET DIAGNOSTIC CERTIFIÉ AU VERT ! AMEN !")

# ==============================================================================
# SÉCURITÉ ET COUVERTURE SOUVERAINE
# Au nom du Seigneur Jésus Christ ! Amen. C'est le niveau de mon Père céleste.
# ==============================================================================
# Tout est possible à celui qui croit au nom de Jésus Christ, et avec la puissance du Saint Esprit.
