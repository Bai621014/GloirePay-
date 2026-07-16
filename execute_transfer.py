import os
from web3 import Web3

def send_transaction():
    # 1. Connexion au nœud (via Alchemy)
    w3 = Web3(Web3.HTTPProvider(os.getenv('POLYGON_RPC_URL')))
    
    # 2. Chargement et nettoyage de la clé privée (SÉCURITÉ MAXIMALE)
    raw_key = os.getenv('PRIVATE_KEY')
    # On nettoie tout caractère invisible, espace ou préfixe 0x
    clean_key = raw_key.strip().replace('0x', '')
    account = w3.eth.account.from_key(clean_key)
    
    # 3. Adresse de destination
    to_address = "0xA1e615A74D22D9dC3D9388c2b5009DAc7917784d"
    
    print(f">>> [SOUVERAINETÉ] Préparation du transfert depuis {account.address} vers {to_address}")
    
    # 4. Préparation de la transaction
    tx = {
        'nonce': w3.eth.get_transaction_count(account.address),
        'to': to_address,
        'value': w3.to_wei(0.0001, 'ether'), # Montant à envoyer (ajustez selon votre besoin)
        'gas': 21000,
        'gasPrice': w3.eth.gas_price,
        'chainId': 137 # Réseau Polygon Mainnet
    }
    
    # 5. Signature et envoi
    signed_tx = w3.eth.account.sign_transaction(tx, clean_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    print(f">>> [TRANSACTION] Succès ! Hash : {w3.to_hex(tx_hash)}")

if __name__ == "__main__":
    send_transaction()
