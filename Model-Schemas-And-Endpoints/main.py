from enum import StrEnum
from pydantic import BaseModel
from fastapi import FastAPI, Query, Path
from typing import Annotated

class ModelFamily(StrEnum):
    llm = "llm"
    vision = "vision"
    tabular = "tabular"

class InferenceRequest(BaseModel):
    prompt : str
    max_tokens : int = 256
    tags : list[str] = []

class ModelUpdate(BaseModel):
    name : str 
    description : str | None = None
    temperature : float 
    active : bool = True

app = FastAPI()

@app.get("/models/{family}")
async def get_models(family : ModelFamily,
                     top_k : Annotated[int, Query(ge=1, le=50)] = 5,
                     labels : Annotated[list[str] | None, Query(alias="model-label")] = None):
    return {
        "family" : family,
        "top_k" : top_k,        
        "labels" : labels   
        }

@app.post("/models/{family}/predict")
async def get_predict(family : ModelFamily, playload : InferenceRequest):
    playload_dict = playload.model_dump()
    return {
        "family" : family,
        "prediction_id" : "1234",
        "request" : playload_dict,
        "output": f"[{family.value}] Simüle edilmiş yanıt: {playload.prompt[:40]}"
    }

@app.put("/models/{model_id}")
async def update_model(
    model_id: Annotated[int, Path(gt=0)],
    model_data: ModelUpdate,
    dry_run: bool = False,
):
    return {
        "model_id": model_id,
        "dry_run": dry_run,
        "updated_fields": model_data.model_dump(),
    }