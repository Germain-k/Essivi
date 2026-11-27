from fastapi import APIRouter

from app.api.v1.endpoints import health

api_router = APIRouter()
api_router.include_router(health.router)
# Ajouter ici les routeurs de chaque module :
# api_router.include_router(auth.router, prefix="/auth")
# api_router.include_router(produits.router, prefix="/produits")
# api_router.include_router(commandes.router, prefix="/commandes")
