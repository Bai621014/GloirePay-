import logging
import os
from web3 import Web3
from web3.exceptions import Web3Exception

# Configuration du logger
logger = logging.getLogger("SovereignManager")

class GloireWeb3Manager:
    """Gestionnaire de trésorerie haute performance pour Safe Infrastructure."""
    
    def __init__(self, rpc_url: str):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.safe_address = Web3.to_checksum_address("0xA1e615A74D22D9dC3D9388c2b5009DAc7917784d")

    def estimate_maintenance_cost(self) -> int:
        try:
            gas_price = self.w3.eth.gas_price
            return gas_price * 21000
        except Web3Exception as e:
            logger.error(f"Erreur estimation coût : {e}")
            return 0

    def get_treasury_status(self) -> dict:
        if not self.w3.is_connected():
            return {"status": "ERROR", "message": "Nœud RPC injoignable"}
        
        try:
            balance = self.w3.eth.get_balance(self.safe_address)
            balance_eth = self.w3.from_wei(balance, 'ether')
            is_compliant = balance_eth >= 0.0001
            
            return {
                "status": "COMPLIANT" if is_compliant else "NON-COMPLIANT",
                "balance_eth": float(balance_eth),
                "safe_address": self.safe_address
            }
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

# --- FONCTION COMPATIBLE AVEC DEPLOY_ENGINE ---
def verifier_tresorerie():
    """Fonction wrapper pour assurer la compatibilité avec le moteur."""
    rpc_url = os.getenv('POLYGON_RPC_URL')
    if not rpc_url:
        raise Exception("Variable d'environnement POLYGON_RPC_URL manquante.")
        
    manager = GloireWeb3Manager(rpc_url)
    status = manager.get_treasury_status()
    
    if status["status"] == "ERROR":
        raise Exception(f"Audit Trésorerie Échoué : {status['message']}")
    
    return status["balance_eth"]
