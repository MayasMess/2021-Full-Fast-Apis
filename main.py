from fastapi import FastAPI
import uvicorn
from apis.itchio.routes import router as itchio_router

app = FastAPI()
app.include_router(itchio_router)


@app.get("/")
def root():
    return {"Welcome": "API Master"}


if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=4557, reload=True, workers=3)
