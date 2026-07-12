import os
from src.blockchain_agent import GloireDevIA_Web3

class GloireOrchestrator:
    def __init__(self):
        self.agent = GloireDevIA_Web3()
        # Seuil minimal en Wei (1 MATIC = 10^18 Wei)
        self.threshold = 1000000000000000000 

    def run_cycle(self):
        status = self.agent.get_treasury_status()
        print(f"Audit: Trésorerie à {status['balance_wei']} Wei")
        
        # Logique de décision souveraine
        if status['balance_wei'] >= self.threshold:
            print("Action: Seuil atteint. Déclenchement maintenance.")
            return self.agent.execute_treasury_maintenance()
        else:
            print("Action: Trésorerie sous le seuil. Aucune action.")
            return "Standby"

if __name__ == "__main__":
    bot = GloireOrchestrator()
    bot.run_cycle()
