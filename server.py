from fastapi import FastAPI, Form
import os
from typing import Annotated
from pydantic import BaseModel

server = FastAPI()

@server.post("/")
async def attendance(host: Annotated[str, Form()], username: Annotated[str, Form()], time: Annotated[str, Form()]):
    #TODO: get IP using Request object
    file = open("./attendance/attendance.log", "w")
    entry = {"host": host, "username": username, "time": time}
    file.write(str(entry))
    return entry
