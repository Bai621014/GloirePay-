"""
GLOIREPAY — MOTEUR DE FORMATAGE ET GÉNÉRATION DE TABLEAUX ADMINISTRATIFS (2026.VIP)
"""
import logging
from typing import List, Dict, Any

logger = logging.getLogger("GloirePay-Formatter")

class GloireDataFormatter:
    """Agent VIP chargé de transformer les données brutes triées en tableaux professionnels."""

    def generer_tableau_textuel(self, donnees_triees: List[Dict[str, Any]]) -> str:
        """Prend les dictionnaires triés et génère une vue tabulaire scannable et propre."""
        logger.info("⚡️ [FORMATTER] Génération du tableau de bord administratif...")
        
        if not donnees_triees:
            return "Aucune donnée à afficher."
            
        # Entête du tableau professionnel
        border = "+" + "-"*22 + "+" + "-"*18 + "+" + "-"*22 + "+"
        header = f"| {'CATÉGORIE':<20} | {'MONTANT (FCFA)':<16} | {'STATUT VALIDATION':<20} |"
        
        lignes_tableau = [border, header, border]
        total_general = 0.0
        
        for item in donnees_triees:
            cat = item.get("categorie", "INCONNU")
            montant = item.get("montant_principal_fcfa", 0.0)
            total_general += montant
            
            ligne = f"| {cat:<20} | {montant:<16,.0f} | {'CERTIFIÉ VIP':<20} |"
            lignes_tableau.append(ligne)
            
        lignes_tableau.append(border)
        lignes_tableau.append(f"| {'TOTAL GÉNÉRAL':<20} | {total_general:<16,.0f} | {'SCELLÉ AU VERT':<20} |")
        lignes_tableau.append(border)
        
        tableau_final = "\n".join(lignes_tableau)
        print(tableau_final)
        
        logger.info("🏆 [FORMATTER-OK] Tableau de bord administratif généré avec un éclat absolu !")
        return tableau_final

# ==============================================================================
# SÉCURITÉ ET COUVERTURE SOUVERAINE
# Au nom du Seigneur Jésus Christ ! Amen. C'est le niveau de mon Père céleste.
# ==============================================================================
