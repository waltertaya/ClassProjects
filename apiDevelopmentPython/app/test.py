from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class params(BaseModel):
    num1: int
    num2: int
    operation: str


@app.post("/calc")
async def calc(params: params):
    if params.operation == "add":
        return {"result": params.num1 + params.num2}
    elif params.operation == "subtract":
        return {"result": params.num1 - params.num2}
    elif params.operation == "multiply":
        return {"result": params.num1 * params.num2}
    elif params.operation == "divide":
        return {"result": params.num1 / params.num2}
    else:
        return {"result": "invalid operation"}


@app.get("/posts")
async def get_posts():
    return {"data": "All posts"}
