# GloireDevIA

GloireDevIA est un agent d'audit et d'analyse conçu pour assister les équipes techniques et métiers dans l'évaluation de conformité et de sécurité en s'appuyant sur les six piliers pertinents pour l'écosystème ISO 20022.

## Mission de l'agent
L'objectif principal de GloireDevIA est de fournir :
- Une analyse rapide d'artefacts applicatifs via une API simple.
- Un audit initial basé sur les 6 piliers ISO 20022 pour détecter les lacunes évidentes.
- Un point d'entrée extensible pour intégrer des contrôles plus approfondis et automatisés.

## Les 6 piliers (ISO 20022 — adaptation contextuelle)
1. Gouvernance — Politiques et responsabilités.
2. Confidentialité — Protection des données et chiffrement.
3. Intégrité — Mécanismes assurant que les données ne sont pas altérées.
4. Disponibilité — Surveillance, haute disponibilité et reprise.
5. Traçabilité — Journalisation et traçage des opérations.
6. Conformité — Documentation et alignement réglementaire.

## Structure du projet
- src/ : code applicatif (agent, audit, API Flask).
- tests/ : tests unitaires (pytest).
- requirements.txt, Procfile, runtime.txt : fichiers nécessaires pour le déploiement.

## Déploiement sur Render
1. Connectez votre dépôt GitHub à Render.
2. Créez un nouveau Web Service :
   - Environment : Python
   - Build Command : pip install -r requirements.txt
   - Start Command : gunicorn src.app:app (Render utilisera aussi le Procfile si présent)
   - Runtime : Python 3.11 (Render prend en charge runtime.txt)
3. Variables d'environnement : ajoutez les clés nécessaires si vous étendez l'agent (ex. API keys).
4. Tester l'application :
   - Endpoint de santé : GET /health
   - Exemple d'appel : curl -X POST https://<votre-service>.onrender.com/analyze -d '{"foo":"bar"}' -H "Content-Type: application/json"

## Tests
- Exécuter les tests localement :
  - pip install -r requirements.txt
  - pip install pytest
  - pytest -q

## Extension
Ce squelette est conçu pour être étendu : ajout de vrais contrôles d'audit, intégration CI/CD, gestion des secrets, monitoring et règles de sécurité renforcées.
