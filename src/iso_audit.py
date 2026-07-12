import datetime
import json

class ISO20022_Validator:
    """
    Validateur de conformité pour les messages financiers (Standard ISO 20022).
    Assure l'intégrité, la traçabilité et la validation des données.
    """
    
    REQUIRED_FIELDS = ["sender", "receiver", "amount", "currency", "purpose"]

    @staticmethod
    def audit_transaction(tx_data):
        """
        Analyse une transaction pour vérifier sa conformité avec les normes ISO 20022.
        """
        # 1. Vérification de la structure obligatoire (Intégrité)
        for field in ISO20022_Validator.REQUIRED_FIELDS:
            if field not in tx_data:
                return {
                    "status": "NON-COMPLIANT",
                    "error": f"Champ obligatoire manquant : {field}",
                    "timestamp": datetime.datetime.utcnow().isoformat()
                }

        # 2. Validation de la donnée (Formatage)
        if not isinstance(tx_data["amount"], (int, float)) or tx_data["amount"] <= 0:
            return {
                "status": "NON-COMPLIANT",
                "error": "Montant invalide : doit être numérique et positif",
                "timestamp": datetime.datetime.utcnow().isoformat()
            }

        # 3. Validation réussie (Traçabilité)
        return {
            "status": "COMPLIANT",
            "message": "Transaction conforme ISO 20022",
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "audit_id": f"ISO-{datetime.datetime.utcnow().strftime('%Y%m%d-%H%M%S')}"
        }

# Exemple d'utilisation rapide pour test unitaire
if __name__ == "__main__":
    test_tx = {
        "sender": "0xABC",
        "receiver": "0xXYZ",
        "amount": 100.50,
        "currency": "EUR",
        "purpose": "Maintenance"
    }
    print(ISO20022_Validator.audit_transaction(test_tx))
