"""
GLOIREPAY — MANIFESTE DE SÉCURITÉ ABSOLUE (2026.VIP)
"""
import os
import logging
from dotenv import load_dotenv

logger = logging.getLogger("GloirePay-Security")

class GloireSecurityManager:
    """Gestionnaire d'élite pour la protection absolue des clés privées et secrets d'API."""
    
    def __init__(self):
        # Charge le fichier .env de manière sécurisée en local
        load_dotenv()
        self.verifier_integrite_environnement()

    def verifier_integrite_environnement(self):
        """S'assure que toutes les clés stratégiques sont présentes sans les afficher."""
        cles_obligatoires = ["GLOIRE_PRIVATE_KEY", "AIRTEL_API_SECRET", "MOOV_API_SECRET"]
        manquantes = [cle for cle in cles_obligatoires if not os.getenv(cle)]
        
        if manquantes:
            logger.warning(f"⚠️ [ALERTE SÉCURITÉ] Variables manquantes dans l'environnement : {manquantes}")
        else:
            logger.info("🔒 [SÉCURITÉ-VIP] Environnement cryptographique étanche et conforme. Prêt pour la production.")

    def obtenir_cle_privee(self) -> str:
        """Récupère la clé privée de signature Blockchain sans fuite de mémoire."""
        cle = os.getenv("GLOIRE_PRIVATE_KEY")
        if not cle:
            raise ValueError("ERREUR CRITIQUE : La clé privée Web3 est introuvable ou corrompue.")
        return cle

    def obtenir_secret_telecom(self, operateur: str) -> str:
        """Récupère de manière isolée le jeton d'accès Airtel ou Moov Africa."""
        nom_variable = f"{operateur.upper()}_API_SECRET"
        secret = os.getenv(nom_variable)
        if not secret:
            raise ValueError(f"ERREUR CRITIQUE : Le secret marchand pour {operateur} est manquant.")
        return secret
