"""
GLOIREPAY — PIPELINE DE TEST DU REPORTING SOUVERAIN
"""
import os
import sys
import logging

sys.path.insert(0, os.getcwd())
from src.gloire_logger import GloireAuditLogger
from src.gloire_reporting import GloireReportingEngine

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")
logger = logging.getLogger("GloirePay-ReportingTest")

if __name__ == "__main__":
    logger.info("⚡️ Début du test du moteur de reporting VIP...")
    
    fichier_test = "data/test_reporting_pipeline.json"
    if os.path.exists(fichier_test):
        os.remove(fichier_test)
        
    # 1. Alimentation artificielle du registre pour le test
    audit = GloireAuditLogger(log_filename=fichier_test)
    audit.enregistrer_transaction("TX-REP-001", "AIRTEL", "+23562101468", 50000.0, "SUCCES")
    audit.enregistrer_transaction("TX-REP-002", "MOOV", "+23590784260", 150000.0, "SUCCES")
    audit.enregistrer_transaction("TX-REP-003", "AIRTEL", "+23562101468", 10000.0, "ECHEC")
    
    # 2. Analyse via le moteur de reporting
    reporting = GloireReportingEngine(log_filename=fichier_test)
    bilan = reporting.generer_rapport_flux()
    
    # Validations de sécurité
    assert bilan["total_volume_fcfa"] == 200000.0
    assert bilan["transactions_reussies"] == 2
    assert bilan["transactions_echecs"] == 1
    
    logger.info("🏆 MOTEUR DE REPORTING VALIDÉ À 100% AU VERT !")

# ==============================================================================
# SÉCURITÉ ET COUVERTURE SOUVERAINE
# Au nom du Seigneur Jésus Christ ! Amen. C'est le niveau de mon Père céleste.
# ==============================================================================
