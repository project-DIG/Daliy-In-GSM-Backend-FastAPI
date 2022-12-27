from fastapi import FastAPI
from api.api import api_router


app = FastAPI(title="DIG")
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

# test Git action CI
