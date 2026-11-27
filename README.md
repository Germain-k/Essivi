# ESSIVIVI — Plateforme de gestion et de reporting des ventes de boissons

Projet de groupe (Programmation distribuée). Une seule API, une seule base de données, quatre clients.

```
┌────────────┐ ┌────────────────┐ ┌───────────────┐
│ web/       │ │ mobile-livreur/│ │ mobile-client/│   Couche présentation
└─────┬──────┘ └───────┬────────┘ └───────┬───────┘
      └────────────────┼──────────────────┘
                 HTTPS / JSON (REST)
                ┌──────┴──────┐
                │  backend/   │   FastAPI — logique métier, 2FA, indicateurs
                └──────┬──────┘
                ┌──────┴──────┐
                │ PostgreSQL  │   Base de données unique
                └─────────────┘
```

Règle d'architecture : **aucune application ne parle directement à la base**, tout passe par l'API.

## Arborescence

| Dossier | Contenu | Techno | Responsable |
|---|---|---|---|
| [backend/](backend/) | API REST, modèles, migrations, tests | FastAPI + SQLAlchemy + PostgreSQL | Daniel |
| [mobile-client/](mobile-client/) | App des clients (bars, restaurants…) | Flutter | Daniel |
| [mobile-livreur/](mobile-livreur/) | App des agents commerciaux / livreurs | Flutter | Meruem |
| [web/](web/) | App gestionnaire + administration | à définir | à attribuer |
| [docs/](docs/) | Cahier des charges, conception (UML, MCD), contrat d'API | — | tous |

Chaque membre ne modifie **que son dossier**. Ce qui est partagé (racine, `docs/`) passe par une
pull request relue par au moins un autre membre. Voir [CONTRIBUTING.md](CONTRIBUTING.md).

## Démarrage rapide

```powershell
# Base de données (si Docker est installé ; sinon PostgreSQL installé localement)
docker compose up -d db

# API
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
# → documentation interactive : http://127.0.0.1:8000/docs
```

## Contrat d'API

La source de vérité est le schéma OpenAPI généré par FastAPI (`/openapi.json`).
Une copie est versionnée dans [docs/api/openapi.json](docs/api/) à chaque changement d'endpoint,
pour que les équipes mobile et web puissent travailler sans lancer le backend.
