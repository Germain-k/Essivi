from fastapi import APIRouter

router = APIRouter(tags=["santé"])


@router.get("/health")
def health() -> dict[str, str]:
    """Vérifie que l'API répond (utilisé par les apps et le déploiement)."""
    return {"status": "ok"}
