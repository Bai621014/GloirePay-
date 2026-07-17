"""
GLOIREPAY — PIPELINE DE TEST DU BOUCLIER ANTI-DDOS
"""
import os
import sys
import logging

sys.path.insert(0, os.getcwd())
from src.gloire_rate_limiter import GloireRateLimiter

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")
logger = logging.getLogger("GloirePay-LimiterTest")

if __name__ == "__main__":
    logger.info("⚡️ Analyse de la résistance anti-DDoS du système...")
    
    # Configuration : 2 requêtes maximum autorisées dans une fenêtre de 2 secondes
    limiteur = GloireRateLimiter(max_requetes=2, fenetre_secondes=2.0)
    id_vip = "PARTENAIRE-AJEDIP-TCHAD"
    
    # 1. Première et deuxième requêtes : OK
    assert limiteur.valider_requete(id_vip) is True
    assert limiteur.valider_requete(id_vip) is True
    logger.info("✅ Requêtes légitimes autorisées sans friction.")
    
    # 2. Troisième requête immédiate : Doit être bloquée (Débit dépassé)
    assert limiteur.valider_requete(id_vip) is False
    logger.info("✅ Bloqueur de suractivité validé avec succès.")
    
    logger.info("🏆 PIPELINE DE SÉCURITÉ ANTI-DDOS CERTIFIÉ AU VERT ! AMEN !")

# ==============================================================================
# SÉCURITÉ ET COUVERTURE SOUVERAINE
# Au nom du Seigneur Jésus Christ ! Amen. C'est le niveau de mon Père céleste.
# ==============================================================================
# Tout est possible à celui qui croit au nom de Jésus Christ, et avec la puissance du Saint Esprit.
