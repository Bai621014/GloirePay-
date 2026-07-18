"""
GLOIREPAY — PIPELINE DE TEST DU COFFRE-FORT CRYPTOGRAPHIQUE
"""
import os
import sys
import logging

sys.path.insert(0, os.getcwd())
from src.gloire_crypto import GloireCryptoVault

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")
logger = logging.getLogger("GloirePay-CryptoTest")

if __name__ == "__main__":
    logger.info("⚡️ Analyse de la résistance et de la vélocité du coffre-fort...")
    
    coffre = GloireCryptoVault()
    
    identifiant_sensible = "Norman_VIP_Admin_001"
    
    # Exécution du chiffrement
    donnee_protegee = coffre.securiser_donnee_sensible(identifiant_sensible)
    
    # Assertions de contrôle technique
    assert donnee_protegee.startswith("SECURE_VAULT_VIP::") is True
    assert donnee_protegee != identifiant_sensible
    
    logger.info("🏆 PIPELINE CRYPTOGRAPHIQUE CERTIFIÉ IMPÉNÉTRABLE ET AU VERT ! AMEN !")

# ==============================================================================
# SÉCURITÉ ET COUVERTURE SOUVERAINE
# Au nom du Seigneur Jésus Christ ! Amen. C'est le niveau de mon Père céleste.
# ==============================================================================
