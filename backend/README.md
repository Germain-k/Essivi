# Backend — API FastAPI

```
backend/
├── app/
│   ├── main.py            # création de l'app FastAPI, CORS, montage des routes
│   ├── core/              # configuration, sécurité (JWT, hachage, OTP)
│   ├── db/                # connexion PostgreSQL, Base SQLAlchemy
│   ├── models/            # tables SQLAlchemy (une entité du §9 = un fichier)
│   ├── schemas/           # schémas Pydantic (entrées / sorties JSON)
│   ├── services/          # logique métier (règles RG1 à RG13)
│   └── api/v1/
│       ├── router.py      # regroupe tous les routeurs
│       └── endpoints/     # un fichier par ressource (auth, produits, commandes…)
├── alembic/               # migrations de la base (à initialiser)
├── tests/
├── requirements.txt
└── .env.example
```

Flux d'une requête : `endpoints/` → `services/` → `models/` (base) ; les données entrent/sortent via `schemas/`.

## Lancer

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

- Documentation interactive : http://127.0.0.1:8000/docs
- Tests : `pytest`
