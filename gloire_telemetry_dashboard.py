Import os
from web3 import Web3

class GloirePayVIPDashboard:
    """Moteur VIP de confirmation flash et de lecture de solde en temps réel."""
    def __init__(self):
        # Connexion souveraine au nœud RPC Polygon configuré dans vos variables GitHub
        self.rpc_url = os.environ.get("RPC_URL", "https://polygon-rpc.com")
        self.w3 = Web3(Web3.HTTPProvider(self.rpc_url))
        
        # Vos coordonnées souveraines et immuables
        self.wallet_boss = "0xA1e615A74D22D9dC3D9388c2b5009DAc7917784d"
        self.phone_airtel = "+23562101468"
        self.phone_moov = "+23590784260"
        
        # Taux de la trésorerie fixe
        self.matic_rate = 0.55
        self.fcfa_rate = 655.957

    def fetch_real_time_balances(self) -> dict:
        """Lit la blockchain à la vitesse de l'éclair et calcule les équivalences de votre trésorerie."""
        if not self.w3.is_connected():
            return {"status": "OFFLINE", "error": "Nœud RPC inaccessible"}

        # 1. Lecture du solde MATIC réel sur le réseau Polygon
        balance_wei = self.w3.eth.get_balance(self.wallet_boss)
        balance_matic = self.w3.from_wei(balance_wei, 'ether')
        
        # 2. Conversion financière instantanée VIP (Trésorerie Globale)
        balance_usd = float(balance_matic) * self.matic_rate
        balance_fcfa = balance_usd * self.fcfa_rate

        return {
            "status": "ONLINE",
            "wallet": self.wallet_boss,
            "balances": {
                "MATIC": round(float(balance_matic), 4),
                "USD_VAL": round(balance_usd, 2),
                "FCFA_VAL": round(balance_fcfa, 2)
            },
            "channels": {
                "Airtel_Money": self.phone_airtel,
                "Moov_Money": self.phone_moov
            }
        }

    def render_vip_interface_data(self):
        """Formate l'affichage concret destiné à être projeté sur votre Interface Pro VIP."""
        data = self.fetch_real_time_balances()
        if data["status"] == "OFFLINE":
            print("[ERREUR SYSTEME] Synchronisation impossible.")
            return

        print("\n" + "="*50)
        print(" 👑  GLOIREPAY CENTRAL — INTERFACE PRO WEB3 VIP  👑")
        print("="*50)
        print(f"📡 STATUT DU RÉSEAU  : [ VERT ABSOLU ]")
        print(f"🔑 ADRESSE METAMASK  : {data['wallet']}")
        print(f"💰 SOLDE DISPONIBLE  : {data['balances']['MATIC']} MATIC")
        print(f"💵 VALEUR EN DOLLARS : {data['balances']['USD_VAL']} $")
        print(f"🇨🇫 ÉQUIVALENT TRÉSOR : {data['balances']['FCFA_VAL']:,} XAF FCFA")
        print("-"*50)
        print(f"📲 ROUTAGE AIRTEL    : {data['channels']['Airtel_Money']} -> ACTIF")
        print(f"📲 ROUTAGE MOOV      : {data['channels']['Moov_Money']} -> ACTIF")
        print("="*50 + "\n")

if __name__ == "__main__":
    vip_engine = GloirePayVIPDashboard()
    # Déclenchement et affichage immédiat de l'état des comptes
    vip_engine.render_vip_interface_data()
