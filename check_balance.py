import os
import sys
from web3 import Web3

def main():
    rpc_url = os.getenv('POLYGON_RPC_URL')
    if not rpc_url:
        print(">>> [ERREUR] Variable POLYGON_RPC_URL manquante.")
        sys.exit(1)

    w3 = Web3(Web3.HTTPProvider(rpc_url))
    if not w3.is_connected():
        print(">>> [ERREUR] Impossible de se connecter au réseau.")
        sys.exit(1)

    wallet_address = "0xA1e615A74D22D9dC3D9388c2b5009DAc7917784d"
    checksum_address = Web3.to_checksum_address(wallet_address)

    try:
        balance_wei = w3.eth.get_balance(checksum_address)
        balance_eth = w3.from_wei(balance_wei, 'ether')
        print(f"\n--- [GLOIREPAY] État de la Trésorerie ---")
        print(f"Adresse : {checksum_address}")
        print(f"Solde : {balance_eth:.6f} MATIC")
        print(f"----------------------------------------\n")
    except Exception as e:
        print(f">>> [ERREUR] Lecture solde impossible : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
