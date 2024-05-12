#!/usr/bin/env python

import uvicorn
from fastapi import FastAPI
from settings import settings


app = FastAPI()
API_HOST: str = settings.config('api', 'host')
API_PORT: int = settings.config('api', 'port')
API_DEBUG: bool = settings.config('api', 'debug')


@app.get('/')
def index() -> dict[str, str]:
    return {'Hello': 'World'}


if __name__ == '__main__':
    uvicorn.run(app=app,
                host=API_HOST,
                port=API_PORT,
                log_level='DEBUG' if API_DEBUG else 'INFO',
                reload=API_DEBUG)
