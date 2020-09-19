from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def main():
    return 'Hello World'

@app.get("/test")
async def test():
    return 'Test Tutorial'

if __name__ == '__main__':
   uvicorn.run(app, host="0.0.0.0", port=80, debug=True) 