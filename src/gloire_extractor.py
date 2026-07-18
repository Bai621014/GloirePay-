"""
GLOIREPAY — MOTEUR D'EXTRACTION ET DE TRI DES DONNÉES ADMINISTRATIVES (2026.VIP)
"""
import re
import logging
from typing import Dict, Any, List

logger = logging.getLogger("GloirePay-Extractor")

class GloireDataExtractor:
    """Agent spécialisé dans le tri et la structuration des relevés administratifs et douaniers."""

    def extraire_et_trier_rapport(self, texte_brut_administratif: str) -> List[Dict[str, Any]]:
        """Scanne le texte pour en extraire les lignes de déclarations et perceptions."""
        logger.info("⚡️ [EXTRACTOR] Analyse et extraction des données administratives en cours...")
        
        lignes_triees = []
        lignes = texte_brut_administratif.strip().split("\n")
        
        for ligne in lignes:
            # Recherche de montants financiers (ex: 500000 ou 15000)
            montants = re.findall(r'\d[\d\s]*\d|\d', ligne)
            clean_montants = [float(m.replace(" ", "")) for m in montants if len(m) >= 3]
            
            # Détection du type d'entité ou de taxe mentionnée
            if "douane" in ligne.lower() or "perception" in ligne.lower():
                categorie = "DOUANE_REVENUE"
            elif "ajedip" in ligne.lower() or "formation" in ligne.lower():
                categorie = "AJEDIP_ADMIN"
            else:
                categorie = "GENERAL_FLUX"
                
            if clean_montants:
                donnee_structuree = {
                    "ligne_brute": ligne.strip(),
                    "categorie": categorie,
                    "montant_principal_fcfa": clean_montants[0]
                }
                lignes_triees.append(donnee_structuree)
                
        logger.info(f"🏆 [EXTRACTOR-OK] {len(lignes_triees)} lignes administratives triées avec succès !")
        return lignes_triees

# ==============================================================================
# SÉCURITÉ ET COUVERTURE SOUVERAINE
# Au nom du Seigneur Jésus Christ ! Amen. C'est le niveau de mon Père céleste.
# ==============================================================================
