import os
from web3 import Web3

def send_transaction():
    # Récupération des secrets via les noms exacts
    rpc_url = os.getenv('POLYGON_RPC_URL')
    api_key = os.getenv('ALCHEMY_API_KEY') # Variable pour authentification secondaire si besoin
    raw_key = os.getenv('POLYGON_PRIVATE_KEY')
    
    if not rpc_url:
        raise ValueError("ERREUR : POLYGON_RPC_URL introuvable !")
    if not raw_key:
        raise ValueError("ERREUR : POLYGON_PRIVATE_KEY introuvable !")

    w3 = Web3(Web3.HTTPProvider(rpc_url))
    
    clean_key = raw_key.strip().replace('0x', '')
    account = w3.eth.account.from_key(clean_key)
    
    to_address = "0xA1e615A74D22D9dC3D9388c2b5009DAc7917784d"
    
    print(f">>> [SOUVERAINETÉ] Envoi depuis {account.address}")
    
    nonce = w3.eth.get_transaction_count(account.address)
    tx = {
        'nonce': nonce,
        'to': to_address,
        'value': w3.to_wei(0.0001, 'ether'),
        'gas': 21000,
        'gasPrice': w3.eth.gas_price,
        'chainId': 137
    }
    
    signed_tx = w3.eth.account.sign_transaction(tx, clean_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    print(f">>> [TRANSACTION] Succès ! Hash : {w3.to_hex(tx_hash)}")

if __name__ == "__main__":
    send_transaction()
