import sys
import os
import json
import traceback

# Force le répertoire courant dans le chemin de recherche Python
sys.path.insert(0, os.getcwd())

# Importation corrigée : on passe par le dossier 'src' comme demandé
from src.web3_manager import verifier_tresorerie
from src.gloire_hub import calculer_valeur_fcfa 

def run_gloiretech():
    print("--- [GloireTech] Initialisation Souveraine ---")
    
    try:
        # Chargement du registre depuis la racine
        with open('registry.json', 'r') as f:
            config = json.load(f)
        print(f"Connexion au réseau : {config['metadata']['network']}")
        
        # Audit et calcul
        print("Audit du Safe en cours...")
        solde = verifier_tresorerie()
        
        print("Calcul de la valeur souveraine en FCFA...")
        valeur_fcfa = calculer_valeur_fcfa(solde)
        
        # Rapport Pro VIP
        print(f"--- RAPPORT DE TRÉSORERIE ---")
        print(f"Solde actuel : {solde} MATIC")
        print(f"Valeur estimée : {valeur_fcfa} FCFA")
        print("Système stable : Déploiement réussi.")
        
    except Exception as e:
        print(f"Erreur lors de l'exécution souveraine : {e}")
        traceback.print_exc()

if __name__ == "__main__":
    run_gloiretech()
