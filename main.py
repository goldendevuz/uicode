from fastapi import FastAPI

app = FastAPI(
    title="Vercel + FastAPI",
    description="Vercel + FastAPI",
    version="1.0.0",
)

@app.get("/data")
async def get_data():
    return {"data": "some useful data"}
