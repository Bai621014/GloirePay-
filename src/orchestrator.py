import time
import sys
import os
from datetime import datetime

# FIX ABSOLU : On ajoute le répertoire racine (celui qui contient src/) au PATH
# os.path.abspath('.') pointe toujours vers le dossier courant (ton dossier racine)
sys.path.append(os.path.abspath('.'))

from src.gloire_base import GloireBase
from src.blockchain_agent import GloireDevIA_Web3

class GloireOrchestrator:
    def __init__(self):
        # Initialisation directe
        self.db = GloireBase()
        self.agent = GloireDevIA_Web3()
        # Lecture sécurisée du seuil avec typage strict
        self.threshold = int(self.db.db.get("settings", {}).get("minTreasuryThreshold", 10**18))
        print(">>> [GloireDevIA-Pro] Initialisation terminée.")

    def run_cycle(self):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"\n--- [GloirePay] Audit {timestamp} ---")
        try:
            status = self.agent.get_treasury_status()
            balance = int(status.get('balance_wei', 0))
            print(f"Trésorerie Actuelle : {balance / 10**18:.6f} ETH")
            
            if balance >= self.threshold:
                print(">> [Action] Maintenance souveraine déclenchée.")
                result = self.agent.execute_treasury_maintenance()
                self.db.save_tx(f"MAIN-{int(time.time())}", {"status": "SUCCESS", "result": result})
                self.db.save_state()
                print(">> [Succès] Synchronisation Blockchain OK.")
            else:
                print(">> [Standby] Trésorerie sécurisée.")
        except Exception as e:
            print(f"!! [CRITIQUE] : {str(e)}")

if __name__ == "__main__":
    bot = GloireOrchestrator()
    while True:
        bot.run_cycle()
        time.sleep(3600)
