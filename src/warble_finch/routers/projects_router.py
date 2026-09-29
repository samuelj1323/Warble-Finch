from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/projects")


class Project(BaseModel):
    projectId: str
    projectName: str


projects: list[Project] = [
    Project(projectId="1", projectName="project-1"),
    Project(projectId="2", projectName="project-2"),
]


@router.get("/")
def get_all_projects() -> list[Project]:
    return projects


@router.get("/{project_id}")
def get_project(project_id: str) -> Project | str:
    try:
        for project in projects:
            if project.projectId == project_id:
                return project
    except ValueError as e:
        return "Value-Error"
    return "Value-Error"


@router.post("/projects/")
def add_new_project(new_project: Project):
    try:
        projects.append(new_project)
    except ValueError as e:
        return e
    return projects
