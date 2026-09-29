from pydantic import BaseModel


class Project(BaseModel):
    projectId: str
    projectName: str
