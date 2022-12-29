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
def test():
    import redis
    from core.config import settings

    r = redis.StrictRedis(settings.REDIS_DB, settings.REDIS_PORT, settings.REDIS_DB)
    return r.get("asd")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
# git action test 1
