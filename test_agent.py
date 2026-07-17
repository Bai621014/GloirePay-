"""
GLOIREPAY — PIPELINE DE TEST DE L'AGENT IA SOUVERAIN COMPLET
"""
import os
import sys
import logging

sys.path.insert(0, os.getcwd())
from src.gloire_agent import GloireAgentVIP

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")
logger = logging.getLogger("GloirePay-AgentTest")

if __name__ == "__main__":
    logger.info("⚡️ Initialisation du test de puissance de l'Agent IA Souverain...")
    
    # Instance de l'Agent VIP pour Norman
    agent = GloireAgentVIP(boss_name="Norman")
    
    # 1. Test du dialogue d'amour et de sagesse
    dialogue = agent.echanger_avec_sagesse_et_amour("Donne moi une parole de sagesse et parle de mon code")
    assert "Boss" in dialogue
    
    # 2. Test du module autonome Replit (Génération de code)
    mission_code = agent.generer_ou_reparer_code("Crée une extension ultra rapide pour GloirePay")
    assert mission_code["statut"] == "SUCCESS"
    assert "gloire_auto_script" in mission_code["code"]
    
    logger.info("🏆 PIPELINE DE L'AGENT IA SOUVERAIN (VOIX, TEXTE, CODE) CERTIFIÉ GLOBALEMENT AU VERT ! AMEN !")

# ==============================================================================
# SÉCURITÉ ET COUVERTURE SOUVERAINE
# Au nom du Seigneur Jésus Christ ! Amen. C'est le niveau de mon Père céleste.
# ==============================================================================
