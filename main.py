import datetime
import sqlalchemy
import databases
from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

config = context.config
fileConfig(config.config_file_name)

app = FastAPI()
"""
username
email
created_at
updated_at
"""

class User(BaseModel):
    username: str
    email: Optional[str] = None
    price: float
    tax: Optional[float] = None
    #created_at: datetime.datetime
    #updated_at: datetime.datetime
'''
title
type: ChoiceField (e.g. text or image)
created_by
create_at
updated_at
is_add_choices_active
is_voting_active

'''    
class Polls(BaseModel):
    title: str
    type: str
    is_add_choices_active: bool
    is_voting_active: bool
    created_by: int
    #created_at: datetime.datetime
    #updated_at: datetime.datetime

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/polls")
async def root():
    return {"polls": "Hello World"}

@app.get("/users")
async def root():
    return {"users": "Hello World"}

@app.post("/users/")
async def create_user(user: User):
    return user 

@app.post("/polls/")
async def create_poll(poll: Polls):
    return poll   