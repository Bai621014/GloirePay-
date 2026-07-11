"""Audit des 6 piliers ISO 20022 — module utilitaire."""

from typing import Dict, List

PILIERS = [
    "Gouvernance",
    "Confidentialité",
    "Intégrité",
    "Disponibilité",
    "Traçabilité",
    "Conformité"
]

class SecurityAudit:
    """Fournit un audit minimal basé sur les 6 piliers ISO 20022."""

    def __init__(self) -> None:
        self.piliers = PILIERS

    def audit(self, context: Dict[str, any]) -> Dict[str, List[str]]:
        """Retourne un rapport simple listant pour chaque pilier des observations.

        Le context peut contenir des clés comme 'policies', 'logs', 'access_control'.
        Cette implémentation est volontairement légère — à enrichir en production.
        """
        report = {}
        # Règles heuristiques minimales pour l'exemple
        for p in self.piliers:
            findings = []
            if p == "Gouvernance":
                if not context.get("policies"):
                    findings.append("Aucune politique documentée détectée.")
            if p == "Confidentialité":
                if not context.get("encryption"):
                    findings.append("Chiffrement des données non confirmé.")
            if p == "Intégrité":
                if not context.get("checksums") and not context.get("signatures"):
                    findings.append("Absence de mécanismes d'intégrité identifiés.")
            if p == "Disponibilité":
                if not context.get("monitoring"):
                    findings.append("Surveillance/monitoring non configuré.")
            if p == "Traçabilité":
                if not context.get("logging"):
                    findings.append("Journaux/traces manquants ou insuffisants.")
            if p == "Conformité":
                if not context.get("compliance_docs"):
                    findings.append("Documents de conformité absents.")
            report[p] = findings or ["Aucune anomalie majeure détectée (vérifier en profondeur)."]
        return report
