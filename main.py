from fastapi import FastAPI

from dbconfig import TORTOISE_ORM
from routes import router
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

# Include the router from routes.py
app.include_router(router)


@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI app!"}


register_tortoise(
    app=app,
    config=TORTOISE_ORM
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8123)
