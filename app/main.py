from fastapi import FastAPI
from app.routers.userRouter import router as user_router
from app.routers.found_item_router import router as item_router
from app.routers.claim_router import router as claim_router
from app.routers.pickup_router import router as pickup_router

app = FastAPI(title="OuluFind API", version="1.0.0")

API_PREFIX = "/api/v1"

app.include_router(user_router, prefix=API_PREFIX)
app.include_router(item_router, prefix=API_PREFIX)
app.include_router(claim_router, prefix=API_PREFIX)
app.include_router(pickup_router, prefix=API_PREFIX)

@app.get("/")
def root():
    return {"message": "OuluFind API is running"}