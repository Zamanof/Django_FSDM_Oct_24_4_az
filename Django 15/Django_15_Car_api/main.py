from typing import List, Optional

from fastapi import FastAPI

from car_repository_service import _create_car, _get_car_by_id, _patch_car, _delete_car, _replace_car
from models import CarRead, CarCreate, CarUpdate

from in_memory_data import _store

app = FastAPI()


@app.post('/cars', response_model=CarRead, status_code=201)
def create_car(payload: CarCreate):
    return _create_car(payload)


@app.get('/cars', response_model=List[CarRead])
def get_all_cars(
        model: Optional[str]=None,
        manufacturer: Optional[str]=None,
        limit: int=100,
        offset: int=0
):
    items = list(_store.values())
    if model:
        items = [c for c in items if model.lower() in c.model.lower()]
    if manufacturer:
        items = [c for c in items if manufacturer.lower() in c.manufacturer.lower()]

    offset = (offset - 1) * limit
    return items[offset:offset+limit]

@app.get('/cars/{id}', response_model=CarRead)
def get_car(cid: int):
    return _get_car_by_id(cid)


@app.patch('/cars/{cid}', response_model=CarRead)
def patch_car(cid: int, payload: CarUpdate):
    return _patch_car(cid, payload)


@app.delete('/cars/{cid}')
def delete_car(cid: int):
    _delete_car(cid)
    return None


@app.put('/cars/{cid}', response_model=CarRead)
def update_car(cid: int, payload: CarCreate):
    return _replace_car(cid, payload)



