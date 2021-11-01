from fastapi import FastAPI
import uvicorn
from apis.itchio.routes import router as itchio_router
from apis.linkedin.routes import router as linkedin_router

app = FastAPI()
app.include_router(itchio_router)
app.include_router(linkedin_router)


@app.get("/")
def root():
    return {"Welcome": "API Master"}


if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=5000, reload=True, workers=3)
