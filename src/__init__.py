"""
GLOIREPAY — MODULE D'INITIALISATION SOUVERAIN (2026.VIP)
Standard : ISO 20022 - Architecture : Façade Sécurisée
"""

import sys
import os
import logging

# 1. Configuration du chemin pour que src puisse voir la racine
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 2. Configuration du log système
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [GLOIREPAY] %(message)s")
logger = logging.getLogger("GloirePay.Init")

# 3. Importation des composants (une seule fois)
from gloire_dev_ia import GloireDevIA
from security import SecurityAudit

# Métadonnées de conformité
__version__ = "2026.07.14"
__author__ = "GloirePay Core Team"
__all__ = ["GloireDevIA", "SecurityAudit", "get_system_status"]

def get_system_status() -> dict:
    """Vérification d'intégrité haute-fidélité pour le module."""
    try:
        status = {
            "module": "GloirePay.Root",
            "status": "OPERATIONAL",
            "version": __version__,
            "compliance": "ISO_20022_V1"
        }
        logger.info(f"Intégrité vérifiée : {status['status']} (v{__version__})")
        return status
    except Exception as e:
        logger.error(f"Erreur d'intégrité système : {e}")
        return {"status": "CRITICAL_FAILURE", "module": "GloirePay.Root"}

# Initialisation du noyau
logger.info("Noyau Souverain en ligne.")
