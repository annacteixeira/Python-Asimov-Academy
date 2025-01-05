from pydantic import BaseModel

class Job(BaseModel):
    id: str
    name: str
    main_activities: str
    pre_requisites: str
    differentials: str