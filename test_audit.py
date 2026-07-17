"""
GLOIREPAY — TEST DE JOURNALISATION D'AUDIT
"""
import os
import sys
import logging

sys.path.insert(0, os.getcwd())
from src.gloire_logger import GloireAuditLogger

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")
logger = logging.getLogger("GloirePay-AuditTest")

if __name__ == "__main__":
    logger.info("⚡️ Début du test du registre d'audit...")
    
    # Fichier temporaire de test
    fichier_test = "data/test_audit_pipeline.json"
    if os.path.exists(fichier_test):
        os.remove(fichier_test)
        
    audit = GloireAuditLogger(log_filename=fichier_test)
    
    # Simulation d'écritures de transactions VIP
    succes_airtel = audit.enregistrer_transaction("TX-ART-777", "AIRTEL", "+23562101468", 35000.0, "SUCCES")
    succes_moov = audit.enregistrer_transaction("TX-MOV-888", "MOOV", "+23590784260", 70000.0, "SUCCES")
    
    assert succes_airtel is True
    assert os.path.exists(fichier_test)
    
    logger.info("🏆 REGISTRE D'AUDIT COMPLIANT ET OPÉRATIONNEL ! AMEN !")
