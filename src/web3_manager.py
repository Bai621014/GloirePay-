import logging
from web3 import Web3
from web3.exceptions import Web3Exception

# Configuration du logger pour le mode souverain
logger = logging.getLogger("SovereignManager")

class GloireWeb3Manager:
    """Gestionnaire de trésorerie haute performance pour Safe Infrastructure."""
    
    def __init__(self, rpc_url: str):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        # Adresse de votre Gnosis Safe
        self.safe_address = Web3.to_checksum_address("0xA1e615A74D22D9dC3D9388c2b5009DAc7917784d")

    def estimate_maintenance_cost(self) -> int:
        """Estime le coût d'une transaction standard pour maintenance."""
        try:
            gas_price = self.w3.eth.gas_price
            return gas_price * 21000 # Gas limit standard
        except Web3Exception as e:
            logger.error(f"Erreur estimation coût : {e}")
            return 0

    def get_treasury_status(self) -> dict:
        """Audit instantané de l'intégrité de la trésorerie."""
        if not self.w3.is_connected():
            return {"status": "ERROR", "message": "Nœud RPC injoignable"}
        
        try:
            balance = self.w3.eth.get_balance(self.safe_address)
            balance_eth = self.w3.from_wei(balance, 'ether')
            
            # Seuil de conformité opérationnelle
            is_compliant = balance_eth >= 0.0001
            
            return {
                "status": "COMPLIANT" if is_compliant else "NON-COMPLIANT",
                "balance_eth": float(balance_eth),
                "safe_address": self.safe_address
            }
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}
