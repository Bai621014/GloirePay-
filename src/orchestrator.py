"""
GLOIREPAY — ORCHESTRATEUR SOUVERAIN (2026.VIP)
Moteur de surveillance transactionnelle avec tolérance aux pannes.
"""

import time
import sys
import logging
from pathlib import Path
from datetime import datetime, timezone

# Sécurité : Injection de PATH robuste
sys.path.append(str(Path(__file__).resolve().parent))

from src import GloireBase, GloireDevIA_Web3

# Configuration Logging VIP
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.FileHandler("gloire_audit.log"), logging.StreamHandler()]
)
logger = logging.getLogger("GloireOrchestrator")

class GloireOrchestrator:
    def __init__(self):
        self.db = GloireBase()
        self.agent = GloireDevIA_Web3()
        self.threshold = int(self.db.db.get("settings", {}).get("minTreasuryThreshold", 10**18))
        logger.info(">>> [SOUVERAINETÉ] Orchestrateur Initialisé")

    def run_cycle(self):
        """Cycle d'audit transactionnel sécurisé."""
        try:
            status = self.agent.get_treasury_status()
            if status.get("status") == "error":
                raise Exception(f"Node RPC unreachable: {status.get('message')}")
                
            balance = int(status.get('balance_wei', 0))
            logger.info(f"Audit Trésorerie : {balance} Wei")
            
            if balance >= self.threshold:
                self._execute_maintenance(balance)
            else:
                logger.info(">> [Standby] Trésorerie conforme.")
                
        except Exception as e:
            logger.critical(f"!! [CRITIQUE] : {str(e)}")

    def _execute_maintenance(self, balance: int):
        """Exécution sécurisée de maintenance avec traçabilité."""
        logger.warning(f">> [ACTION] Maintenance déclenchée (Bilan: {balance})")
        result = self.agent.execute_treasury_maintenance()
        
        tx_id = f"MAIN-{int(time.time())}"
        self.db.save_tx(tx_id, {"action": "maintenance", "result": result, "balance": balance})
        logger.info(f">> [SUCCESS] Tx enregistrée: {tx_id}")

if __name__ == "__main__":
    bot = GloireOrchestrator()
    logger.info("Système actif. Audit cyclique toutes les 3600s.")
    while True:
        bot.run_cycle()
        time.sleep(3600) # Maintenance horaire stable
