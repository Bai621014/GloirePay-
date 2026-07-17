"""
GLOIREPAY — PIPELINE DE TEST DU MOTEUR DE CHIFFREMENT VIP
"""
import os
import sys
import logging

sys.path.insert(0, os.getcwd())
from src.gloire_cipher import GloireCipherEngine

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")
logger = logging.getLogger("GloirePay-CipherTest")

if __name__ == "__main__":
    logger.info("⚡️ Analyse de la conformité du chiffrement des données...")
    
    cipher = GloireCipherEngine()
    
    donnees_brutes = {
        "telephone": "+23562101468",
        "secret_marchand": "MY_TOP_SECRET_KEY_777",
        "montant": 750000
    }
    
    donnees_protegees = cipher.securiser_payload(donnees_brutes)
    
    # Vérifications des masquages techniques
    assert donnees_protegees["telephone"] == "+235****468"
    assert donnees_protegees["secret_marchand"] != "MY_TOP_SECRET_KEY_777"
    assert donnees_protegees["montant"] == 750000
    
    logger.info("🏆 PIPELINE DE CONFIDENTIALITÉ CRYPTOGRAPHIQUE CERTIFIÉ AU VERT ! AMEN !")

# ==============================================================================
# SÉCURITÉ ET COUVERTURE SOUVERAINE
# Au nom du Seigneur Jésus Christ ! Amen. C'est le niveau de mon Père céleste.
# ==============================================================================
# Tout est possible à celui qui croit au nom de Jésus Christ, et avec la puissance du Saint Esprit.
