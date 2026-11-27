# Documentation

| Dossier | Contenu |
|---|---|
| `cahier-des-charges/` | Cahier des charges validé (PDF) |
| `conception/` | Cas d'utilisation, diagrammes de séquence et de classes, MCD/MLD, maquettes |
| `api/` | `openapi.json` exporté depuis le backend (contrat entre l'API et les apps) |

Exporter le contrat d'API (backend lancé) :

```powershell
curl http://127.0.0.1:8000/openapi.json -o docs/api/openapi.json
```
