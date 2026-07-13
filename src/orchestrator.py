import time
from .gloire_base import GloireBase
from .blockchain_agent import GloireDevIA_Web3

class GloireOrchestrator:
    def __init__(self):
        self.db = GloireBase()
        self.agent = GloireDevIA_Web3()
        # Seuil par défaut si absent du registre
        self.threshold = self.db.db.get("settings", {}).get("maintenance_threshold", 1000000000000000000)

    def run_cycle(self):
        print(f"\n--- [GloirePay] Audit {time.strftime('%Y-%m-%d %H:%M:%S')} ---")
        
        try:
            status = self.agent.get_treasury_status()
            balance = status.get('balance_wei', 0)
            
            print(f"Trésorerie Actuelle : {balance} Wei")
            
            if balance >= self.threshold:
                print("Action: Seuil atteint. Exécution maintenance...")
                result = self.agent.execute_treasury_maintenance()
                self.db.save_tx(f"MAIN-{int(time.time())}", {"action": "maintenance", "result": result})
                self.db.save_state()
            else:
                print("Action: Trésorerie protégée (sous seuil). Standby.")
        
        except Exception as e:
            print(f"Alerte Système : Erreur lors de l'audit -> {e}")

if __name__ == "__main__":
    bot = GloireOrchestrator()
    print("Système de surveillance activé sur Redmi 13.")
    
    # Boucle infinie souveraine
    while True:
        bot.run_cycle()
        print("Mise en veille (Prochain audit dans 1 heure)...")
        # 3600 secondes = 1 heure
        time.sleep(3600)
