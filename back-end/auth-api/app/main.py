from fastapi import Depends, FastAPI

app = FastAPI(title='Auth API', version=0.1)


@app.get('/')
async def root():
    return {'message': 'Hello Auth API, I love you!!'}
