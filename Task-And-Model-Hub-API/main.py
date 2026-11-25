from fastapi import FastAPI, status, Body, Path, Response
from typing import Annotated
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, HttpUrl, Field

class UserBase(BaseModel):
    username : str
    email : EmailStr
    role : str = "operator"
    bio : str | None = None

class UserCreate (UserBase):
    password : str


app = FastAPI()

users_db : dict[str,dict] = {}
tasks_db : dict[int,dict] = {}

@app.post("/users/", status_code= status.HTTP_201_CREATED ,response_model=UserBase)
async def user_create(user_create : UserCreate):

    new_id = len(users_db) + 1
    record = {"id" : new_id , **user_create.model_dump()}
    users_db[user_create.username.lower()] = record
    return record 

@app.get("/users/{username}/profile",
        response_model= UserBase,
        response_model_exclude_unset=True)
async def get_user_profile(username : str):
    key = username.lower()
    if key in users_db:
        return users_db[key]
    return {"username": username, "email": "unknown@example.com"}

    #2

class EvidenceImage(BaseModel):
    url : HttpUrl
    label : str

class TaskCreate(BaseModel):
    title : str = Field(min_length=3, max_length=80)
    priority_score : float = Field(gt = 0.0, le=10.0)
    tags : set[str] = set()
    evidences : list [EvidenceImage] |None = None

class TaskUpdate(BaseModel):
    title : str | None = Field(default= None, min_length= 3 , max_length=80)
    priority_score : float | None = Field(default=None, ge=0.0, le=10.0)
    tags : set[str] | None = None

@app.post("/tasks/", status_code=status.HTTP_201_CREATED)
async def create_task(
    task: Annotated[
        TaskCreate,
        Body(
            openapi_examples={
                "normal_gorev": {
                    "summary": "Standart saha görevi",
                    "description": "Orta öncelikli rutin kontrol görevi örneği.",
                    "value": {
                        "title": "Trafo pano kontrolü",
                        "priority_score": 5.5,
                        "tags": ["saha", "rutin"],
                        "evidences": [
                            {
                                "url": "https://example.com/pano-1.jpg",
                                "label": "Pano ön görünüm",
                            }
                        ],
                    },
                },
                "kritik_ariza": {
                    "summary": "Kritik saha arızası",
                    "description": "Yüksek öncelikli acil müdahale görevi örneği.",
                    "value": {
                        "title": "Ana hat enerji kesintisi",
                        "priority_score": 9.8,
                        "tags": ["kritik", "acil", "hat"],
                        "evidences": [
                            {
                                "url": "https://example.com/ariza-kritik.png",
                                "label": "Kesinti ölçüm kaydı",
                            }
                        ],
                    },
                },
            }
        ),
    ]
):
    new_id = max(tasks_db.keys(), default = 0)+ 1
    record = {"id": new_id, **task.model_dump()}
    tasks_db[new_id] = record
    return record

@app.post("/tasks/{task_id}/weights")
async def set_task_weights(
    task_id : Annotated[int, Path(gt=0)],
    weights : dict[int, float],

):
    task_record = tasks_db.get(task_id)
    if task_record is not None:
        task_record["weights"] = weights
    return{
        "task_id": task_id,
        "weights": weights,
        "saved_on_existing_task" : task_record is not None,
}

@app.put("/tasks/{task_id}")
async def update_task(
    task_id : Annotated[int, Path(gt = 0)],
    task_update : Annotated[TaskUpdate, Body(embed= True)],
    dry_run : bool = False
):
    existing_task = tasks_db.get(task_id, {"id": task_id})
    update_data = task_update.model_dump(exclude_unset= True)
    preview_task = {**existing_task, **update_data}

    if not dry_run:
        tasks_db[task_id] = preview_task

    return {
        "task_id": task_id,
        "dry_run": dry_run,
        "applied_changes": update_data,
        "task": preview_task
    }

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: Annotated[int, Path(gt =0)]):
    tasks_db.pop(task_id, None)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get("/health-raw", response_model = None) 
async def health_raw(raw_mode: bool = False)-> Response | dict:
    if raw_mode:
        return JSONResponse(content={"engine":"raw", "status":"healthy"})
    return {"engine":"dict", "status":"healthy"}

      
