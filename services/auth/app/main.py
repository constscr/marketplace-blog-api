import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Auth Service")


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
