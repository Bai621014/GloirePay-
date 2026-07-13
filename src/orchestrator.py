import time
import sys
import os
from datetime import datetime

# Injection de chemin haute priorité
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from src.gloire_base import GloireBase
from src.blockchain_agent import GloireDevIA_Web3

class GloireOrchestrator:
    def __init__(self):
        self.db = GloireBase()
        self.agent = GloireDevIA_Web3()
        # Seuil par défaut : 1 Ether (1e18 Wei)
        self.threshold = int(self.db.db.get("settings", {}).get("minTreasuryThreshold", 1000000000000000000))
        print(">>> [GloireDevIA-Pro] Initialisation terminée.")

    def run_cycle(self):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"\n--- [GloirePay] Audit {timestamp} ---")
        
        try:
            # Récupération rapide du statut via l'agent Web3
            status = self.agent.get_treasury_status()
            balance = int(status.get('balance_wei', 0))
            
            print(f"Trésorerie Actuelle : {balance / 10**18:.6f} ETH ({balance} Wei)")
            
            if balance >= self.threshold:
                print(">> [Action] Seuil atteint : Maintenance souveraine déclenchée...")
                # Execution ultra-rapide
                result = self.agent.execute_treasury_maintenance()
                self.db.save_tx(f"MAIN-{int(time.time())}", {"status": "SUCCESS", "result": result})
                self.db.save_state()
                print(">> [Succès] État synchronisé avec la blockchain.")
            else:
                print(">> [Standby] Trésorerie sécurisée sous le seuil.")
                
        except Exception as e:
            print(f"!! [CRITIQUE] Erreur Web3 : {str(e)}")

if __name__ == "__main__":
    bot = GloireOrchestrator()
    print("Moteur Pro activé. Surveillance active...")
    while True:
        bot.run_cycle()
        # Cycle optimisé pour ne pas saturer le processeur du Redmi 13
        time.sleep(3600)
