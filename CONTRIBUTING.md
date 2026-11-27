# Règles de travail du groupe

## 1. Un dossier = un propriétaire

| Dossier | Propriétaire |
|---|---|
| `backend/` | Daniel |
| `mobile-client/` | Daniel |
| `mobile-livreur/` | Meruem |
| `web/` | à attribuer |
| racine, `docs/`, `.github/` | tout le groupe (PR obligatoire) |

On ne modifie pas le dossier d'un autre. Besoin d'un changement chez quelqu'un
(ex. un nouvel endpoint) → ouvrir une *issue* GitHub et l'assigner au propriétaire.

## 2. Branches

- `main` : toujours fonctionnelle. **Personne ne pousse directement dessus.**
- Une branche par tâche, préfixée par la partie :

```
backend/auth-2fa
backend/commandes
client/catalogue
livreur/saisie-livraison
web/tableau-de-bord
docs/mcd
```

## 3. Cycle d'une tâche

```powershell
git switch main
git pull
git switch -c client/catalogue      # nouvelle branche
# ... travail, commits ...
git push -u origin client/catalogue
# puis ouvrir une Pull Request vers main sur GitHub
```

Avant d'ouvrir la PR, se remettre à jour : `git pull origin main` sur sa branche.

## 4. Messages de commit

Format court : `type(partie): description`

```
feat(backend): endpoint POST /auth/login
fix(client): calcul du total du panier
docs: ajout du MCD
chore(livreur): mise à jour des dépendances
```

Types : `feat`, `fix`, `docs`, `refactor`, `test`, `chore`.

## 5. Cohérence entre les parties

- **API** : les noms des champs JSON sont en `snake_case`, les montants en entier FCFA (pas de décimales),
  les dates en ISO 8601 UTC (`2026-11-27T12:50:00Z`).
- **Endpoints** préfixés par `/api/v1`.
- Toute modification d'un endpoint existant = mise à jour de `docs/api/openapi.json` dans la même PR,
  et prévenir les autres sur le groupe.
- Les secrets (`.env`, clés, mots de passe) ne sont **jamais** commités. On commite `.env.example`.
