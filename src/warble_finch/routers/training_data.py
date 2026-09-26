from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/training_data")


@router.get("/{id}")
def get_training_data(id: int) -> list[str]:
    return []


@router.post("/upload/{id}")
def upload_training_data_to_id(id: int):
    print(f"Uploading...{id}")
