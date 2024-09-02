from typing import Annotated

from fastapi import FastAPI, Path, HTTPException, Response, Body, Header, Cookie, Query
from fastapi import status as http_status_codes
import uvicorn
from uvicorn.config import LOGGING_CONFIG

from db_service.config import *
from db_service.db import Database

app = FastAPI(
    title='DB Service',
    version='1.0',
    description=''
)
db = Database(f'{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')


@app.get('/', status_code=http_status_codes.HTTP_200_OK)
async def root():
    with db.cursor() as cursor:
        cursor.execute('SELECT * FROM games')
        return cursor.fetchall()


if __name__ == '__main__':
    uvicorn_logging_config = LOGGING_CONFIG
    uvicorn_logging_config['formatters']['default']['fmt'] = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    uvicorn_logging_config['formatters']['access']['fmt'] = '%(asctime)s - %(levelname)s - %(client_addr)s - \"%(request_line)s\" %(status_code)s'

    uvicorn.run('main:app', host='127.0.0.1', port=8000, log_config=uvicorn_logging_config, reload=True) # TODO reload==debug
