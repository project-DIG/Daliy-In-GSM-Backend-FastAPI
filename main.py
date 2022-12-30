from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.api import api_router


app = FastAPI(title="DIG")
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/zz")
def zz():
    import redis
    from core.config import settings

    r = redis.StrictRedis(host=settings.REDIS_HOST)
    r.set("asd", "성공!!")
    return {"asd", r.get("asd").decode()}


@app.get("/zzzz")
def zzzz():
    import redis
    from core.config import settings

    r = redis.StrictRedis(host=settings.REDIS_HOST)
    return {"asd", r.get("asd").decode()}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
