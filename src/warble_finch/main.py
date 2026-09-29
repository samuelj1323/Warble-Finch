from enum import Enum

from fastapi import FastAPI

from .routers.projects_router import router


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()
app.include_router(router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep learning for the win"}
    if model_name is ModelName.lenet:
        return {"model_name": model_name, "message": "Howdy partner "}
    return {"model_name": model_name, "message": "I'm left I guess"}


def main() -> None:
    print("Hello from warble-finch!")
