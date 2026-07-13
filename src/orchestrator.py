import time
from .gloire_base import GloireBase
from .blockchain_agent import GloireDevIA_Web3

class GloireOrchestrator:
    def __init__(self):
        # Initialisation souveraine : on charge tout depuis le local
        self.db = GloireBase()
        self.agent = GloireDevIA_Web3()
        # On récupère le seuil directement depuis votre registre local
        self.threshold = self.db.db.get("settings", {}).get("maintenance_threshold", 1000000000000000000)

    def run_cycle(self):
        print("--- [GloirePay] Cycle Souverain Actif ---")
        
        # Audit interne
        status = self.agent.get_treasury_status()
        balance = status['balance_wei']
        
        print(f"Audit Trésorerie: {balance} Wei")
        
        # Logique de décision ancrée dans la GloireBase
        if balance >= self.threshold:
            print("Action: Seuil atteint. Exécution maintenance...")
            result = self.agent.execute_treasury_maintenance()
            # Enregistrement de la preuve de maintenance dans GloireBase
            self.db.save_tx(f"MAIN-{time.time()}", {"action": "maintenance", "result": result})
            self.db.save_state()
            return result
        else:
            print("Action: Trésorerie protégée (sous seuil).")
            return "Standby"

if __name__ == "__main__":
    orchestrator = GloireOrchestrator()
    # Cycle simple sur le téléphone
    orchestrator.run_cycle()
