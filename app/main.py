from fastapi import FastAPI
from app.routers import example_router

app = FastAPI()

# Include the routers
app.include_router(example_router.router)

# Optional: Add a basic root endpoint
@app.get("/health")
async def health_status():
    return 'Healthy'

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
