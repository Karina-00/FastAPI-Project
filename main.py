from fastapi import FastAPI, HTTPException
from typing import Dict
from pydantic import BaseModel

app = FastAPI()
app.counter = 0

# Examples


class HelloResp(BaseModel):
    message: str


class GiveMeSomethingRq(BaseModel):
    first_key: str


class GiveMeSomethingResp(BaseModel):
    received: Dict
    constant_data: str = "python jest super"


@app.get("/hello/{name}", response_model=HelloResp)
def hello_name(name: str):
    return HelloResp(message=f"Hello {name}")


@app.get("/counter")
def counter():
    app.counter += 1
    return str(app.counter)


@app.post("/dej/mi/coś", response_model=GiveMeSomethingResp)
def receive_something(rq: GiveMeSomethingRq):
    return GiveMeSomethingResp(received=rq.dict())


# Homework
# 1
@app.get("/")
def root():
    return {"message": "Hello World during the coronavirus pandemic!"}


# 2
@app.get("/method")
def method_get():
    return {"method": "GET"}


@app.post("/method")
def method_post():
    return {"method": "POST"}


@app.put("/method")
def method_put():
    return {"method": "PUT"}


@app.delete("/method")
def method_delete():
    return {"method": "DELETE"}


# 3
app.counterId = -1
app.patients = []


class PatientRq(BaseModel):
    name: str
    surename: str


class PatientPost(BaseModel):
    id: int
    patient: PatientRq


@app.post("/patient", response_model=PatientPost)
def patient(rq: PatientRq):
    app.counterId += 1
    app.patients.append(rq)
    return PatientPost(id=app.counterId, patient=rq)


# 4
@app.get("/patient/{pk}", response_model=PatientRq)
def patient_get(pk: int):
    if len(app.patients) > pk > -1:
        return app.patients[pk-1]
    else:
        raise HTTPException(status_code=204, detail="no_content")

