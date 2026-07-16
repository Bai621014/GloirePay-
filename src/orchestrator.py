"""
GLOIREPAY — ORCHESTRATEUR SOUVERAIN (2026.VIP)
Architecture asynchrone haute performance.
"""

import asyncio
import logging
from src import GloireBase, GloireDevIA_Web3

# Configuration Logging VIP
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] [SOUVERAIN] %(message)s',
    handlers=[logging.FileHandler("gloire_audit.log"), logging.StreamHandler()]
)
logger = logging.getLogger("GloireOrchestrator")

class GloireOrchestrator:
    def __init__(self):
        self.db = GloireBase()
        self.agent = GloireDevIA_Web3()
        self.threshold = int(self.db.db.get("settings", {}).get("minTreasuryThreshold", 10**18))
        self.max_gas_price = 500 * 10**9 
        logger.info(">>> [SYSTÈME] Orchestrateur Asynchrone Initialisé")

    async def run_cycle(self):
        """Cycle d'audit asynchrone non-bloquant."""
        try:
            status = self.agent.get_treasury_status()
            balance = int(status.get('balance_wei', 0))
            current_gas = self.agent.w3.eth.gas_price
            
            if balance >= self.threshold:
                if current_gas <= self.max_gas_price:
                    self._execute_maintenance(balance)
                else:
                    logger.warning(f">> [ÉCONOMIE] Gas {current_gas} Gwei > Max. Attente.")
            else:
                logger.debug(">> [STANDBY] Trésorerie conforme.")
                
        except Exception as e:
            logger.error(f"!! [ALERTE] : {str(e)}")

    def _execute_maintenance(self, balance: int):
        # Logique de maintenance synchrone (bloquante le temps de la Tx)
        result = self.agent.execute_treasury_maintenance()
        logger.info(f">> [SUCCESS] Maintenance effectuée. Bilan: {balance}")

async def main():
    bot = GloireOrchestrator()
    logger.info("Démarrage du cycle asynchrone (Fréquence : 3600s).")
    while True:
        await bot.run_cycle()
        # await asyncio.sleep ne bloque pas le thread, il libère les ressources
        await asyncio.sleep(3600)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Arrêt propre demandé par le Boss.")
