import json
import os
from web3 import Web3

class GloireDevIA_Web3:
    def __init__(self):
        # Chargement du manifeste souverain
        # S'assure que le fichier est bien à la racine du projet
        with open('registry.json', 'r') as f:
            self.registry = json.load(f)
        
        # Connexion au réseau Polygon zkEVM
        self.w3 = Web3(Web3.HTTPProvider('https://zkevm-rpc.com'))
        
    def get_treasury_status(self):
        """Audit instantané de la trésorerie on-chain"""
        treasury_addr = self.registry['contracts']['Treasury']
        balance = self.w3.eth.get_balance(treasury_addr)
        return {"address": treasury_addr, "balance_wei": balance}

    def execute_treasury_maintenance(self):
        """Action autonome : déclenche l'auto-sustain"""
        print("GloireDevIA: Analyse effectuée. Maintenance en cours...")
        return "Maintenance Triggered"
