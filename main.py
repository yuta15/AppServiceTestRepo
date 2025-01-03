from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get('/')
async def test():
    return {'message': 'Hello World'}

@app.get('/test')
async def test2():
    return {'message': 'test'}

@app.post('/test2/{item}')
async def test3(item):
    return {'message': item}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=80)
