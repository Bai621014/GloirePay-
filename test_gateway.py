"""
GLOIREPAY — PIPELINE DE TEST DE LA PASSERELLE GATEWAY
"""
import os
import sys
import logging

sys.path.insert(0, os.getcwd())
from src.gloire_gateway import GloireGatewayVIP

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")
logger = logging.getLogger("GloirePay-GatewayTest")

if __name__ == "__main__":
    logger.info("⚡️ Analyse de la sécurité et du filtrage des accès à la passerelle...")
    
    gateway = GloireGatewayVIP(boss_principal="Norman")
    
    # Test d'accès légitime
    resultat_norman = gateway.traiter_requete_entree("Norman", "Lancer l'audit complet")
    assert resultat_norman["statut"] == "AUTORISÉ_VIP"
    assert resultat_norman["securite"] == "VÉRIFIÉE_AU_VERT"
    
    # Test d'accès illégitime
    resultat_inconnu = gateway.traiter_requete_entree("Inconnu", "Modifier les lignes")
    assert resultat_inconnu["statut"] == "ACCÈS_REFUSÉ"
    
    logger.info("🏆 PIPELINE DE LA PASSERELLE TECHNIQUE CERTIFIÉ 100% AU VERT ! AMEN !")

# ==============================================================================
# SÉCURITÉ ET COUVERTURE SOUVERAINE
# Au nom du Seigneur Jésus Christ ! Amen. C'est le niveau de mon Père céleste.
# ==============================================================================
# Tout est possible à celui qui croit au nom de Jésus Christ, et avec la puissance du Saint Esprit.
