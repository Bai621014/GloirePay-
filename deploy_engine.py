import json
import sys
import os
import traceback

# Importations directes (structure plate)
from web3_manager import verifier_tresorerie
from gloire_hub import calculer_valeur_fcfa 

def run_gloiretech():
    print("--- [GloireTech] Initialisation Souveraine ---")
    
    try:
        # 1. Chargement de la configuration souveraine
        with open('registry.json', 'r') as f:
            config = json.load(f)
        print(f"Connexion au réseau : {config['metadata']['network']}")
        
        # 2. Audit rapide du Gnosis Safe
        print("Audit du Safe en cours...")
        solde = verifier_tresorerie()
        
        # 3. Conversion intelligente via GloireHub
        print("Calcul de la valeur souveraine en FCFA...")
        valeur_fcfa = calculer_valeur_fcfa(solde)
        
        # 4. Rapport Pro VIP
        print(f"--- RAPPORT DE TRÉSORERIE ---")
        print(f"Solde actuel : {solde} MATIC")
        print(f"Valeur estimée : {valeur_fcfa} FCFA")
        print("Système stable : Prêt pour déploiement automatique.")
        
    except Exception as e:
        print(f"Erreur lors de l'exécution souveraine : {e}")
        traceback.print_exc()

if __name__ == "__main__":
    run_gloiretech()
